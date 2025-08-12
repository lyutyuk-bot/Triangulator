from typing import Dict, List, Tuple
from .models import Claim, Evidence, Source
from .scoring import confidence_score, contradiction_flags

class TriangulationEngine:
    def __init__(self, sources: Dict[str, Source]):
        self.sources = sources

    def evaluate(self, claim: Claim, evidence: List[Evidence]) -> Dict[str, object]:
        # Filter evidence to only known sources
        ev = [e for e in evidence if e.source_id in self.sources]
        score = confidence_score(ev)
        contradictions = contradiction_flags(ev)
        # Minimal bias map (list biases present)
        biases = sorted({self.sources[e.source_id].bias for e in ev if self.sources[e.source_id].bias})
        # Node "agreement" heuristic: count distinct sources that support
        support_sources = {e.source_id for e in ev if e.supports}
        contra_sources = {e.source_id for e in ev if not e.supports}
        node_agreement = len(support_sources)
        node_contradiction = len(contra_sources)
        return {
            "claim_id": claim.id,
            "claim": claim.text,
            "confidence": score,
            "contradictions": contradictions,
            "biases": biases,
            "support_sources": sorted(list(support_sources)),
            "contra_sources": sorted(list(contra_sources)),
            "node_agreement": node_agreement,
            "node_contradiction": node_contradiction,
        }
