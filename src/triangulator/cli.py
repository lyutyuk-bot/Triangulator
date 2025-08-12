"""Simple CLI to run a triangulation on a JSON file.
Usage:
    python -m triangulator.cli data/example_case.json
"""
import json, sys
from .models import Claim, Evidence, Source
from .engine import TriangulationEngine

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m triangulator.cli <path-to-json>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    sources = {s["id"]: Source(**s) for s in payload["sources"]}
    claim = Claim(**payload["claim"])
    evidence = [Evidence(**e) for e in payload["evidence"]]
    eng = TriangulationEngine(sources)
    result = eng.evaluate(claim, evidence)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
