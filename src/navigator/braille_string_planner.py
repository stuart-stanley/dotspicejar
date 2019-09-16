from .nav_planner import NavigatorPlanner   # , NavigatorMove, NavigatorDrill
from braille import BrailleString


class BrailleStringPlanner(object):
    def __init__(self, planner, braille_string):
        assert isinstance(planner, NavigatorPlanner)
        assert isinstance(braille_string, BrailleString)
        self.__braille_string = braille_string
        self.__planner = planner
