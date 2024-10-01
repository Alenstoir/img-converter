from tkinter import ttk, filedialog
import tkinter as tk

from converter.director import FileDirector


class ImageConverterWindow(tk.Tk):
    _input_directory = None
    _output_directory = None

    quit_button: tk.Button
    convert_button: tk.Button

    file_director: FileDirector

    def __init__(self):
        self.file_director = FileDirector()

        super().__init__()
        self.title("Image Converter")
        self.minsize(500, 120)
        self.update()

        self.mainframe = tk.Frame(self, relief=tk.RAISED, borderwidth=1, bg="#ababab")
        self.mainframe.pack_propagate(False)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        self.quit_button = tk.Button(self, text="Закрыть", command=self.destroy, state=tk.NORMAL)
        self.quit_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.convert_button = tk.Button(self, text="Сконвертировать", command=self.perform_convert, state=tk.DISABLED)
        self.convert_button.pack(side=tk.RIGHT)

        tk.Label(self, text="Выберите выходной формат: ").pack(side=tk.LEFT, padx=5, pady=5)
        supported_formats = ["----"] + list(self.file_director.formats_available().keys())
        self._chosen_format = tk.StringVar()
        self._chosen_format.set(supported_formats[0])
        self._chosen_format.trace("w", self.check_for_format)
        tk.OptionMenu(self, self._chosen_format, *supported_formats).pack(side=tk.LEFT)

        self.inputframe = tk.Frame(self.mainframe, width=150, height=150)
        self.inputframe.pack_propagate(False)
        self.outputframe = tk.Frame(self.mainframe, width=150)
        self.outputframe.pack_propagate(False)

        self.inputframe.pack(side="left", fill="both", expand=True)
        ttk.Separator(self.mainframe, orient=tk.VERTICAL).pack(side=tk.LEFT)
        self.outputframe.pack(side="left", fill="both", expand=True)

        labelframe = tk.Frame(self.inputframe)
        labelframe.pack_propagate(False)
        labelframe.pack(side=tk.TOP, fill="both", expand=True)
        ttk.Label(labelframe, text="Забрать из:").pack(side=tk.TOP, padx=5, pady=5)
        self._input_directory = tk.StringVar()
        tk.Label(labelframe, textvariable=self._input_directory, anchor=tk.E, wraplength=0).pack(fill=tk.BOTH, padx=5, expand=True)
        ttk.Button(self.inputframe, text="Выбрать директорию", command=self.select_input_dir).pack(side=tk.BOTTOM, fill=tk.BOTH)

        labelframe = tk.Frame(self.outputframe)
        labelframe.pack_propagate(False)
        labelframe.pack(side=tk.TOP, fill="both", expand=True)
        ttk.Label(labelframe, text="Сохранить в:").pack(side=tk.TOP, padx=5, pady=5)
        self._output_directory = tk.StringVar()
        ttk.Label(labelframe, textvariable=self._output_directory, anchor=tk.E, wraplength=0).pack(fill=tk.BOTH, padx=5, expand=True)
        ttk.Button(self.outputframe, text="Выбрать директорию", command=self.select_output_dir).pack(side=tk.BOTTOM, fill=tk.BOTH)

    def check_for_format(self, *_args):
        if not (not self._chosen_format.get() == "----" and self._input_directory.get() and self._output_directory.get()):
            self.convert_button.config(state=tk.DISABLED)
        else:
            self.convert_button.config(state=tk.NORMAL)

    def select_input_dir(self):
        dir_name = filedialog.askdirectory(initialdir="/")
        self._input_directory.set(dir_name)
        self.check_for_format()

    def select_output_dir(self):
        dir_name = filedialog.askdirectory(initialdir="/")
        self._output_directory.set(dir_name)
        self.check_for_format()

    def perform_convert(self):
        files = self.file_director.parse_directory_into_files(path=self._input_directory.get())
        self.file_director.save_files_through_converter(files=files, output_path=self._output_directory.get(), file_format=self._chosen_format.get())


def main():
    window = ImageConverterWindow()
    window.mainloop()


if __name__ == '__main__':
    main()
