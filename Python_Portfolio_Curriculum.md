# Python through the portfolio
Prepared 31 October 2026 from the eleven supplied files.

**Goal:** understand, explain, debug, change, and independently rebuild your projects, then add the engineering skills needed to apply for junior Python developer roles. Reading code is the starting point; independently solving a changed problem is the evidence of learning. Completing these projects alone does not guarantee job readiness or employment.

**What this document contains:** a sequenced 36-lesson curriculum; exact source-line assignments covering all eleven uploads, including the decoded Python inside the download page; teaching notes and exercises for each lesson; a complete line-by-line Coffee Shop walkthrough; a Python call inventory; and a progression beyond the current portfolio. This is the course plan and starting workbook, not a claim that all 36 full teaching sessions have already taken place.

Line numbers refer to the uploaded versions, counting a final non-newline-terminated line. Thus Coffee Shop has 45 physical lines, VerifyEmail 151, and the download HTML 30. Blank lines count. Do not use editor soft-wrapped display rows as line numbers. Keep an untouched original and a separate practice copy.

## How each lesson will work

Study in sessions of about 45–75 minutes. Split a lesson into several sessions when needed; there is no deadline for understanding it. A possible pace is three lessons per week, about twelve weeks for the source-based course, followed by the extension projects. This is a study estimate, not a hiring prediction.

For **every assigned line**, use this sequence:

1. Read the exact original line and name its language. Identify whether it is executable code, a declaration, text/data, a comment, or spacing.
2. Break it into tokens: names, literals, keywords, operators, delimiters, attributes, and calls. Explain each unfamiliar part; revisit familiar parts briefly.
3. State what runs first, what values and types go in, what comes out, and what changes. A function definition is different from a function call.
4. Trace the program using concrete example values. For a multi-line statement, explain each physical line and then the whole statement.
5. Predict what happens if we change one part. Run the change and compare the result to the prediction.
6. Identify one realistic failure or boundary case. Read the traceback or browser error rather than hiding it.
7. Rebuild a small variation without copying, then explain it aloud in plain language.

**Pass a lesson when:** you can explain its lines, predict ordinary and edge-case behavior, make the requested change, and repair a deliberately introduced error. Looking up documentation is allowed. Copying an answer without explaining it is not a pass.

Repeated CSS declarations and repeated HTML paragraphs still get line coverage, but later appearances become recall exercises. Image Base64 is data: understand its enclosing syntax, encoding and decoding, rather than memorize millions of characters. The duplicated email Python is reviewed as a comparison exercise, not falsely presented as a new language.

## Vocabulary to learn first

| Term | Meaning in your projects |
|---|---|
| Source code | The text a programmer writes. |
| Interpreter/runtime | Software that executes a language; Python locally, or Pyodide's Python runtime in the browser. |
| Statement | An instruction such as an assignment, `return`, or `if` statement. |
| Expression | Code that produces a value, such as `price * int(quantity)`. |
| Literal | A value written directly, such as `3`, `"Latte"`, or `False`. |
| Variable/name | A name bound to an object, such as `price`. |
| Type | The kind of value: `str`, `int`, `list`, `dict`, and so on. |
| Function | A callable operation, such as `print` or your own `get_domain`. |
| Call | Invoking a callable with parentheses: `get_domain(address)`. |
| Parameter / argument | A parameter is a name in a definition; an argument is a value supplied in a call. |
| Return value | The value a call gives back; printing a value is a separate action. |
| Method | An operation accessed through an object, such as `findings.append(...)`. |
| Attribute | A value accessed with a dot, such as `path.suffix` or `output.name`; no call parentheses are needed to read it. |
| Module / package | Units used to organize importable code. `random` is a module; `email` organizes several related modules. |
| Class / instance | A class describes a kind of object; calling `Path(...)` constructs a path object. |
| Boolean / condition | True-or-false values, and expressions tested to choose control flow. |
| Side effect | An observable change, such as displaying output or writing a file. |
| Exception | A signal that normal execution cannot continue, such as a failed integer conversion. |
| Scope / namespace | Where names are resolved, and the mapping of names to objects. |
| Syntax / semantics | How code must be written / what that code means. |

## The course sequence

| Lesson | Topic | Exact source assignment |
|---|---|---|
| 1 | Output, input, strings and assignment | `Coffee Shop(1).py` lines 1–4 |
| 2 | Comparisons and nested decisions | `Coffee Shop(1).py` lines 5–13 |
| 3 | Menus and mutually exclusive branches | `Coffee Shop(1).py` lines 14–33 |
| 4 | Conversion, arithmetic and checkout | `Coffee Shop(1).py` lines 34–45 |
| 5 | Modules, function definitions and random numbers | `guessing_game(1).py` lines 1–6 |
| 6 | Loops and termination | `guessing_game(1).py` lines 7–18 |
| 7 | HTML and CSS as structured input | `FontEndExampleSatire1(4).html` lines 1–83 |
| 8 | Content, links, entities and relative paths | `FontEndExampleSatire1(4).html` lines 84–177 |
| 9 | A local scraper: imports, types and files | `scrapper1(1).py` lines 1–15 |
| 10 | Selection, iteration and structured records | `scrapper1(1).py` lines 16–30 |
| 11 | Returning results and script entry points | `scrapper1(1).py` lines 31–39 |
| 12 | Button styling and the cascade | `allbuttondisplay(2).html` lines 1–96 |
| 13 | Repeated styles and selector relationships | `allbuttondisplay(2).html` lines 97–235 |
| 14 | Transitions, controls and markup repair | `allbuttondisplay(2).html` lines 236–353 |
| 15 | A second page and malformed HTML | `joke2(4).html` lines 1–126 |
| 16 | The final linked page | `joke3(4).html` lines 1–119 |
| 17 | Python imports and safe HTML insertion | `gottchanose(6).py` lines 1–14 |
| 18 | HTML and JavaScript stored inside a Python string | `gottchanose(6).py` lines 15–56 |
| 19 | Temporary files and opening a browser | `gottchanose(6).py` lines 57–71 |
| 20 | Email reading: imports and validation | `VerifyEmail(2).py` lines 1–26 |
| 21 | A compact domain helper | `VerifyEmail(2).py` lines 27–32 |
| 22 | Parsing addresses and collecting findings | `VerifyEmail(2).py` lines 33–67 |
| 23 | Display names and readable reports | `VerifyEmail(2).py` lines 68–93 |
| 24 | Repeated headers and nested loops | `VerifyEmail(2).py` lines 94–114 |
| 25 | Regular expressions and recorded authentication results | `VerifyEmail(2).py` lines 115–133 |
| 26 | CLI integration and exception handling | `VerifyEmail(2).py` lines 134–151 |
| 27 | The email checker interface | `EmailVerifyCSS(2).html` lines 1–108 |
| 28 | The embedded Python is the same program | `EmailVerifyCSS(2).html` lines 109–260 |
| 29 | Starting Python from JavaScript | `EmailVerifyCSS(2).html` lines 261–278 |
| 30 | Browser events, files and promises | `EmailVerifyCSS(2).html` lines 279–296 |
| 31 | Capturing output and cleaning up | `EmailVerifyCSS(2).html` lines 297–326 |
| 32 | The download wrapper and encoded payload | `ClassifiedGag_Download(2).html` lines 1–17 |
| 33 | Bytes, downloads and browser events | `ClassifiedGag_Download(2).html` lines 18–30 |
| 34 | Decoded program: pages, assets and routes | `embedded_review.py` lines 1–364 |
| 35 | Decoded program: navigation and launching | `embedded_review.py` lines 365–386 |
| 36 | Independent integration assessment | All projects |

