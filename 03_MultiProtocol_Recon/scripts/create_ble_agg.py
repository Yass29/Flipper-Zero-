import csv
from pathlib import Path

# Dossier flipper_exports basé sur l'emplacement du script
BASE = (Path(__file__).parent / ".." / "flipper_exports").resolve()
SRC  = BASE / "ble_scan_example.csv"
OUT  = BASE / "ble_agg.csv"

print("BASE =", BASE)
print("SRC  =", SRC)
print("OUT  =", OUT)

if not SRC.exists():
    print("ERREUR: Fichier source introuvable :", SRC)
else:
    rows = []
    with SRC.open() as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "collected_at": r.get("timestamp",""),
                "address": r.get("address",""),
                "name": r.get("name",""),
                "rssi": r.get("rssi","")
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["collected_at","address","name","rssi"])
        writer.writeheader()
        writer.writerows(rows)
    print("OK: Créé ->", OUT, "(", len(rows), "lignes )")
