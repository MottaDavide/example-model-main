from typing import Any
from pathlib import Path
import yaml


class YamlStorage:
    def __init__(self, path: Path):
        self.path = path

    def save(self, data: Any) -> None:
        with open(self.path, "w") as yaml_file:
            yaml.safe_dump(data, yaml_file)

    def load(self) -> Any:
        with open(self.path, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
        return data