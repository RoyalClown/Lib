class FileSave:
    def __init__(self, contents):
        self.contents = contents

    def txt_save(self, path='./test.txt'):
        with open(path, 'w') as f:
            f.write(self.contents)


if __name__ == "__main__":
    filesave = FileSave('yerw')
    filesave.txt_save()
