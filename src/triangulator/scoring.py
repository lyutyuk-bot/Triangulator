from typing import Dict, Iterable
from .models import Evidence

# Default evidence weights (sum to 1.0)
DEFAULT_WEIGHTS: Dict[str, float] = {
    "physical": 0.40,
    "contemporary": 0.30,
    "third_party": 0.20,
    "retrospective": 0.10,
    # These two map into the above classes for demo simplicity:
    "material": 0.40,       # treated like physical
    "environmental": 0.40,  # treated like physical
}

def normalize_type(t: str) -> str:
    if t in ("material", "environmental"):
        return "physical"
    return t

def confidence_score(evidence: Iterable[Evidence]) -> float:
    """Compute a 0..100 confidence that a claim is true.

    Approach:
    - For each evidence item, take weight by (type weight * strength)
    - Add for supports=True, subtract for supports=False
    - Clamp to [0, 1] and convert to percentage
    """
    pos = 0.0
    neg = 0.0
    for ev in evidence:
        w = DEFAULT_WEIGHTS.get(ev.type, 0.0) * max(0.0, min(1.0, ev.strength))
        if ev.supports:
            pos += w
        else:
            neg += w
    raw = pos - neg
    # Map from [-1..+1] to [0..1]
    norm = (raw + 1.0) / 2.0
    if norm < 0.0:
        norm = 0.0
    if norm > 1.0:
        norm = 1.0
    return round(norm * 100.0, 2)

def contradiction_flags(evidence: Iterable[Evidence]) -> bool:
    """Return True if there is significant contradiction across evidence types."""
    seen_support = set()
    seen_contra = set()
    for ev in evidence:
        t = normalize_type(ev.type)
        if ev.supports:
            seen_support.add(t)
        else:
            seen_contra.add(t)
    # Contradiction if both support and contra exist in 2+ distinct types
    return len(seen_support & seen_contra) >= 1 and (len(seen_support) + len(seen_contra)) >= 2
