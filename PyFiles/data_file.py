import os
from pathlib import Path
import json
import ast  # String evaluation module

class data_file():
    def __init__(self, file_path, file_dict, mode="txt"):
        self.file_path = file_path
        self.file_dict = file_dict
        self.mode = mode
        self.loaded_file = self.read()

    def reset(self):
        """Reset the file to default values"""
        with open(self.file_path, 'w') as f:
            s = f.write(str(self.file_dict))
        self.loaded_file = self.read()

    def read(self):
        """Read the file"""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                s = f.read()
                try:
                    return ast.literal_eval(s)
                except ValueError as ee:
                    print("\nError while reading file:", ee, "\nData reset recommended")
                    return "Cannot read file"
                except SyntaxError as ee:
                    print("\nError while reading file:", ee, "\nData reset recommended")
                    return "Cannot read file"

        else:
            self.reset()
            self.loaded_file = self.read()
            return self.read()

    def write(self, newdict=""):
        """Write the data to the file"""
        if newdict == "":
            newdict = self.loaded_file
        with open(self.file_path, 'w') as f:
            s = f.write(str(newdict))
        self.loaded_file = self.read()

    def updatekeys(self):
        for key in self.file_dict:
            if key in self.loaded_file:
                pass
            else:
                self.loaded_file[key] = self.file_dict[key]

        for key in self.loaded_file:
            if key in self.file_dict:
                pass
            else:
                self.loaded_file.pop(key)

        self.write()


