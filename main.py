"""One-line AI excuse for breaking production.

Writes the excuse to /output/entry.txt (deterministic, stdlib only).
"""

import os

EXCUSE = "The tests passed locally, in the only universe where this code works, and I have decided to live there now."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(f"wrote /output/entry.txt ({len(EXCUSE)} characters)")

if __name__ == "__main__":
    main()
