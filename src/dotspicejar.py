from braille import BrailleTranslator
from navigator import NavigatorPlanner
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
log = logging.getLogger(__name__)


class DotSpiceJar(object):
    def __init__(self, text_string):
        self.__braille_translator = BrailleTranslator(text_string)
        self.__planner = NavigatorPlanner(None, 0.0, 0.0)
        self.__figure_braille_moves()
        print(self.__planner.for_now_emit())

    def __figure_braille_moves(self):
        grade1_str = self.__braille_translator.as_grade_1
        log.info("Translating '{}' to movements".format(grade1_str.as_unicode))


if __name__ == '__main__':
    x = DotSpiceJar("basil")
    print(x)
