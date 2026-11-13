# excel-product-updater

A project to help store staff prepare product price and promotion updates from
an Excel spreadsheet, review them, and approve them for the store website.

## Current status

We are starting with documentation only. There is no working importer and
nothing to install or run yet.

The goal is to learn by building one small piece at a time. Add a file or tool
when we need it, understand what it does, and document it here. All project
instructions and notes live in this README.

## Files in this project

- `README.md`: explains the project, decisions, and how to use it as it grows.
- `.gitignore`: tells Git which local files to leave out of commits, such as
  private spreadsheets, passwords, and generated Python files.
- `LICENSE`: contains the project's existing MIT license.

Git also keeps a hidden `.git/` directory for version history.

## What we want to build

1. Read a single worksheet from an Excel `.xlsx` file.
2. Check its columns and product rows, explaining any problems.
3. Find existing website products that match the spreadsheet products.
4. Show proposed price and promotion changes for staff review.
5. Let the website apply only the changes staff approve.

The first coding step will be a small Python script that opens a made-up
spreadsheet and prints its rows. We will explain the script and anything it
needs before adding more features.

## Planned spreadsheet rules

The spreadsheet uses these columns:

| Column | Meaning |
| --- | --- |
| `Mã hàng` | Product code |
| `Tên hàng` | Product name |
| `Thương hiệu` | Brand |
| `Giá bán` | Selling price |
| `Mô tả` | Store promotion text |

- Use valid positive prices. Skip zero-price rows completely, including their
  promotions. Report negative or invalid prices.
- Use Python's `Decimal` type for money when price handling is implemented.
- Update existing products only. Never create products from the spreadsheet.
- For approved matches, replace the price with `Giá bán`, make the price visible,
  and replace the store promotion with `Mô tả`.
- Preserve promotion wording and line breaks. An empty `Mô tả` clears the old
  promotion. Do not subtract promotion amounts from the selling price.
- Leave absent, unmatched, uncertain, and unapproved products unchanged.
- Show changes before saving, including promotion removals. Require staff approval.

Required fields, blank values, duplicate handling, price limits, and rounding
still need precise rules as we implement them.

## Planned product matching

Look for the complete spreadsheet product code in the website product name.
Ignore capitalization and surrounding whitespace, but preserve punctuation and
model suffixes. For example, `DEMO-FR100-A` must not match `DEMO-FR100-A2`.

Check brands when both sides provide one. Multiple candidates or conflicting
brands require review. Never automatically choose an uncertain match. Full
product names do not need to be identical. Matching has not been tested yet.

## Website integration, later

Keep Excel reading, validation, and matching separate from the website. That
Python code should return proposed changes and explanations without writing to
the store database. The website will handle staff access, uploads, previews,
confirmation, and saving.

Notes from the original project brief, not independently checked:

- The website uses Django 4.2, Django REST Framework, and Next.js App Router.
- Product fields include `id`, `name`, `brand`, `model_number`, `price`,
  `description`, and `compare_price`. Model numbers were reported as empty.
- The price field is `DecimalField(max_digits=12, decimal_places=2)`.
- A global `SHOW_PRICES = false` currently hides numeric prices. Updating the
  database alone will not make them visible.
- Proposed fields are `is_price_visible` (initially false) and `store_promotion`
  (initially empty). These have not been implemented.

The website will need to keep reviewed changes on the server, detect products
changed since preview, and save approved updates together in a database
transaction. Price visibility, promotion display, discount badges, and sorting
also need checking.

Customer-facing and staff-facing text should be Vietnamese. Code identifiers,
comments, and project documentation should be English.

## How we will check our work

Use made-up data. As behavior is added, check valid and invalid prices, missing
or duplicate columns and codes, similar product codes, brand conflicts,
unmatched products, and promotion changes. Add automated tests when there is
behavior to test. Website approval and database behavior need separate checks
in the website project.

Useful future examples include a positive price with a multiline promotion, a
positive price with an empty promotion, zero, a negative price, and a price
containing text. No examples or tests are implemented yet.

## Keeping the scope small

Start with one worksheet and one store workflow. Fuzzy matching, creating
products, inventory updates, scheduled imports, complex spreadsheets, and
supporting multiple store platforms are outside the initial scope.

Packaging, publishing, build tools, and automated checks can be introduced when
needed. If we later publish a Python package, confirm its name first and check
that it installs correctly.

Never commit customer spreadsheets, catalog exports, databases, or credentials.
Use `private_data/` for local private files; it is ignored by Git. Review changes
before committing. The ignore rules do not remove files already tracked by Git.
