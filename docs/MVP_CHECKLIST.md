# MVP development checklist

Only scaffolding is complete. Implement later steps in small, reviewable changes.

## 1. Repository setup

- [x] Document rules, package boundaries, and exclusions.
- [x] Add packaging, `src/` layout, and development dependencies.
- [x] Preserve MIT license and ignore private data and generated files.
- [x] Provide synthetic examples with regeneration instructions.
- [ ] Confirm distribution and import names before publishing.

## 2. Spreadsheet reading and validation

- [ ] Define public input/result types and required headers/optional cell values.
- [ ] Read one sheet with `openpyxl`; validate headers before processing rows.
- [ ] Track row numbers and reasons for skipped/invalid rows.
- [ ] Parse prices as `Decimal`; define rounding and reject values outside target field limits.
- [ ] Skip zero-price rows and promotions; reject negative/invalid prices.
- [ ] Detect duplicate codes after trimming and ignoring capitalization.
- [ ] Preserve promotion text and line breaks; represent empty text as a clear operation.

## 3. Conservative matching

- [ ] Accept product records independently of Django models.
- [ ] Match complete codes in names, preserving punctuation and suffixes.
- [ ] Test boundaries against similar and longer model codes.
- [ ] Check brands when both are present; review conflicts and multiple candidates.
- [ ] Report unmatched/uncertain rows without automatically selecting products.
- [ ] Validate against development catalog data before making accuracy claims.

## 4. Structured preview

- [ ] Return proposed updates plus skipped/error/review results and reasons.
- [ ] Include current/proposed prices, promotions, and visibility.
- [ ] Clearly label price replacement and promotion removal.
- [ ] Ensure the package performs no database writes.

## 5. Tests and CI

- [ ] Add behavioral tests described in `tests/README.md`.
- [ ] Check wheel and source-distribution installation in clean environments.
- [ ] Add CI for supported Python versions once executable behavior exists.
- [ ] Keep fixtures synthetic and examples reproducible.

## 6. Website integration (separate website repository)

- [ ] Add `is_price_visible=False` and `store_promotion=""` through migrations.
- [ ] Build staff-only upload, preview, confirmation, and results in Vietnamese.
- [ ] Fetch catalog data and call the package.
- [ ] Store reviewed changes server-side and reject stale confirmations.
- [ ] Apply approved updates in a database transaction.
- [ ] Update storefront price visibility and promotion display.
- [ ] Check discount badges and sorting when prices are hidden.

## 7. Development validation and release

- [ ] Validate the full workflow on development data with staff review.
- [ ] Confirm zero-price rows and unapproved products remain unchanged.
- [ ] Verify empty promotions clear previous text and approved prices become visible.
- [ ] Document API usage, supported inputs, limitations, and original contributions.
- [ ] Review naming, license, private-data exclusions, and AI disclosure.
- [ ] Prepare v0.1.0 artifacts; publishing requires a separate explicit action.
