# parse_subghz.py - parser metadata Sub-GHz (lecture-only, pas d'émission)
import csv
from pathlib import Path

SRC = Path("03_MultiProtocol_Recon/flipper_exports/subghz_example.csv")
OUT = Path("03_MultiProtocol_Recon/flipper_exports/subghz_agg.csv")

def parse():
    if not SRC.exists():
        print("Aucun fichier Sub-GHz d'exemple trouvé:", SRC)
        return
    rows = []
    with SRC.open() as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "collected_at": r.get("timestamp",""),
                "freq": r.get("frequency",""),
                "rssi": r.get("rssi",""),
                "note": r.get("note","")
            })
    write_header = not OUT.exists()
    with OUT.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["collected_at","freq","rssi","note"])
        if write_header:
            writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"Parsed {len(rows)} entries -> {OUT}")

if __name__ == "__main__":
    parse()
