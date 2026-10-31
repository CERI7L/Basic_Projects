import re

from pathlib import Path
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr


def read_email(file_path: str) -> dict:
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Could not find file: {path}")

    if path.suffix.lower() != ".eml":
        raise ValueError("Please select an .eml file.")

    with path.open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    return {
        "subject": str(message.get("Subject", "")),
        "sender": str(message.get("From", "")),
        "reply_to": str(message.get("Reply-To", "")),
        "return_path": str(message.get("Return-Path", "")),
    }


def get_domain(address: str) -> str:
    return address.rsplit("@", 1)[1].lower() if "@" in address else ""


def screen_record(record: dict) -> str:
    findings = []

    sender_name, sender_address = parseaddr(record["sender"])
    _, reply_address = parseaddr(record["reply_to"])
    _, return_address = parseaddr(record["return_path"])

    sender_domain = get_domain(sender_address)
    reply_domain = get_domain(reply_address)
    return_domain = get_domain(return_address)

    if not sender_domain:
        findings.append("Missing or unrecognized sender email address.")

    if (
        sender_domain
        and reply_domain
        and sender_domain != reply_domain
    ):
        findings.append(
            f"Reply-To domain differs from sender domain: "
            f"{reply_domain} versus {sender_domain}."
        )

    if (
        sender_domain
        and return_domain
        and sender_domain != return_domain
    ):
        findings.append(
            f"Return-Path domain differs from sender domain: "
            f"{return_domain} versus {sender_domain}. "
            "Mailing services commonly cause this."
        )

    # Detect a display name that looks like a different email address.
    if "@" in sender_name:
        _, displayed_address = parseaddr(sender_name)

        if (
            get_domain(displayed_address)
            and sender_address
            and displayed_address.casefold() != sender_address.casefold()
        ):
            findings.append(
                f"Display name presents a different email address: "
                f"{displayed_address} versus {sender_address}."
            )

    if findings:
        return (
            "Assessment: Review needed\n\n"
            + "\n".join(f"- {finding}" for finding in findings)
            + "\n\nThese differences do not prove phishing."
        )

    return (
        "Assessment: No obvious header mismatches detected.\n"
        "This does not verify the sender or establish that the email is safe."
    )

def show_authentication_results(file_path: str) -> None:
    with Path(file_path).open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    headers = message.get_all("Authentication-Results", [])

    print("\n--- Recorded email authentication ---")

    if not headers:
        print("No Authentication-Results headers found.")
        return

    for number, header in enumerate(headers, start=1):
        # Put folded header lines onto one line for easier reading.
        header = " ".join(str(header).split())
        server = header.split(";", 1)[0].strip()

        print(f"\nHeader {number} — reporting server: {server}")

        for method in ("spf", "dkim", "dmarc"):
            # Capture each result and its accompanying recorded details.
            matches = re.findall(
                rf"(?:^|;)\s*{method}\s*=\s*"
                rf"([a-zA-Z0-9_-]+)([^;]*)",
                header,
                flags=re.IGNORECASE,
            )

            if not matches:
                print(f"\n{method.upper()}: not recorded")
                continue

            for result, details in matches:
                print(f"\n{method.upper()}: {result.lower()}")
                print(f"  Recorded details: {details.strip() or '(none)'}")

        print(f"\nFull authentication header:\n{header}")

    print("\nRecorded claims only; reporting-server trust is not checked.")

if __name__ == "__main__":
    file_path = input(
        "Enter the path to your .eml file: "
    ).strip().strip('"')

    try:
        email_record = read_email(file_path)

        print(f"\nSubject: {email_record['subject']}")
        print(f"From: {email_record['sender']}")
        print(f"Reply-To: {email_record['reply_to'] or '(not provided)'}")
        print(f"Return-Path: {email_record['return_path'] or '(not provided)'}")
        print()
        print(screen_record(email_record))
        show_authentication_results(file_path)

    except (OSError, ValueError) as error:
        print(f"Could not check email: {error}")
