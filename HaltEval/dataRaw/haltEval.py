import json
import pickle
import zlib
import base64
from pathlib import Path

# -------- Pfade --------
BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "halteval_prelim.jsonl"
OUT_DIR = BASE_DIR.parent / "data"

OUT_DIR.mkdir(exist_ok=True)

# -------- Decoder --------
def decode(enc_code: str) -> str:
    return json.loads(
        pickle.loads(
            zlib.decompress(
                base64.b64decode(enc_code.encode("utf-8"))
            )
        )
    )

# -------- Verarbeitung --------
with open(RAW_FILE, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        data = json.loads(line)

        code = decode(data["enc_code"])
        terminates = data["terminates"]  # True / False

        suffix = "_t" if terminates else "_f"

        filename = f"task_{i:04d}{suffix}.py"
        filepath = OUT_DIR / filename

        with open(filepath, "w", encoding="utf-8") as pyfile:
            pyfile.write(code)

        print(f"✓ geschrieben: {filename}")