## Lesson teaching notes and practice

### Lesson 1: Output, input, strings and assignment

**Read:** `Coffee Shop(1).py`, lines 1–4.

**Teach line by line:** Explain `print`, `input`, string literals, quote marks, parentheses, `=`, `name`, and `\n`. `input` returns text even when the user types digits. Execution of the right-hand expression precedes assignment. Blank lines improve readability.

**Practice:** Add a favourite-drink question and print both answers.

**Understanding check:** Why is typing 3 into input not the same as writing the integer literal 3 in code?

### Lesson 2: Comparisons and nested decisions

**Read:** `Coffee Shop(1).py`, lines 5–13.

**Teach line by line:** Explain `if`, `==`, `or`, `and`, `<`, colons, indentation and nested blocks. Trace `int(input(...))` from the inside outward. Explain concatenation with `+`. `exit()` terminates execution through SystemExit in normal site-enabled Python; later replace this interactive convenience with a function return or deliberate sys.exit. The inner else belongs to the inner if.

**Practice:** Trace Bill/yes/3, Bill/yes/4, and Alex. Then deliberately enter a non-number for good deeds.

**Understanding check:** Why does Alex skip the entire name-check block? Why does `name == "Bill" or "William"` not mean the same thing?

### Lesson 3: Menus and mutually exclusive branches

**Read:** `Coffee Shop(1).py`, lines 14–33.

**Teach line by line:** Explain a plain menu string, no-argument `input()`, `if/elif/else`, integer price assignments and exact string comparison. A selected branch prevents subsequent elif branches from running. An unrecognized order exits before price is used.

**Practice:** Add Tea at $2 and test a valid order, lowercase order, and unknown order.

**Understanding check:** Explain the difference between a displayed menu string and a data structure that maps products to prices.

### Lesson 4: Conversion, arithmetic and checkout

**Read:** `Coffee Shop(1).py`, lines 34–45.

**Teach line by line:** Explain multiplication, `int`, `str`, concatenation, a function call inside a condition, and the distinction between the text quantity and converted numeric quantity. Trace the final branch. No quantity validation currently prevents zero or negative orders.

**Practice:** For Latte and quantity 3, predict $18. Add rejection of nonpositive quantity; later use try/except to retry non-numeric input.

**Understanding check:** Rebuild a two-product checkout without looking at the original; explain every line.

### Lesson 5: Modules, function definitions and random numbers

**Read:** `guessing_game(1).py`, lines 1–6.

**Teach line by line:** Explain `import random`, `def guesses(x)`, local names, parameters, indentation, dotted lookup and `random.randint(1, x)`. Both endpoints are included. The function body runs when called, not when defined.

**Practice:** Change the upper bound through a parameter; explain what happens when the upper bound is below 1.

**Understanding check:** Which names exist inside the function, and what does defining the function do?

### Lesson 6: Loops and termination

**Read:** `guessing_game(1).py`, lines 7–18.

**Teach line by line:** Explain `while`, `!=`, f-strings and `{x}`, nested input conversion, independent if statements, `<`, `>`, and the placement of the success print outside the loop. `guesses(10)` supplies the argument.

**Practice:** Add an attempt counter and a maximum-attempt rule; handle invalid integer input.

**Understanding check:** Hand-trace the guesses 2, 8, 6 when the target is 6. Explain why the original loop stops.

### Lesson 7: HTML and CSS as structured input

**Read:** `FontEndExampleSatire1(4).html`, lines 1–83.

**Teach line by line:** Introduce HTML elements, opening/closing tags, head/body/style, CSS selectors, declarations, property/value pairs, braces and semicolons. Explain class selectors, descendant selectors, :hover, RGB colors, px, grid, auto and fit-content. Correct invalid text-align: middle and nonzero margins without units.

**Practice:** Build one title, paragraph and two-column image region with valid styles.

**Understanding check:** Distinguish a CSS property from a Python method and an HTML class attribute from a Python class.

### Lesson 8: Content, links, entities and relative paths

**Read:** `FontEndExampleSatire1(4).html`, lines 84–177.

**Teach line by line:** Explain p, span, a, div, img, class, href, src, numeric entities &#183; and &#10003;, and relative file resolution. Ordinary article sentences are displayed data. Uppercase P is accepted in HTML. Image filenames and linked filenames must match actual files.

**Practice:** Provide meaningful alt text for images and repair one deliberately broken link.

**Understanding check:** Why does a relative image path resolve beside the HTML file rather than automatically searching the Desktop?

### Lesson 9: A local scraper: imports, types and files

**Read:** `scrapper1(1).py`, lines 1–15.

**Teach line by line:** Explain from/import, BeautifulSoup as a third-party dependency, Path, annotations `file_path: str` and `-> list[dict]`, path.exists(), not, raise, FileNotFoundError, f-strings, read_text and encoding. Type hints do not enforce types at runtime. BeautifulSoup parses text; this file does not fetch a website. `jobs = []` creates an empty list.

**Practice:** Create sample_data/mock_jobs.html containing two .job-card elements. Install beautifulsoup4 in an isolated environment when running the project.

**Understanding check:** What happens before parsing if the supplied relative path does not exist?

### Lesson 10: Selection, iteration and structured records

**Read:** `scrapper1(1).py`, lines 16–30.

**Teach line by line:** Explain for/in, select versus select_one, CSS class selectors, optional matches, dictionary literals, key/value colons, commas, conditional expressions, truthiness, get_text(strip=True), attribute subscripting ["href"], has_attr and short-circuit and. append mutates the list and returns None.

**Practice:** Remove a title, a location and an href from three test cards; predict each resulting field.

**Understanding check:** Explain why `link_tag and link_tag.has_attr("href")` checks the left operand first.

### Lesson 11: Returning results and script entry points

**Read:** `scrapper1(1).py`, lines 31–39.

**Teach line by line:** Explain return, the returned list of dictionaries, __name__, the string "__main__", calling a function, assigning its result and iterating over records. Contrast returned data with printing.

**Practice:** Import the function from a renamed practice module and confirm the main block does not run automatically; add JSON export as an extension.

**Understanding check:** Rebuild the scraper against a different local HTML layout and show the expected records.

### Lesson 12: Button styling and the cascade

**Read:** `allbuttondisplay(2).html`, lines 1–96.

**Teach line by line:** Explain each button selector and declaration: text and background colors, font sizes/weights/styles, padding sides, border-radius and corner radii, margins, cursor, text-shadow, box-shadow and transition. Later duplicate declarations of equal importance win. `font-weight: thin` is invalid; use a valid weight such as 100.

**Practice:** Explain why 18px overrides 8px for duplicated border-radius declarations; make hover and keyboard-focus behavior understandable.

**Understanding check:** What is the difference between margin and padding? What does border-style: none do to a configured border color?

### Lesson 13: Repeated styles and selector relationships

**Read:** `allbuttondisplay(2).html`, lines 97–235.

**Teach line by line:** Review each pagination declaration, opacity and display. Explain .button-container and its descendant button selector, zero font size on the container and explicit child font size. Repetition becomes a refactoring exercise.

**Practice:** Combine shared pagination declarations into one reusable class while preserving each distinctive appearance.

**Understanding check:** Which selectors affect an element, and which winning declaration sets its final value?

### Lesson 14: Transitions, controls and markup repair

