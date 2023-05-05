from pathlib import Path
from typing import Optional


class PipelineTrace:
    output_dir: str
    file_name: str
    file_stem: str
    index: int = 0

    enabled: bool = False
    instance: Optional["PipelineTrace"] = None

    @classmethod
    def enable(cls):
        cls.enabled = True

    @classmethod
    def start(cls, *args, **kwargs):
        cls.instance = cls(*args, **kwargs)

    @classmethod
    def get(cls):
        return cls.instance

    def __init__(self, output_dir: str, file_name: str):
        self.output_dir = output_dir
        self.file_name = file_name
        self.file_stem = Path(file_name).stem

    def new_step_path(self, description: str, suffix):
        path = (
            Path(self.output_dir)
            / f"{self.file_stem}-{self.index}-{description}.{suffix}"
        )
        self.index += 1
        return str(path)
