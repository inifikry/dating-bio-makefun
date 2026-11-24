"""Write the dating-app bio to /output/entry.txt."""

import os

OUTPUT_PATH = "/output/entry.txt"

BIO = (
    "I ghosted 4,000 matches this week, but I kept your profile open "
    "in a tab for six days straight. You're different. Probably."
)


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(BIO)


def main():
    write_entry()


if __name__ == "__main__":
    main()
