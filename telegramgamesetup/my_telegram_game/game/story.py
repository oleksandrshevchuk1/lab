import json
import os

CHOICES_FILE = os.path.join("data", "choices.json")

with open(CHOICES_FILE, "r", encoding="utf-8") as f:
    STORY = json.load(f)

def get_node(node_id: str):
    return STORY.get(node_id)