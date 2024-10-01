import os
from typing import Type

from PIL import Image

from img_converter.converter.converter import Converter


class FileDirector:
    _converter: Converter

    def __init__(self, converter_class: Type[Converter] = Converter):
        self._converter = converter_class()

    def formats_available(self):
        return self._converter.saveable_formats()

    def parse_directory_into_files(self, path, recursive: bool = False, _rel_path: str = None):
        images = {}
        errors = []
        if recursive:
            raise NotImplemented

        base_dir, _recursive, filenames = list(os.walk(path))[0]
        for filename in filenames:
            file, ext = os.path.splitext(filename)
            if ext not in self._converter.openable_extensions():
                errors.append(f"FileDirector::_parse_directory_into_files::{filename} расширение не поддерживается для чтения")
                continue
            file_path = os.path.join(_rel_path, filename) if _rel_path else filename
            img = Image.open(os.path.join(base_dir, file_path)).convert("RGB")
            images[file_path] = img
        return images, errors

    def save_file_through_converter(self, output_path, files: dict, file_format: str):
        errors = []
        if file_format.upper() not in self._converter.saveable_formats():
            errors.append(f"FileDirector::_save_files_through_converter::{file_format} расширение не поддерживается для чтения")
        for filepath, file in files.items():
            self._converter.save(file, filepath, output_path, file_format)
        return errors
