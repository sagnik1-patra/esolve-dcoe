import json
import os

RULE_FILE = os.path.join(os.path.dirname(__file__), "rules.json")

def assign_team(days_past_due: int) -> str:
    with open(RULE_FILE) as f:
        rules = json.load(f)
    for rule in rules["rules"]:
        if rule["min"] <= days_past_due <= rule["max"]:
            return rule["team"]
    return "Call Center"
