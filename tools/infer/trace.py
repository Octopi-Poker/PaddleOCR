import json
from pathlib import Path
from typing import Optional

import cv2


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

    def trace_image(self, description: str, img):
        fname = PipelineTrace.instance.new_step_path(description, "png")
        cv2.imwrite(fname, img)

    def trace_data(self, description: str, data):
        fname = PipelineTrace.instance.new_step_path(description, "json")
        with open(fname, "w") as f:
            json.dump(data, f, default=lambda v: repr(v), indent=2)