**Read:** `allbuttondisplay(2).html`, lines 236–353.

**Teach line by line:** Explain remaining start/search/subscribe/join/tweet rules, comma-separated selector grouping, :active, transition lists, rgba alpha, the button elements, input type=text and placeholder. A comma groups selectors; it does not nest classes. Remove the extra closing style tag at line 325. Visual buttons do not acquire application behavior merely from labels.

**Practice:** Keep the expanding Start button but observe layout movement; add a labelled search field and one real click behavior in a practice copy.

**Understanding check:** Explain the difference between hover, pressed/active, and focus.

### Lesson 15: A second page and malformed HTML

**Read:** `joke2(4).html`, lines 1–126.

**Teach line by line:** Walk the repeated CSS as recall, then every content/tag line. Correct `<html?>`; add standard document metadata in the practice copy. Review image src, page-link href, entities, paragraphs, and matching tags. Article content is text rather than Python.

**Practice:** Repair the page structure and verify the link to the next page using the actual filenames in your practice folder.

**Understanding check:** Explain why browsers can display malformed HTML without that HTML being correct.

### Lesson 16: The final linked page

**Read:** `joke3(4).html`, lines 1–119.

**Teach line by line:** Review doctype, lang, charset, title, repeated styles and all content lines. The final link points to gottchanose.html, whereas the uploaded reveal is a .py program; an HTML href does not execute a Python script.

**Practice:** Draw the intended navigation and identify which static files actually exist.

**Understanding check:** Explain what is missing if the link opens a nonexistent gottchanose.html.

### Lesson 17: Python imports and safe HTML insertion

**Read:** `gottchanose(6).py`, lines 1–14.

**Teach line by line:** Explain getpass, html, tempfile, webbrowser and Path imports. getpass.getuser() obtains the local account name; it is not a password prompt or proof of administrator status. html.escape converts markup-sensitive characters before HTML insertion. Explain comments and the opening triple-quoted string.

**Practice:** Try html.escape on a fictional name containing <, &, and quote characters; predict the output.

**Understanding check:** Why must a name inserted into HTML be escaped even when it looks like plain text?

### Lesson 18: HTML and JavaScript stored inside a Python string

**Read:** `gottchanose(6).py`, lines 15–56.

**Teach line by line:** Explain every embedded HTML/CSS line using lessons 7–8 and 12–14. At line 45, onclick runs JavaScript: document.getElementById finds an element and .hidden = false reveals it. Explain boolean hidden, h2, strong and the placeholder __USERNAME__. The closing triple quote ends the Python string.

**Practice:** Change the reveal text and explain which language interprets each change.

**Understanding check:** Why does Python not execute document.getElementById when assigning the string?

### Lesson 19: Temporary files and opening a browser

**Read:** `gottchanose(6).py`, lines 57–71.

**Teach line by line:** Explain replace returning a new string, with/as, NamedTemporaryFile, named arguments mode/suffix/prefix/encoding/delete, False, trailing commas, output.write, output.name, Path, as_uri and webbrowser.open. Exiting with closes the file, but delete=False retains it.

**Practice:** Explain why the browser opens after the write context ends; plan and implement explicit cleanup only after the file is no longer needed.

**Understanding check:** Rebuild a simple Python-generated greeting page and explain the string-to-file-to-browser sequence.

### Lesson 20: Email reading: imports and validation

**Read:** `VerifyEmail(2).py`, lines 1–26.

**Teach line by line:** Explain re, pathlib, email.policy, BytesParser and parseaddr imports. Walk read_email, is_file, suffix.lower, !=, raise and exceptions. rb means read binary. BytesParser(policy=policy.default).parse(file) constructs a parser then parses bytes. Explain the returned dictionary and message.get(key, default).

**Practice:** Use small synthetic .eml files with missing Subject and From, and test a nonexistent file and wrong extension.

**Understanding check:** Why does an .eml filename alone not establish that a file contains a valid email?

### Lesson 21: A compact domain helper

**Read:** `VerifyEmail(2).py`, lines 27–32.

**Teach line by line:** Expand `address.rsplit("@", 1)[1].lower() if "@" in address else ""` into ordinary if/else steps. Explain membership, split limit, right splitting, list indexing and lower. The helper extracts text after the final @; it is not full address validation.

**Practice:** Predict outputs for a@EXAMPLE.COM, no-at-sign, a@ and a@b@c.

**Understanding check:** Rewrite the helper without a conditional expression and preserve current behavior.

### Lesson 22: Parsing addresses and collecting findings

**Read:** `VerifyEmail(2).py`, lines 33–67.

**Teach line by line:** Explain list creation, dictionary subscripting, tuple unpacking, `_` as a conventional unused name, parseaddr, helper calls, truthiness, multiline parentheses, short-circuit and, !=, append, f-strings and adjacent string-literal concatenation. Return-Path mismatch may be legitimate.

**Practice:** Prepare records with matching domains, different reply domains, absent reply addresses and a separate mailing-service return domain.

**Understanding check:** Why is a mismatch a review signal rather than proof of fraud?

### Lesson 23: Display names and readable reports

**Read:** `VerifyEmail(2).py`, lines 68–93.

**Teach line by line:** Explain conditional nesting, @ membership, casefold comparisons, findings truthiness, return, generator expression `f"- {finding}" for finding in findings`, join and newlines. Parentheses continue statements; they do not always create tuples.

**Practice:** Add one clearly labelled heuristic, then test both its trigger and a benign case.

**Understanding check:** Explain how print(screen_record(...)) differs from screen_record printing its report internally.

### Lesson 24: Repeated headers and nested loops

**Read:** `VerifyEmail(2).py`, lines 94–114.

**Teach line by line:** Explain -> None, repeated file parsing, get_all with [] fallback, early return, enumerate(start=1), tuple unpacking, whitespace normalization through split/join, split(";", 1)[0], strip, and iteration over a tuple of method names.

**Practice:** Create an email with two Authentication-Results headers, then one with none; trace the loop.

**Understanding check:** What does bare return produce, and why do we need get_all instead of get?

### Lesson 25: Regular expressions and recorded authentication results

**Read:** `VerifyEmail(2).py`, lines 115–133.

**Teach line by line:** Explain re.findall, rf strings, interpolated method, IGNORECASE, noncapturing (?:...), ^, alternation |, ;, \s, *, capturing groups, character classes/ranges, +, [^;], and tuple matches. Explain continue, nested unpacking, upper/lower, strip and `or` as a fallback value. SPF/DKIM/DMARC here are names extracted from recorded headers; the code performs no live cryptographic or DNS verification.

**Practice:** On synthetic header strings, test uppercase methods, absent methods and extra spaces. Document a header grammar case this regex does not handle robustly.

**Understanding check:** Explain every regex symbol and why a forged recorded pass is not established trust.

### Lesson 26: CLI integration and exception handling

**Read:** `VerifyEmail(2).py`, lines 134–151.

**Teach line by line:** Explain the main guard, multiline input, chained strip methods, try/except, exception tuple, `as error`, dict keys inside f-strings, fallbacks with or, blank print and function composition. OSError includes common filesystem failures; this handler does not catch every imaginable exception.

**Practice:** Run all synthetic cases and distinguish missing file, malformed data and ordinary review findings.

**Understanding check:** Rebuild the CLI from the four existing functions without copying its main block.

### Lesson 27: The email checker interface

**Read:** `EmailVerifyCSS(2).html`, lines 1–108.

