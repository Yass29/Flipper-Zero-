# 03 · Multi-Protocol Recon & Reporting

**Work in progress — exploring how to organize and report device-discovery metadata.**

## Current components

- `flipper_exports/ble_scan_example.csv`: example BLE records
- `scripts/create_ble_agg.py`: converts the example BLE CSV into a normalized `ble_agg.csv`
- `scripts/generate_report.py`: builds a simple HTML report from available aggregate CSVs
- `scripts/parse_subghz.py`: early CSV metadata parser (requires an example input that is not yet included)
- `flipper_exports/report.html`: an existing sample report
- `web/dashboard.html`: early dashboard scaffold

**Not yet implemented:** live scanning, automated Flipper Zero integration, and the currently empty NFC/BLE parsing placeholders. No claim of discovering live devices is made.

## Reproduce the sample report

From the repository root, with Python 3 installed:

```bash
python3 03_MultiProtocol_Recon/scripts/create_ble_agg.py
python3 03_MultiProtocol_Recon/scripts/generate_report.py
```

Then open `03_MultiProtocol_Recon/flipper_exports/report.html` in a browser.

The report reads existing CSV data only. Missing NFC and Sub-GHz aggregate files simply produce empty sections.

## Next improvements

- Normalize input formats and add sample NFC/Sub-GHz datasets
- Complete the placeholder parsers and write basic tests
- Improve the HTML report's layout and clarity
- Document data minimization and privacy considerations

## Ethics

Use only your own test data or data collected with permission. Device identifiers should be anonymized before publication.

[← Back to lab overview](../README.md)
