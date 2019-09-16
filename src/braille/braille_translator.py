from .braille_cell import BrailleCell
from .braille_string import BrailleString


class BrailleTranslator(object):
    _simple_cells = None

    def __init__(self, text):
        self.__raw_text = text
        if BrailleTranslator._simple_cells is None:
            self.__setup_class_simple_cells()

    @property
    def as_grade_1(self):
        cell_list = []
        for c in self.__raw_text:
            cell = self._simple_cells[c]
            cell_list.append(cell)
        bs = BrailleString(cell_list)
        return bs

    def __setup_class_simple_cells(self):
        cd = {}
        cd['a'] = BrailleCell('a', '*..', '...')
        cd['b'] = BrailleCell('b', '**.', '...')
        cd['c'] = BrailleCell('c', '*..', '*..')
        cd['d'] = BrailleCell('d', '*..', '**.')
        cd['e'] = BrailleCell('e', '*..', '.*.')
        cd['f'] = BrailleCell('f', '**.', '*..')
        cd['g'] = BrailleCell('g', '**.', '**.')
        cd['h'] = BrailleCell('h', '**.', '.*.')
        cd['i'] = BrailleCell('i', '.*.', '*..')
        cd['j'] = BrailleCell('j', '.*.', '**.')
        cd['k'] = BrailleCell('k', '*.*', '...')
        cd['l'] = BrailleCell('l', '***', '...')
        cd['m'] = BrailleCell('m', '*.*', '*..')
        cd['n'] = BrailleCell('n', '*.*', '**.')
        cd['o'] = BrailleCell('o', '*.*', '.*.')
        cd['p'] = BrailleCell('p', '***', '*..')
        cd['q'] = BrailleCell('q', '***', '**.')
        cd['r'] = BrailleCell('r', '***', '.*.')
        cd['s'] = BrailleCell('s', '.**', '*..')
        cd['t'] = BrailleCell('t', '.**', '**.')
        cd['u'] = BrailleCell('u', '*.*', '..*')
        cd['v'] = BrailleCell('v', '***', '..*')
        cd['w'] = BrailleCell('w', '.*.', '***')
        cd['x'] = BrailleCell('x', '*.*', '*.*')
        cd['y'] = BrailleCell('y', '*.*', '***')
        cd['z'] = BrailleCell('z', '*.*', '.**')
        BrailleTranslator._simple_cells = cd
