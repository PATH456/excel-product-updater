# Synthetic workbook

`sample_products.xlsx` contains invented products and prices, not a customer export.
Regenerate it after installing the package dependencies:

```bash
python examples/generate_sample.py
```

The generator writes only `examples/sample_products.xlsx`. Cell content is
reproducible; ZIP metadata may differ. This is a fixture generator, not an importer.

| Code | Price | Intended future outcome |
| --- | ---: | --- |
| DEMO-FR100-A | 10700000 | Eligible; preserve multiline promotion |
| DEMO-WM200-B | 5200000 | Eligible; empty promotion clears existing text |
| DEMO-TV300-C | 0 | Skip entirely, including promotion |
| DEMO-AC400-D | -100 | Report invalid price |
| DEMO-OV500-E | invalid | Report invalid price |

For a future matching exercise, use an invented website product named
`Tủ lạnh ExampleCool Inverter DEMO-FR100-A`, brand `ExampleCool`, with a current
price of `11000000.00`. The first row should eventually propose replacing that
price with `10700000.00`, making it visible, and replacing its promotion. A product
containing only `DEMO-FR100-A2` must not match `DEMO-FR100-A`.
These are expected behaviors, not verified importer output.
