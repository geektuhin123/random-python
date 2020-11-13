# This is a starting file
# task 1 - read a file and print

import os

class Reader:

    def __init__(self):
        pass

    def readFiles(self):
        current_location = os.getcwd()
        print("Reading file location", current_location)
        list_of_files = [file.name for file in os.scandir(current_location) if file.is_file() ]
        # print(list_of_files)
        textFileNames = (name for name in list_of_files if name.split('.')[1] == 'txt')
        list_of_texts = list(textFileNames)
        # print(list(list_of_texts))
        contents = []

        for file_name in list_of_texts:
            f = open(file_name, "r")
            contents.append(f.read())
            f.flush()
            f.close()
        self.contents = contents

    
    def get_contents(self):
        return self.contents



def main_method():    
    # test code

    obj_reader = Reader()
    obj_reader.readFiles()
    print(obj_reader.get_contents())


if __name__ == "__main__":
    main_method()