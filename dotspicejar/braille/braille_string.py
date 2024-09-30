

class BrailleString(object):
    def __init__(self, raw_string, cell_string):
        self.__raw_string = raw_string
        self.__cells = cell_string

    def __len__(self):
        return len(self.__cells)

    @property
    def as_unicode(self):
        r = u''
        for cell in self.__cells:
            r += cell.unicode
        return r

    @property
    def as_string(self):
        return self.__raw_string

    def __getitem__(self, index):
        return self.__cells[index]
