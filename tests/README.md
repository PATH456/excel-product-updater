# Planned tests

No importer behavior exists yet, so no feature tests or placeholder passing tests
are included. `pytest` will report no tests collected until implementation begins.
For now, check the installed package import and build as described in the README.

Add tests alongside each feature, covering:

- Missing/duplicate headers, empty codes, duplicate normalized codes, and row reasons.
- Positive decimal prices, invalid/negative prices, field limits, and rounding.
- Zero-price rows skipping both prices and promotions.
- Case/whitespace normalization, preserved punctuation, and model suffixes.
- Complete-code boundaries, similar codes, multiple candidates, and brand conflicts.
- Unmatched products staying unchanged and no product creation.
- Promotion text/line breaks and empty text clearing a previous promotion.
- Current/proposed price replacement and visibility in structured previews.

Use synthetic fixtures. Tests here must not connect to a real store database.
Staff authorization, stale previews, transactions, and storefront display need
integration tests in the website repository.
