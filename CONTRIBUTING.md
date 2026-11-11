# Contributing

Follow the README's development setup and the MVP checklist. Keep changes small.
The current scope is scaffolding; importer functionality comes later.

Keep the package independent of Django models and database writes. Use English
for identifiers, comments, and documentation; future customer-facing and
store-admin messages should be Vietnamese.

For functional changes, add tests of observable behavior and failure cases, run
`python -m pytest`, and build with `python -m build`. Until tests exist, pytest's
"no tests collected" result is expected and does not verify features. Check built
artifacts install and import outside the repository root.

Use synthetic examples only. Do not commit customer workbooks, catalog exports,
secrets, or databases. Keep local private data in ignored `private_data/` and
review `git diff --staged` before committing.

Explain the problem, resulting behavior, and validation in pull requests. Disclose
meaningful AI assistance and review generated content. Initial scaffolding and
documentation were prepared with AI assistance; no importer logic was added.
