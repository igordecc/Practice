"""
rename all files to condition python names
# module - small_characters.py
# directory/package - small_characters
# more about naming:
# https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
"""
import os
import sys

class Renamer():
    def __init__(self, start_directory, ignore_files=[]):
        # silent initialisation
        self.start_directory = start_directory
        self.ignore_files = [".git", ".idea", ".gitignore", "README", "LICENCE"]
        for file in ignore_files:
            self.ignore_files.append(file)

    def status(self):
        print("start directory", self.start_directory)
        print("ignorefiles", self.ignore_files)

    def main_init(self):
        print("file renamer is running")
        self.start_directory = input("enter absolute start path: ")

    def print(self):
        for root, dirs, files in os.walk(self.start_directory):
            ckechlist = root.split("\\")
            if self.check_dir(ckechlist)=="continue":    # skipp all ignored files
                continue
            print(root, dirs, files)

    def check_dir(self, checklist):
        s = "ok"
        for file in self.ignore_files:
            if file in checklist:
                s = "continue"  # don't visit "ignore_files" in dirs
        return s

    def __call__(self, *args, **kwargs):
        def find_files():
            files_to_rename = []
            for root, dirs, files in os.walk(self.start_directory):
                checklist = root.split("\\")
                filename = checklist[-1]
                if (self.check_dir(checklist) == "continue") or filename.isupper():     # skipp all ignored files and CAPSLOG files
                    continue
                files_to_rename.append(root)
            return files_to_rename
        files_to_rename = find_files()
        # print(files_to_rename)

        imax = len(files_to_rename)
        i = 0
        while i< imax:
            file = files_to_rename[i]
            filename = file.split("\\")[-1]
            newfilename = ""
            previous_char = ""
            for char in filename:
                char = self.statemachine(previous_char, char)
                previous_char = char
                newfilename += char

            dst = "\\".join(file.split("\\")[:-1]) + "\\" + newfilename  # create new_directory with new_filename in it

            # print("FILE ", file)
            # print("DST ", dst)

            try:
                os.rename(file, dst)  # rename the file
            except:
                os.execv(__file__, sys.argv)
                quit()

            # rename all occurrences in files_to_renames
            old_file = file

            files_to_rename = [_file.replace(old_file, dst) if old_file in _file else _file for _file in files_to_rename] # find and repl
            i += 1


    def statemachine(self, previous_char:str, char:str):
        if previous_char.islower() and char.isupper():
            return "_" + char.lower()
        elif char.isupper():
            return char.lower()
        elif char == " ":
            return "_"
        return char



if __name__ == '__main__':
    print("file renamer is running")
    start_directory = r"D:\work\ssupractice"
    renamer = Renamer(start_directory)
    renamer()
    renamer.status()