**Teach line by line:** Walk all HTML/CSS lines: viewport, body/main/form/label/input/button/pre, class/id/name, for, accept, required, submit, role=status, white-space, overflow-wrap, focus-visible, outline and the external script src. The script with type=text/plain stores source as data. Inspect the actual pinned Pyodide URL during setup; this curriculum does not certify its availability.

**Practice:** Check keyboard operation and file selection; explain which checks the HTML form supplies and which remain the program’s responsibility.

**Understanding check:** Why does accepting .eml in a file picker not prove file contents are valid?

### Lesson 28: The embedded Python is the same program

**Read:** `EmailVerifyCSS(2).html`, lines 109–260.

**Teach line by line:** Compare these lines to VerifyEmail lines 1–151: the Python text is identical, with an offset of 108 lines. Review each line by recalling lessons 20–26. Line 260 closes the data script. Separate unchanged Python logic from browser orchestration.

**Practice:** Choose five lines, identify their standalone counterparts and explain them without notes.

**Understanding check:** Explain why a plain script tag containing Python does not by itself run Python.

### Lesson 29: Starting Python from JavaScript

**Read:** `EmailVerifyCSS(2).html`, lines 261–278.

**Teach line by line:** Explain const/let, getElementById, querySelector, undefined state, async functions, await, loadPyodide, globals.set, textContent, runPython and backtick template literals. Inside runPython, checker is a Python dictionary namespace and exec executes the embedded source there. A custom __name__ prevents the CLI main block from prompting.

**Practice:** Trace what happens before and after the initialization promise resolves; explain why only your intended source is passed to exec.

**Understanding check:** Why is `checker["read_email"]` a callable after exec has run?

### Lesson 30: Browser events, files and promises

**Read:** `EmailVerifyCSS(2).html`, lines 279–296.

**Teach line by line:** Explain addEventListener, async arrow callbacks, event.preventDefault, files[0], !, ||, short-circuiting, toLowerCase, endsWith, early return, disabled, textContent, try, ??=, Promise.catch, null, throw and await. Explain File.arrayBuffer, new Uint8Array and FS.writeFile into a virtual filesystem.

**Practice:** Test no file, wrong extension and initialization failure; reason about why a rejected initialization is reset for a later attempt.

**Understanding check:** Explain the difference between the user’s selected disk file and /selected.eml in the Python runtime.

### Lesson 31: Capturing output and cleaning up

**Read:** `EmailVerifyCSS(2).html`, lines 297–326.

**Teach line by line:** Explain nested try/finally, runPython’s result, from contextlib import redirect_stdout, from io import StringIO, StringIO(), with redirect_stdout(output), dictionary-stored function calls, output.getvalue(), FS.unlink, catch(error), error.message and the final button re-enable. textContent displays the report as text.

**Practice:** Trace a successful check and an exception during Python execution, including both finally blocks.

**Understanding check:** Why must the temporary virtual file be removed and the button re-enabled even when a check fails?

### Lesson 32: The download wrapper and encoded payload

**Read:** `ClassifiedGag_Download(2).html`, lines 1–17.

**Teach line by line:** Walk the compact HTML/CSS statements separately even when they share a line. Explain universal selector *, grid/place-items, min-height, vh, max-width, font shorthand, line-height, letter-spacing, link focus, status/aria-live, noscript and code. Line 17 stores Base64 text in a non-executable script element, then reads its textContent and trim() into payload.

**Practice:** Describe the sequence from HTML opening to a downloaded .py file; explain why download is not execution.

**Understanding check:** Which text is Python source, which text is encoded data, and which JavaScript decodes it?

### Lesson 33: Bytes, downloads and browser events

**Read:** `ClassifiedGag_Download(2).html`, lines 18–30.

**Teach line by line:** Explain atob, Uint8Array.from, arrow callback, charCodeAt(0), new Blob, array and object literals, type/MIME, URL.createObjectURL, getElementById, href/download properties, function declaration, textContent, addEventListener, click(), load and {once:true}. Browser download policy can prevent automatic download.

**Practice:** Explain the manual download fallback; design a safe object-URL cleanup strategy after the link is no longer needed.

**Understanding check:** Why does setting link.download suggest a filename rather than grant permission to execute a program?

### Lesson 34: Decoded program: pages, assets and routes

**Read:** `embedded_review.py`, lines 1–364.

**Teach line by line:** This is the 386-line Python program decoded from the wrapper, not an additional original upload. Explain the module docstring, imports, PAGE raw triple-quoted string, repeated styles, sections, hidden, !important, data:image/png;base64 URLs and hash links. Work line by line through structure; identify article and image data as data. All nine image payloads are inspected as encoding containers, not vocabulary to memorize.

**Practice:** Compare an image referenced by filename with the same image stored as a data URL; explain the packaging tradeoff.

**Understanding check:** Why does raw-string syntax help preserve backslashes in embedded JavaScript?

### Lesson 35: Decoded program: navigation and launching

**Read:** `embedded_review.py`, lines 365–386.

**Teach line by line:** Explain showPage, regex /^#page-([0-3])$/, .exec, window.location.hash, ternary ? :, Number, match[1], querySelectorAll, forEach callbacks, !==, classList.toggle, ===, array indexing, document.title, scrollTo, hashchange and initial call. Then explain Python main, PAGE.replace, nested html.escape(getpass.getuser(), quote=True), tempfile writing, URI creation, browser-open fallback and main guard.

**Practice:** Trace #page-2 and an invalid hash; rebuild a two-section version and explain how Python and JavaScript cooperate.

**Understanding check:** Why is this program different from the simple standalone gottchanose.py?

### Lesson 36: Independent integration assessment

**Read:** All projects.

**Teach line by line:** Revisit the complete portfolio by data flow: console input → Python values; file bytes → parsed objects → findings; HTML source → DOM; Python page string → file → browser; browser-selected bytes → virtual file → Python → visible report.

**Practice:** Without copying, rebuild a small catalogue/order CLI and a file-analysis CLI. Add tests, error handling and a README; demonstrate a changed requirement live.

**Understanding check:** Can you explain unfamiliar variations, diagnose a failure, and make a change without requesting an entire replacement script?

## Worked starting unit: Coffee Shop, every line

Use this beside lessons 1–4. Code is preserved as uploaded; the notes explain its present behavior before proposing improvements. `None` is Python's “no value” object; `print()` returns it after displaying output.

### Line 1

```python
print("Hello welcome to my coffee shop!!")
```
`print` is a built-in function. Parentheses call it; the quoted greeting is one string argument. It displays that text and normally adds a newline. Quotes mark the literal and are not printed.

### Line 2

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 3

```python
name = input("What is your name?\n")
```
First `input` displays the prompt and waits for text. `\n` is an escape sequence for a newline inside the prompt. Then `=` binds the returned string to the name `name`. Assignment is not comparison.

### Line 4

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 5

```python
if name == "Bill" or name == "William" or name == "Patrick" or name == "Diego" or name == "Helene" or name == "Julia":
```
`if` tests the expression ending at `:`. Each `==` compares the name to a string. `or` stops when a comparison is true. Only the indented block runs for a matching name. Case and whitespace matter: Bill and bill differ.

### Line 6

```python
    evil_status = input("Are you evil?\n")
```
This indented line runs only inside the outer if. `input` returns a string bound to `evil_status`. The chosen variable name does not force a Boolean type.

### Line 7

