import os

from PIL import Image


class Converter:
    _openable_extensions = []
    _saveable_extensions = []
    _saveable_formats = []

    def __init__(self):
        Image.preinit()
        Image.init()
        extensions = Image.registered_extensions()
        self._openable_extensions = {ex for ex, f in extensions.items() if f in Image.OPEN}
        self._saveable_extensions = {ex for ex, f in extensions.items() if f in Image.SAVE}
        self._saveable_formats = Image.SAVE

    def openable_extensions(self):
        if self._openable_extensions:
            return self._openable_extensions
        raise RuntimeError("PIL not initialized or codec load error")

    def saveable_extensions(self):
        if self._saveable_extensions:
            return self._saveable_extensions
        raise RuntimeError("PIL not initialized or codec load error")

    def saveable_formats(self):
        if self._saveable_formats:
            return self._saveable_formats
        raise RuntimeError("PIL not initialized or codec load error")

    def save(self, image, filename, output_path, extension):
        file, ext = os.path.splitext(filename)
        image.save(os.path.join(output_path, file + "." + extension), extension)
