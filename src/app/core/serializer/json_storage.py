from pathlib import Path
import json


class JsonStorage:

    def __init__(self, path: Path):
        self.path = path

    def save(self, data: dict):
        with open(self.path, "w") as fd:
            json.dump(data, fd, indent=4)

    def load(self) -> dict:
        with open(self.path, "r") as fd:
            return json.load(fd)