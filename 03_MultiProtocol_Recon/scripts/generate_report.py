# generate_report.py -> lit les CSV agrégés et produit un simple report HTML
import csv
from pathlib import Path
from datetime import datetime
import html

# BASE = dossier flipper_exports, calculé par rapport à ce fichier
BASE = (Path(__file__).parent / ".." / "flipper_exports").resolve()
OUT = BASE / "report.html"

def read_csv(p):
    if not p.exists():
        return []
    with p.open() as f:
        reader = csv.DictReader(f)
        return list(reader)

def table_html(rows, title):
    if not rows:
        return f"<h3>{html.escape(title)} - Aucun résultat</h3>"
    keys = rows[0].keys()
    header = "".join(f"<th>{html.escape(k)}</th>" for k in keys)
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f"<td>{html.escape(str(r.get(k,'')))}</td>" for k in keys) + "</tr>"
    return f"<h3>{html.escape(title)}</h3><table border='1' cellpadding='4'><thead><tr>{header}</tr></thead><tbody>{body}</tbody></table>"

def main():
    BASE.mkdir(parents=True, exist_ok=True)
    ble = read_csv(BASE / "ble_agg.csv")
    nfc = read_csv(BASE / "nfc_agg.csv")
    sub = read_csv(BASE / "subghz_agg.csv")

    html_content = f"""<html><head><meta charset='utf-8'><title>Multi-Protocol Recon Report</title>
    <style>body{{font-family:Arial;}} table{{border-collapse:collapse;}} th{{background:#eee;}}</style></head><body>
    <h1>Multi-Protocol Recon Report</h1>
    <p>Generated: {datetime.utcnow().isoformat()} UTC</p>
    {table_html(ble,"BLE Discoveries")}
    {table_html(nfc,"NFC Discoveries")}
    {table_html(sub,"Sub-GHz Metadata")}
    <h2>Summary</h2>
    <ul>
      <li>BLE entries: {len(ble)}</li>
      <li>NFC entries: {len(nfc)}</li>
      <li>Sub-GHz entries: {len(sub)}</li>
    </ul>
    <p>Usage éthique : voir ../docs/ethics.md</p>
    </body></html>"""

    OUT.write_text(html_content, encoding="utf-8")
    print("Report created ->", OUT)

if __name__ == "__main__":
    main()