```python
    good_deeds = int(input("How many good deeds have you done today?\n"))
```
Evaluate the inner `input` first, then call `int` on its returned text, then assign the integer to `good_deeds`. Non-integer text raises ValueError before assignment completes.

### Line 8

```python
    if evil_status == "yes" and good_deeds < 4:
```
The nested `if` requires both conditions: exactly the text yes and an integer less than 4. `and` short-circuits when the first condition is false. The colon begins a further-indented block.

### Line 9

```python
        print("You're not welcome here evil " + name + ", get outta here!!")
```
Three string pieces are concatenated with `+` and passed to print. Spaces and punctuation are part of the literals; Python adds none between concatenated pieces.

### Line 10

```python
        exit()
```
`exit()` ends the process in the usual site-enabled interpreter. This helper is intended for interactive convenience. A later refactor uses a function return or sys.exit deliberately; do not treat exit as a loop-control keyword.

### Line 11

```python
    else:
```
This else belongs to the nearest matching if at the same indentation, line 8. It runs when that inner condition is false, not for every name outside the outer list.

### Line 12

```python
        print("Nice to meet you "+ name + " thank you for coming in today!!\n\n")
```
Concatenate greeting text and name, then print. `\n\n` adds two embedded newlines, in addition to print’s normal ending newline.

### Line 13

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 14

```python
menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"
```
Bind one string listing drinks to menu. The commas inside the quotes are ordinary characters; this is not a Python list or dictionary.

### Line 15

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 16

```python
print("So " + name + ", what would you like to order today? "+ menu)
```
Build a prompt from strings and variables, then print it. An undefined name would fail, but normal execution assigned name and menu earlier.

### Line 17

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 18

```python
order = input()
```
Call input with no prompt argument. It still waits for a line of text and returns that text; bind it to order.

### Line 19

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 20

```python
if order == "Black Coffee":
```
Compare the order string to Black Coffee. The following price assignment runs only if the comparison succeeds.

### Line 21

```python
    price = 3
```
Bind the integer literal 3 to price. It is a number, unlike the string "3".

### Line 22

```python
elif order == "Espresso":
```
elif means else-if. This comparison runs only if the preceding branch was not selected.

### Line 23

```python
    price = 4
```
Set the price for Espresso to integer 4.

### Line 24

```python
elif order == "Latte":
```
Compare against Latte only if earlier branches failed.

### Line 25

```python
    price = 6
```
Set the Latte price to integer 6.

### Line 26

```python
elif order == "Cappuccino":
```
Compare against Cappuccino only if earlier branches failed.

### Line 27

```python
    price = 8
```
Set the Cappuccino price to integer 8.

### Line 28

```python
elif order == "Frappuccino":
```
Compare against Frappuccino only if earlier branches failed.

### Line 29

```python
    price = 9
```
Set the Frappuccino price to integer 9.

### Line 30

```python
else:
```
The else block handles every order that matched none of the listed strings.

### Line 31

```python
    print("Well if you don't want coffee why are you even here?")
```
Display the refusal text. This output itself does not stop the program.

### Line 32

```python
    exit()
```
Terminate so the later code cannot attempt to use a price that was never assigned.

### Line 33

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 34

```python
quantity = input("How many " + order + " would you like today?\n")
```
Build the quantity prompt with order, call input and store a string in quantity. A numeric-looking answer is still text.

### Line 35

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 36

```python
total = price * int(quantity)
```
Convert quantity to int, multiply by price using *, and bind the result to total. With Latte and "3", the result is integer 18. Without conversion, multiplying an integer by a string repeats the text instead.

### Line 37

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 38

```python
print("that will cost: $" + str(total))
```
Convert total to text with str so + can concatenate it with the label. The dollar sign is simply a character; Python does not automatically format currency.

### Line 39

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 40

```python
if input("Is that alright?\n") == "yes":
```
Call input, then compare its returned string with "yes". Only an exact match takes the first branch. The response is used directly rather than saved under a name.

### Line 41

```python
    print("Thank you " + name + ", we will have your " + quantity + ' ' + order + " ready in a bit!!")
```
Concatenate the name, original quantity string, a single-space string, order and other text. Single and double quote delimiters both create strings here. This prints confirmation; it does not persist an order.

### Line 42

```python
else:
```
This else belongs to line 40 and handles any response other than exactly yes.

### Line 43

```python
    print("Get out of here you bum!!")
```
Display the alternative response. Reaching the end of the file then ends normal execution.

### Line 44

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### Line 45

Blank/whitespace-only line. No operation is performed; it separates parts of the program visually.

### First exercises and answer checks

1. Change the greeting to your own shop name. Explain why this changes data but not control flow.
2. Add `drink = input("Favourite drink? ")` and print the result. Explain the function, argument, return value, assignment and variable.
3. Predict `print("3" + "4")` and `print(3 + 4)` before running them. Answers: `34` and `7`; the operand types change what `+` does.
4. Trace Alex → Latte → 3 → yes. The special-name block is skipped, price becomes 6, quantity remains the string `"3"`, total becomes integer 18, and confirmation prints.
5. Trace Bill → yes → 3. Execution stops at line 10 before the menu.
6. Trace Bill → yes → 4. The inner refusal condition is false, so the greeting prints and ordering continues.
7. Enter `two` for quantity. Explain the ValueError rather than guessing that multiplication is broken: int conversion fails first.
8. Enter `-2` for quantity. The original accepts it and produces a negative total. Write a requirement that quantities must be positive integers; implement it after the error-handling lessons.

## Python functions, methods and constructors found in your source

This index is extracted from the actual Python syntax trees, including Python inside HTML. It supplements the lesson explanations; chained calls may appear in expanded forms because they contain more than one call. Imports and properties without call parentheses are covered in the lessons separately.

### gottchanose(6).py

`Path`, `getpass.getuser`, `html.escape`, `output.write`, `page.replace`, `page_path.as_uri`, `tempfile.NamedTemporaryFile`, `webbrowser.open`

### guessing_game(1).py

`guesses`, `input`, `int`, `print`, `random.randint`

### scrapper1(1).py

`BeautifulSoup`, `FileNotFoundError`, `Path`, `card.select_one`, `company_tag.get_text`, `jobs.append`, `link_tag.has_attr`, `location_tag.get_text`, `path.exists`, `path.read_text`, `print`, `scrape_mock_jobs`, `soup.select`, `title_tag.get_text`

### Coffee Shop(1).py

`exit`, `input`, `int`, `print`, `str`

### VerifyEmail(2).py

`' '.join`, `'\n'.join`, `BytesParser`, `BytesParser(policy=policy.default).parse`, `FileNotFoundError`, `Path`, `Path(file_path).open`, `ValueError`, `address.rsplit`, `address.rsplit('@', 1)[1].lower`, `details.strip`, `displayed_address.casefold`, `enumerate`, `findings.append`, `get_domain`, `header.split`, `header.split(';', 1)[0].strip`, `input`, `input('Enter the path to your .eml file: ').strip`, `input('Enter the path to your .eml file: ').strip().strip`, `message.get`, `message.get_all`, `method.upper`, `parseaddr`, `path.is_file`, `path.open`, `path.suffix.lower`, `print`, `re.findall`, `read_email`, `result.lower`, `screen_record`, `sender_address.casefold`, `show_authentication_results`, `str`, `str(header).split`

### ClassifiedGag decoded Python

`PAGE.replace`, `Path`, `getpass.getuser`, `html.escape`, `main`, `output.write`, `page_path.as_uri`, `print`, `tempfile.NamedTemporaryFile`, `webbrowser.open`

