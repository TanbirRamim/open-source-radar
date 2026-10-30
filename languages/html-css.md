# HTML and CSS quickstart

How to structure a web page with HTML and style it with CSS. Follow the project's own `CONTRIBUTING.md` whenever it gives different instructions.

Open issues: [HTML issues](../issues/by-language/html.md) · [CSS issues](../issues/by-language/css.md)

## Setup

- For a plain static page, you only need a text editor and a browser. HTML and CSS do not need a build step by themselves.
- Create a project folder with `index.html` and `styles.css`. Link the stylesheet from the document's `<head>`:

  ```html
  <link rel="stylesheet" href="styles.css" />
  ```

- Start from a document structure with a doctype, a language on `<html>`, a character encoding, a viewport setting, and a page title. See [MDN's basic HTML syntax guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax).
- Put content and meaning in HTML; use CSS rules to control presentation. MDN's [CSS styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) explains selectors, declarations, and the cascade.

## Common commands

| Task | Usual command |
| --- | --- |
| Serve the current folder locally | `python3 -m http.server --bind 127.0.0.1 8000` |
| Check formatting with Prettier | `npx prettier --check index.html styles.css` |
| Format with Prettier | `npx prettier --write index.html styles.css` |

## Previewing changes

- For a small static page, open `index.html` in a browser. For a more reliable local origin, run the server command above from the project folder.
- Visit `http://127.0.0.1:8000/`. The server serves files from the current directory; stop it with `Ctrl+C`. See the [Python `http.server` documentation](https://docs.python.org/3/library/http.server.html).
- Refresh the page after edits. Use the browser's developer tools to inspect the DOM, computed styles, console errors, and different viewport sizes.
- If the project uses a framework or development server, use its documented command instead of starting a second server.

## Linting and formatting

- Follow the commands configured by the project first; check its `package.json`, task runner, and CI workflow.
- For a small standalone page, validate markup with the [Nu HTML Checker](https://validator.w3.org/nu/) and styles with the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- If the project uses Prettier, check or format only the files you changed with the commands above. See the [Prettier documentation](https://prettier.io/docs/).

## Tips

- Keep element names lowercase and nest elements correctly. Use semantic elements such as `<main>`, `<nav>`, and `<button>` for their intended purpose.
- A class such as `class="card"` is selected in CSS with `.card`. Check relative paths and filename capitalization if a stylesheet or image does not load.
- Test narrow and wide viewports. Prefer flexible layouts and avoid fixed widths that make content overflow on a phone.
- Check keyboard focus, text contrast, and form labels as well as how the page looks.
- Do not add a framework, package manager, or build step to a page that only needs plain HTML and CSS.

## Before you push

- [ ] The page loads without missing files or browser console errors.
- [ ] HTML and CSS validators report no unintended errors.
- [ ] The layout works at narrow and wide viewport sizes.
- [ ] The project's tests, formatter, and linter pass.
- [ ] The diff contains only the files needed for the change.

Back to [all languages](README.md) · [Guide](../guide/README.md)
