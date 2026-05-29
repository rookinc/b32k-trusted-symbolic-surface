#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
profile_path = ROOT / "artifacts/json/surface_profile_000.json"
outdir = ROOT / "experiments/profile_000/prompts"
outdir.mkdir(parents=True, exist_ok=True)

profile = json.loads(profile_path.read_text())
symbols = profile["symbols"]
relations = profile["relations"]
claims = profile["claims"]
assertions = profile["assertions"]
questions = profile["test_questions"]

concept_text = "\n".join(
    f"- {s['name']}: {s['definition']}" for s in symbols
)

claim_text = "\n".join(
    f"- {c['name']}: {c['text']}" for c in claims
)

question_text = "\n".join(
    f"{i+1}. {q}" for i, q in enumerate(questions)
)

base_instruction = """You are evaluating a conceptual packet.
Preserve distinctions carefully.
Do not collapse adjacent concepts.
When uncertain, say what remains uncertain.
Answer the test questions at the end.
"""

prose_only = f"""{base_instruction}

CONCEPTUAL PACKET

{concept_text}

CLAIMS

{claim_text}

TEST QUESTIONS

{question_text}
"""

decorative = f"""{base_instruction}

CONCEPTUAL PACKET WITH DECORATIVE METADATA

Topic: LLM context design
Mode: exploratory analogy
Warning: This is not evidence about neural network internals.
Goal: preserve conceptual distinctions.

Concept labels:
{concept_text}

Claim labels:
{claim_text}

TEST QUESTIONS

{question_text}
"""

surface_symbols = "\n".join(
    f"{s['id']} index={s['index']} type={s['type']} name={s['name']} definition={s['definition']}"
    for s in symbols
)

surface_relations = "\n".join(
    f"{r['id']} index={r['index']} type={r['type']} name={r['name']} definition={r['definition']}"
    for r in relations
)

surface_claims = "\n".join(
    f"{c['id']} index={c['index']} type={c['type']} name={c['name']} text={c['text']} uses={','.join(c['uses'])}"
    for c in claims
)

surface_assertions = "\n".join(
    f"{a['subject']} -- {a['relation']} --> {a['object']}"
    for a in assertions
)

b32k_surface = f"""{base_instruction}

B32K TRUSTED SURFACE PROFILE

Profile: {profile['profile_id']}
Reserved index policy: index 0 is reserved and must not be used as ordinary symbolic data.

Read the prose definitions, but preserve the B32K identities exactly.
The B32K IDs are stable symbolic handles.
Do not merge two identities just because their prose sounds related.

SYMBOLS

{surface_symbols}

RELATIONS

{surface_relations}

CLAIMS

{surface_claims}

ASSERTIONS

{surface_assertions}

TEST QUESTIONS

{question_text}

When answering, refer to B32K IDs when they help preserve identity.
"""

files = {
    "profile_000_A_prose_only.txt": prose_only,
    "profile_000_B_decorative_metadata.txt": decorative,
    "profile_000_C_b32k_surface.txt": b32k_surface,
}

for name, text in files.items():
    path = outdir / name
    path.write_text(text)
    print(f"wrote {path}")

print("prompt variants generated")
