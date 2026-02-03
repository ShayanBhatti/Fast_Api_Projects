import json
from pathlib import Path

FILE_PATH = Path("./data/tasks.json")


def load_tasks():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4, default=str)
