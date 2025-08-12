from dataclasses import dataclass
from typing import List, Literal, Optional

EvidenceType = Literal["physical", "contemporary", "third_party", "material", "environmental", "retrospective"]

@dataclass
class Source:
    id: str
    name: str
    bias: Optional[str] = None  # e.g., "political", "cultural", "patronage", "religious"
    reliability: float = 0.5     # 0..1 subjective prior for source quality

@dataclass
class Evidence:
    source_id: str
    type: EvidenceType
    claim: str
    supports: bool = True        # True if it supports the claim, False if contradicts
    strength: float = 1.0        # 0..1 local strength (quality/clarity of this evidence)

@dataclass
class Claim:
    id: str
    text: str
    # Optional ground-truth (unknown in real life, used for tests/demo)
    truth_hint: Optional[bool] = None
    tags: Optional[List[str]] = None