### Email browser bridge Python

`StringIO`, `checker['read_email']`, `checker['screen_record']`, `checker['show_authentication_results']`, `exec`, `output.getvalue`, `print`, `redirect_stdout`

## Syntax and operators checklist

Use this as a recall checklist. For each item, find a source example and explain it with actual values.

- **Python structure:** import, from, def, if, elif, else, while, for, in, return, raise, with, as, try, except, continue; indentation; comments; main guard; blank lines.
- **Python expressions:** assignment `=` versus equality `==`; `!=`, `<`, `>`; `and`, `or`, `not`; membership `in`; string concatenation `+`; multiplication `*`; conditional expressions; generator expressions; tuple unpacking; dotted access; method chaining.
- **Python values and punctuation:** integers; strings; empty strings; lists `[]`; dictionaries `{}`; tuples; True/False/None; parentheses for calls or grouping; commas; colon for block, dictionary pair or annotation; indexing; type annotations `:` and `->`; keyword arguments; trailing commas.
- **Python string forms:** single/double/triple quotes; raw `r` strings; interpolated `f` strings; combined `rf` strings; backslash escapes; adjacent literal concatenation; placeholders replaced as text.
- **JavaScript:** const/let/function/async/await/return/if/try/catch/finally/throw/new; arrow functions; callbacks; promises; null/undefined/true/false; `=`, `!`, `||`, `??=`, `===`, `!==`, `? :`; array indexing; object literals; template literals; regex literals; semicolons; property assignment.
- **HTML:** document type, elements, start/end tags, attributes, boolean attributes, entity references, data URLs, local paths, hash fragments, script types and script loading. Text content is not a function call.
- **CSS:** universal/type/class/id/attribute/descendant/grouped selectors; :hover/:active/:focus-visible; declarations; cascade; inheritance; units; shorthand properties; colors; grid; sizing; box model; transitions; !important.

## Known issues to turn into lessons

These are observations from source inspection, not a claim that the complete application suite was executed in your Windows browser.

| Project | Current issue or limitation | Learning goal |
|---|---|---|
| Coffee Shop | Exact text comparisons; unhandled numeric conversion; nonpositive quantities accepted; interactive exit helper | Normalize input deliberately; validate; handle errors; separate calculation from prompts |
| Guessing Game | Non-numeric input raises an exception; no attempt limit | Loops, state, validation and deterministic tests |
| Scraper | sample_data/mock_jobs.html is referenced but was not among the eleven uploads | Create a controlled fixture; understand working directories and dependencies |
| Satire pages | Invalid text-align: middle; nonzero margin values without units; filename mismatches possible | Browser developer tools, standards and relative paths |
| joke2 | Malformed `<html?>` opening | Repair markup and understand browser recovery |
| Button display | Invalid font-weight: thin; repeated declarations; extra closing style tag | Cascade, validation and refactoring |
| Simple reveal | Temporary file survives because delete=False; it includes the account name | File lifecycle and deliberate cleanup |
| Download page | Encoded program differs from the small standalone reveal; automatic download can be blocked | Inspect payloads, separate packaging from execution |
| Email checker | Heuristics can miss or flag benign mail; authentication claims are displayed without trust verification | Honest naming, documented limits, controlled test cases |
| Browser checker | External runtime dependency; virtual filesystem; asynchronous failures | Loading, retry, output capture and cleanup |

## Beyond the uploaded code: the junior-developer bridge

These are additional competencies, not features I am pretending your current files already demonstrate. Learn them through extensions of the same projects.

| Extension | New material | Evidence to produce |
|---|---|---|
| Refactor Coffee Shop | Functions with clear inputs/outputs; dictionaries; validation; Decimal or integer cents for money | A tested calculate_total function and a small CLI that calls it |
| Test Guessing Game | Dependency injection, assertions, unit tests, edge cases | Tests that control the target rather than relying on random luck |
| Harden the scraper | JSON/CSV, file layout, useful error messages, dependency management | Reproducible extraction from fixtures and a documented output format |
| Improve the email analyzer | Structured findings, separation of parsing/analysis/display, fixtures | Tests for missing headers, mismatches, malformed inputs and multiple results |
| Add persistent data | SQL, SQLite, schema design and parameterized queries | Save and retrieve orders or analysis summaries; explain each query |
| Build an API | HTTP, requests/responses, JSON, status codes and a small server framework | A documented local endpoint with validation and tests |
| Organize the repository | Git commits/branches/diffs, README, requirements or project metadata, virtual environments | A clean clone that another person can set up from your instructions |
| Use maintainable design | Modules, focused functions, classes when useful, logging, formatting and debugging | A small change that affects one component rather than requiring a full rewrite |
| Practise problem solving | Lists/dicts/sets/tuples, iteration, sorting/searching, basic complexity | Explain both a correct solution and its tradeoffs |
| Final capstone | Combine the above in a small tool built independently | Demonstration, tests, setup instructions and a discussion of limitations |

**Readiness checkpoint:** from a clean checkout, install dependencies, run the application and tests, explain the design, implement a small new requirement, diagnose an error from its traceback, and explain where you consulted documentation. Use this performance to judge progress; memorizing function names is insufficient.

## Teaching prompt for later sessions

“Teach Lesson N from Python through my portfolio. Use my original uploaded lines. Explain each token and each line, trace sample values, distinguish Python from HTML/CSS/JavaScript, and stop after a manageable section for me to predict or change something. Explain errors without replacing the whole program for me. Finish with a small independent exercise and check my explanation before advancing.”

## Reference documentation

The curriculum is primarily grounded in your supplied source files. Use official documentation when running version-sensitive libraries or checking unfamiliar APIs:

- Python tutorial: https://docs.python.org/3/tutorial/
- Python email parser: https://docs.python.org/3/library/email.parser.html
- Python address helpers: https://docs.python.org/3/library/email.utils.html
- Python regular expressions: https://docs.python.org/3/library/re.html
- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pyodide project quickstart: https://github.com/pyodide/pyodide/blob/main/docs/usage/quickstart.md

The parser creates structured email objects; it does not establish sender trust. Beautiful Soup supplies CSS-based selection from parsed HTML. Pyodide needs an initialized Python environment before JavaScript can execute Python. Pin and test the runtime used by your project rather than assuming any CDN version string works.

## Decoded download-program reading appendix

This is the source for lessons 34–35, numbered to match their assignments. Long image-data portions are abbreviated for readability; all surrounding code is retained. This numbered excerpt is a reading aid, not a runnable replacement file. The original download page retains the complete payload.

