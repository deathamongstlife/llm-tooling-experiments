#!/usr/bin/env python3
def missing_items(text, required):
    lower = text.lower()
    return [item for item in required if item.lower() not in lower]

if __name__ == "__main__":
    sample = "Included: section A"
    required = ["section A", "section B"]
    print("Missing:", missing_items(sample, required))
