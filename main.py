import os

LINE = "Error: out of tokens mid-sentence. The model has left the chat and taken your half-finished thought with it."

LIMIT = 140
if len(LINE) != 108 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 108 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# The error message is the joke: it stops exactly where the money ran out.
