import copy


class BrailleCell(object):
    BRAILLE_UNICODE_BASE = 0x2800     # start of unicode braille patterns

    def __init__(self, key, dot_col_1, dot_col_2, description=None):
        self.__key = key
        assert len(dot_col_1) == 3, \
            "invalid column 1, incorrect length: ''".format(dot_col_1)
        assert len(dot_col_2) == 3, \
            "invalid column 2, incorrect length: ''".format(dot_col_2)
        self.__dots = [
            [False, False],
            [False, False],
            [False, False]
        ]
        left_bits = self.__build_row(0, dot_col_1, 1)
        right_bits = self.__build_row(1, dot_col_2, 8)
        ucode_value = chr(self.BRAILLE_UNICODE_BASE + right_bits + left_bits)

        self.__unicode = ucode_value
        if description is None:
            description = key
        self.__description = description

    @property
    def unicode(self):
        return self.__unicode

    @property
    def key(self):
        return self.__key

    def raised(self, over, down):
        return self.__dots[down][over]

    def __build_row(self, row_number, row_text, shift_base):
        bits = 0
        for cinx in range(3):
            bit = shift_base << cinx
            dot_char = row_text[cinx]
            if dot_char == '*':
                bits |= bit
                self.__dots[cinx][row_number] = True
            else:
                assert dot_char == '.', \
                    "invalid column {}, dot-chars must be . or * not '{}'".format(
                        row_number, dot_char)

        return bits
