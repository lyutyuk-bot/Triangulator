# Methodology

Triangulator resolves historical claims by **triangulating** at least three *independent* evidence streams.

## Evidence Weighting (default)
- Physical/archaeological data: 0.40
- Contemporary written records: 0.30
- Neutral/hostile third-party accounts: 0.20
- Retrospective narratives/chronicles: 0.10

We compute a **Confidence Index (0–100%)** via a weighted agreement function and expose contradictions as flags with rationale.

## Bias Mapping
Each source receives a bias profile (political, cultural, patronage, religious) and a *pressure score*. The UI overlays these as a semi-transparent layer.

## Revision Protocol
When new evidence arrives:
1. Create an entry in `CHANGELOG.md` (Added/Changed/Removed).
2. Re-run the triangulation for affected nodes.
3. Update the Confidence Index and attach notes in `docs/Revision-Notes/` (if substantial).
