# excel-product-updater

A Python package being developed to prepare product price and store promotion
updates from Excel for staff review, installable into an existing website project.

**Status: scaffolding only.** Reading, validation, matching, previews, and website
integration are not implemented. There is no CLI or public importer API yet.
Version `0.0.0` identifies this scaffold, not an MVP release. Distribution name
`excel-product-updater` and import name `excel_product_updater` are provisional.
PyPI availability could not be verified; check naming before publishing.

## Development setup

Requires Python 3.10 or newer. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -c "import excel_product_updater; print(excel_product_updater.__doc__)"
python -m build
```

On Windows activate with `.venv\Scripts\activate`. Editable installation uses
the source directly. `openpyxl` is declared for the planned reader; `build` and
`pytest` are development dependencies. Django is not required by the core package.
The existing [MIT license](LICENSE) is retained.

## Planned import rules

- Read one `.xlsx` worksheet with columns `Mã hàng`, `Tên hàng`, `Thương hiệu`,
  `Giá bán`, and `Mô tả`. Validate required headers and report invalid rows with
  reasons. Exact optional-field handling remains to be defined.
- Use `Decimal` for prices. Process valid positive prices only. Skip zero-price
  rows entirely, including promotions. Report negative or invalid prices.
- Update existing products only; never create products. Products absent from
  the sheet or without a confirmed match stay unchanged.
- For approved matches, **replace the existing price** with `Giá bán`, make it
  visible, and replace the store promotion with `Mô tả`.
- Preserve promotion text and line breaks. Empty `Mô tả` clears the previous
  promotion. Do not calculate discounts or subtract promotion amounts from prices.
- Require preview and staff confirmation before database updates. Clearly show
  price replacement and promotion removals in the preview.

Match the complete spreadsheet product code in website product names as the
strongest signal. Ignore capitalization and surrounding whitespace; preserve
meaningful punctuation and model suffixes initially. Avoid partial matches inside
longer codes. Check brand agreement when both records have a brand. One clear match
may become a proposal; multiple candidates or brand conflicts require review.
Never automatically choose uncertain matches. Full-name equality is unnecessary.
Matching has not been validated and no match rate is claimed.

## Package and website boundaries

The reusable package will read Excel with `openpyxl`, validate rows, accept website
product records, match them, and return structured proposals, skips, and errors.
**It will never write directly to the store database.**

The separate website integration will fetch catalog data and provide staff-only
Django Admin upload, preview, confirmation, and results. It must keep reviewed
changes server-side, detect changes since preview, and apply approved updates in
a database transaction. Proposed website fields are `is_price_visible` (default
`False`) and `store_promotion` (default empty); neither is implemented here.

The initial target uses Django 4.2 / Django REST Framework and Next.js App Router.
Existing product fields include `id`, `name`, `brand`, `model_number`, `price`,
`description`, and `compare_price`. The reported price field is
`DecimalField(max_digits=12, decimal_places=2)`. Reported model numbers were empty,
which motivates matching codes in names. A global `SHOW_PRICES = false` currently
hides numeric prices: database updates alone will not make them visible. Website
work must address per-product visibility, promotions, discount badges, and sorting
when prices are hidden. These observations come from the project brief and have
not been independently inspected during setup.

Customer-facing and store-admin text should be Vietnamese. Code identifiers,
comments, and package documentation should be English.

## Layout and next steps

```text
pyproject.toml
src/excel_product_updater/__init__.py   # Package marker only
tests/README.md                        # Planned test coverage
examples/README.md                     # Synthetic fixture and expected outcomes
examples/generate_sample.py            # Recreates the example workbook
examples/sample_products.xlsx          # Synthetic data only
docs/MVP_CHECKLIST.md
CONTRIBUTING.md
LICENSE
```

The `src/` layout helps reveal packaging mistakes by requiring installation before
imports. Feature modules will be added when needed, without placeholder APIs.
See the [MVP checklist](docs/MVP_CHECKLIST.md), [examples](examples/README.md), and
[contribution guidance](CONTRIBUTING.md).

Never commit customer spreadsheets, catalog exports, databases, or credentials.
Workbooks are ignored by default; only the named synthetic example is allowed.
Out of scope: fuzzy matching, product creation, inventory updates, scheduled
imports, complex multi-sheet layouts, and multiple commerce-platform integrations.

AI assistance was used for initial scaffolding and documentation. Contributors
should disclose meaningful AI assistance and verify changes. A potential Open
Source Student Innovation Challenge 2027 submission is a future goal; solving
the store's real workflow is the immediate priority.
