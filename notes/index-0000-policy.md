# Index 0000 Policy

B32K index 0 is reserved by design.

The canonical generated alphabet occupies indices 1 through 32767. Index 0 is intentionally withheld from ordinary symbolic payloads to avoid ambiguity between a real symbol and a null, empty, missing, framing, or control condition.

## Rule

- index 0 is reserved
- index 0 is not an ordinary alphabet symbol
- index 0 MUST NOT be emitted as normal symbolic data
- index 0 MAY be assigned a null, control, or framing role only by an explicit profile
- tools SHOULD treat index 0 as out-of-band unless a profile explicitly enables it

## Rationale

A trusted symbolic surface needs a clean way to distinguish ordinary symbol identity from absence, boundary, framing, or profile-level control.

If index 0 were emitted as an ordinary symbol, then absence and symbolhood could become confused.

The nonzero alphabet avoids that confusion:

- 0 = reserved / out-of-band / profile-controlled
- 1..32767 = canonical alphabet symbols

This preserves the full 15-bit space while keeping the ordinary alphabet unambiguous.