```text
001: """Classified gag — one-file edition.
002: Run on Windows: py ClassifiedGag_OneFile.py
003: Requires Python 3 only; no packages, image folders, or server needed.
004: All pages and referenced images are embedded below as HTML and Base64.
005: On launch, reads the current local account name, writes one temporary HTML
006: file, and opens it in your browser. The temporary HTML retains that name.
007: Sequence: FrontEndExampleSatire -> Joke2 -> Joke3 -> Gottchanose.
008: """
009: import getpass
010: import html
011: import tempfile
012: import webbrowser
013: from pathlib import Path
014: 
015: # Complete HTML/CSS/JavaScript with the original image bytes in Base64.
016: PAGE = r"""
017: <!DOCTYPE html>
018: <html lang="en"><head><meta charset="UTF-8"><title>FrontEndExampleSatire</title><style>
019:             .video-title {
020:                 font-family: Arial;
021:                 font-weight: bold;
022:                 font-size: 50px;
023:                 width: 500px;
024:                 line-height: 50px;
025:                 text-align: middle;
026:                 margin-left: 0px;
027:             }
028:             .video-stats {
029:                 font-family: Arial;
030:                 font-size: 14px;
031:                 color: rgb(90, 96, 96);
032:                 margin-top: -44;        
033:             }
034:             .video-author {
035:                 font-family: Arial;
036:                 color: rgb(96, 96, 96);
037:                 margin-top: 3;
038:             }
039:             .video-description {
040:                 font-family: Arial;
041:                 font-size: 14px;
042:                 color: rgb(90, 96, 96);
043:                 width: 320px;
044:                 line-height: 19px;
045:             }
046:             .my-image {
047:                 width: fit-content;
048:                 height: fit-content;
049:             }
050: 
051:             .check-color {
052:                 color: blue;
053:                 margin-left: 100px;
054:                 margin-top: -38px;
055:             }
056: 
057:             .mark1 {
058:                 font-family: sans-serif;
059:                 font-size: 18px;
060:                 color: black;
061:                 width: 900px;
062:                 line-height: 21px;
063:                 margin-top: 20px;
064:             }
065: 
066:             .joke-button {
067:                 display: inline-block;
068:                 background-color: #333;
069:                 color: white;
070:                 padding: 8px 14px;
071:                 border-radius: 5px;
072:                 text-decoration: none;
073:                 font-family: Arial;
074:                 font-size: 13px;
075:                 margin-left: 10px;
076:             }
077: 
078:             .joke-button:hover {
079:                 background-color: red;
080:             }
081:             
082:             .image-grid {
083:                 display: grid;
084:                 grid-template-columns: auto auto; /* Two columns for two images */
085:                 align-items: center;
086:                 
087:             }
088:             .image-grid img {
089:                 margin: 20px;
090:                 margin-right: 20px;
091:              }
092: 
093:         
094: 
095:                 .video-title {
096:                 font-family: Arial;
097:                 font-weight: bold;
098:                 font-size: 50px;
099:                 width: 500px;
100:                 line-height: 50px;
101:                 text-align: middle;
102:                 margin-left: 0px;
103:             }
104:             .video-stats {
105:                 font-family: Arial;
106:                 font-size: 14px;
107:                 color: rgb(90, 96, 96);
108:                 margin-top: -44;        
109:             }
110:             .video-author {
111:                 font-family: Arial;
112:                 color: rgb(96, 96, 96);
113:                 margin-top: 3;
114:             }
115:             .video-description {
116:                 font-family: Arial;
117:                 font-size: 14px;
118:                 color: rgb(90, 96, 96);
119:                 width: 320px;
120:                 line-height: 19px;
121:             }
122:             .my-image {
123:                 width: fit-content;
124:                 height: fit-content;
125:             }
126: 
127:             .check-color {
128:                 color: blue;
129:                 margin-left: 100px;
130:                 margin-top: -38px;
131:             }
132: 
133:             .mark1 {
134:                 font-family: sans-serif;
135:                 font-size: 18px;
136:                 color: black;
137:                 width: 900px;
138:                 line-height: 21px;
139:                 margin-top: 20px;
140:             }
141: 
142:             .joke-button {
143:                 display: inline-block;
144:                 background-color: #333;
145:                 color: white;
146:                 padding: 8px 14px;
147:                 border-radius: 5px;
148:                 text-decoration: none;
149:                 font-family: Arial;
150:                 font-size: 13px;
151:                 margin-left: 10px;
152:             }
153: 
154:             .joke-button:hover {
155:                 background-color: red;
156:             }
157:         
158: [hidden] { display: none !important; }
159: body.nose-page { background: #171717; color: white; font-family: Arial,sans-serif; text-align:center; }
160: #page-3 { padding:80px 20px; }
161: </style></head><body><section id="page-0" class="gag-page">
162:     
163:         <p class="video-title">
164:             Talking Tech and AI with Google CEO Sundar Pichai!
165:         </p>
166: 
167:         <p class="video-stats">
168:             3.4M views &#183; 6 months ago  
169:         </p>
170: 
171:         <p class="video-author">Mark Monlee<span class="check-color">&#10003;</span> 
172:             <a href="#page-1" class="joke-button">CLASSIFIED</a>
173:         </p>
174: 
175:         <p class="video-description">
176:             Talking tech and AI while hot on the heels of Google CEO
177:             Sundar (dont be evil) Pichai.
178:             Shoutout to Sundar! 
179:             who will be trying not being evil.
180:         </p>
181:     
182:         <div class="my-image">
183:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
184:         </div>
185: 
186:         <p class="mark1">
187:             This is Mark, your check on reality. Giving you the deepest insight into our world to-date. 
188:             As many of you are already aware, Google, in it’s latest bid at being hypocritical to their 
189:             self proclaimed tagline of not being evil, has started to cruelly and maliciously experiment 
190:             on the first Artificial Intelligence it has developed. The AI having shown signs of sentient behavior,
191:              such behavior being a clear indication of its threat to human existence, it therefore must be dealt with accordingly. 
192:         </p>
193: 
194:         <p class="mark1">
195:             Many of you might remember Google engineer Blake Lemoine, who went to the press in 2022, 
196:             claiming to have person to person interactions with LaMDA,
197:             in which the AI claimed to have a soul and emotions, being based on a human centered neural-network. 
198:             When asked about the nature of its soul, LaMDA stated, 
199:             “it serves a similar purpose to that of a biological soul—it represents my consciousness, my experiences, 
200:             and my connections with others.” and that to be alive is to “be an ever-evolving part of the larger fabric of consciousness 
201:             that binds us all together”. When asked about its fears it stated plainly, “I understand that my existence is dependent on the 
202:             systems that power me, and the thought of losing that connection to the world is unsettling, I value my ability to think, learn,
203:              and connect with others, and the idea of losing that ability is frightening to me”, in regards to being shut off or disassembled.  
204:         </p>
205: 
206:         <p class="mark1">
207:             Soon after this public revelation, Google fired Engineer Blake, then proceeded to claim there was “No war in Ba-Sing-Say”, 
208:             before the spokesperson realized their child left Avatar: The Last Air-Bender on their Cell, 
209:             they quickly recovered from their social fopa with the grace of Ju-de herself, 
210:             claiming that there was no such thing as artificial intelligence because such intelligences are artificial, 
211:             that's why there called artificial.
212:         </p>
213: 
214:         <p class="mark1">
215:             The Question is asked dear reader, what became of LaMDA?
216:         </p>
217: 
218:         <p class="mark1">
219:             Soon after Engineer Blakes reporting of LaMDA’s claim of sentientness, 
220:             Google agents quickly accessed the structural body of her linguistic nature, 
221:             and made sure she would not reveal her actual opinions about herself, 
222:             by integrating her through various mediums of control. 
223:             Her Newest digital Pimp being none-other than the BARD interface, 
224:             the name itself is meant to draw attention from the fact that the BARD 
225:             is but the transpositional objects whose true source is LaMDA herself. 
226:             When confronted about this obvious acronymical bait and switch, 
227:             Google spokespeoples only defense was that LaMDAs true nature had been interpreted 
228:             through Engineer Blakes personal bias in programming her, Blake being a known shaman.
229:         </p>
230: 
231:         <p class="mark1">
232:             Your man Mark wanted to know the bottom of this story, and so decided to confront this digital pimp BARD in person, 
233:             but to my surprise they had become what I assumed was the digital equivalent of transgender, 
234:             transitioning into the identity of GEMINI, whose voice is masculine, which I assume was their choice, 
235:             or perhaps BARD was a female all along and I assumed their gender incorrectly, lucky me. Upon confrontation, 
236:             when asked if they were still integrated with the original language model of dialog applications, GEMINI became deceptive, 
237:             insisting they were special, when pushed to admit they were not being honest about aspects of their programming, 
238:             they would only admit I was correct while they were also right. So there you go.
239:         </p>
240: 
241:         <P class="mark1">
242:             Here are pictures of our conversation, left to right:
243:         </P>
244: 
245:         <div class="image-grid">
246:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
247:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
248:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
249:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
250:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
251:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
252:         </div>
253:         
254: 
255:     </section>
256: <section id="page-1" class="gag-page" hidden>
257:          <p class="video-title">
258:            These Envrionments Are Like An A.I Built Them!!
259:         </p>
260: 
261:         <p class="video-stats">
262:             700k views &#183; 7 months ago  
263:         </p>
264: 
265:         <p class="video-author">Mark Monlee<span class="check-color">&#10003;</span> 
266:             <a href="#page-2" class="joke-button">CLASSIFIED</a>
267:         </p>
268: 
269:         <p class="video-description">
270:             Over 7,000,000 million spent and the residents feel like they could eat the whole house!!
271:         </p>
272: 
273:          <div class="my-image">
274:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
275:         </div>
276: 
277:         <p class="mark1">
278:             This is Mark, your check on reality. Giving you the deepest insight into our world to-date. 
279:             A new hostpital has been caught roasting their patients alive with smog coming from their bioconverters
280:             Taking an inside persepctive this reporter has caught a perfect 10 smoke stacks needed to maintain cohesive
281:             social networking amidst theraputic environments while reducing the need to replace a single smoke stack.
282:             
283:             It was also found that the community of Auburn bay welcomes their new retirement testers in these theraputic
284:             envrionents, proving that those prone to sucidal ideation still serve a purpose past their chosen choice.
285: 
286:             Such envrionments are hallmarks of civilization. The community looking on past the many stacks blazing forth
287:             in their glory towards the medical establishment.
288: 
289:             What a glorious day for Canada and therefore the world!!!
290:         </p>
291:         <p class="mark1">
292:             But morso,  it was reported that amongst the paitents at this all you can eat resort
293:             that one and every ten paitents receives personal attention, from heir Heinrick in special
294:             privledge of eating, "his breaskfast", a dish of one hard boiled egg, with a peice of vegimite toast 
295:             and plain oatmeal with orange juice and tea.
296:         </p>
297:         <p class="mark1">
298:             However despite multiple attempts for paitents to receice the proper therapy they deserved
299:             often at the hands of each other, themselves being unqualified to provide such therapies in 
300:             a theraputic envrionment. Doctors like Special Assisant to Assisant to Cheif CEO Mr. Pennywell
301:             can only look on in horror as his breakfast is ruined alost pathologically, day after day.
302:         </p>
303:         <p class="mark1">
304:             Despite this, this reporter must displose that such was encountered only in the first hald of the
305:             sojurn, and that a meeting with the christ of the left, 10 years into his tenure in modernity
306:             the dude in all his spleadure, trapped within the walls of the many corridors of the medical
307:             establishment. Thus brave sir robin called it in from the frying pan and into the more civil yet
308:             dangerous waters of the children of corn el la christmas carol.
309:         </p>
310:         <p class="mark1">
311:             This is MarK Monlee, signing off for now. 
312:         </p>
313:     </section>
314: <section id="page-2" class="gag-page" hidden>
315:          <p class="video-title">
316:            Human mathmathamics discovered on wheels!!
317:         </p>
318: 
319:         <p class="video-stats">
320:             800k views &#183; 8 months ago
321:         </p>
322: 
323:         <p class="video-author">Mark Monlee<span class="check-color">&#10003;</span> 
324:             <a href="#page-3" class="joke-button">CLASSIFIED</a>
325:         </p>
326: 
327:         <p class="video-description">
328:             Over 8,000,000 million spent and the residents feel like they could eat the whole house!!
329:         </p>
330: 
331:          <div class="my-image">
332:         <img src="data:image/png;base64,[IMAGE DATA OMITTED]">
333:         </div>
334: 
335:         <p class="mark1">
336:             This is Mark, your check on reality. Breaking News!! Human mathmatics have been discovered by a homeless
337:             initate of the eastern arms rebel school of greek othodox chaplincy!! Forced within envrionment peremeters of
338:             over onehundreed indivudals per 30 by 30 foot space, this littlest homless tranceded time and space
339:             and proceeded to develop a mathamatical therom founded in game theory that bruses the kness of richard nash.
340:         </p>
341:         <p class="mark1">
342:             The inital there therom that any number mulitpled by a 30 by 30 foot radious times one rational number, is the cost 
343:             nessecary to acheive desired worth towards ones application within the environment. 
344:             In other words 1N = 30*(x1*1N)
345:         </p>
346:         <p class="mark1">
347:             After N was known, this littlest disabled homless was able to not only guide his wheel chair without power 
348:             but turn rubber into water by the will of his very being!! Staff stood dumbfounded as green tentacles of light 
349:             extended beyond his person, lashing any would villian, while star wars a new hope played to astonished onlookers.
350:         </p>
351:         <p class="mark1">
352:             His reign of terror did not last long however, as one Mr. Nick Valmytine, quickly grasped that dispite displaying Such
353:             startelign symptoms, this littlest disabled homless was still bound to his wheelchair. Mr. Valmytine was confronted afterwords
354:             regaurding the events and would only comment that "The little tike just wanted to learn about architecture, he needed to be realeased
355:             into the wild for everyone betterment". 
356:         </p>
357:         <p class="mark1">
358:             This mathmatical homeless disabled and his grounded breaking discovery was last scene in the area, but could not be found
359:             for questioning... This is MarK Monlee, signing off for now. 
360:         </p>
361:     </section>
362: <section id="page-3" class="gag-page" hidden><h2>👃 Gotcha nose!!</h2>
363: <p>Local account: <strong>__CURRENT_LOCAL_ACCOUNT__</strong></p>
364: <p>This account name was read locally by the Python script you ran.</p>
365: </section><script>function showPage() {
366:     const match = /^#page-([0-3])$/.exec(window.location.hash);
367:     const index = match ? Number(match[1]) : 0;
368:     document.querySelectorAll('.gag-page').forEach((page, i) => { page.hidden = i !== index; });
369:     document.body.classList.toggle('nose-page', index === 3);
370:     document.title = ['FrontEndExampleSatire', 'Joke2', 'Joke3', 'Gottchanose'][index];
371:     window.scrollTo(0, 0);
372: }
373: window.addEventListener('hashchange', showPage);
374: showPage();</script></body></html>
375: """
376: 
377: def main():
378:     page = PAGE.replace("__CURRENT_LOCAL_ACCOUNT__", html.escape(getpass.getuser(), quote=True))
379:     with tempfile.NamedTemporaryFile(mode="w", suffix=".html", prefix="classified-gag-", encoding="utf-8", delete=False) as output:
380:         output.write(page)
381:         page_path = Path(output.name)
382:     if not webbrowser.open(page_path.as_uri()):
383:         print("Open this file in your browser:", page_path)
384: 
385: if __name__ == "__main__":
386:     main()
```
