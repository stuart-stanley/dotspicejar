from .nav_planner import NavigatorPlanner   # , NavigatorMove, NavigatorDrill
from braille import BrailleString
from configmgr import cfm


class BrailleStringPlanner(object):
    def __init__(self, planner, braille_string):
        assert isinstance(planner, NavigatorPlanner)
        assert isinstance(braille_string, BrailleString)
        self.__braille_string = braille_string
        self.__planner = planner
        self.__inter_dot_distance = cfm.braille.in_cell_dot_distance
        self.__inter_cell_hz_distance = cfm.braille.tween_cell_dot_hz_distance

    def plan(self):
        """
        just pull the trigger an do it.
        """
        mv_x = 0
        mv_y = 0
        for cell_inx in range(len(self.__braille_string)):
            cell = self.__braille_string[cell_inx]
            mv_x, mv_y = self.__process_cell(cell, cell_inx, mv_x, mv_y)

    def __process_cell(self, cell, cell_inx, mv_x, mv_y):
        for col_inx in range(0, 2):
            for row_inx in range(0, 3):
                if cell.raised(col_inx, row_inx):
                    description = 'cell {}({}), dot[{}][{}]'.format(
                        cell_inx, cell.key, col_inx, row_inx)
                    self.__planner.add_move(mv_x, mv_y, description)
                    self.__planner.add_drill(description)
                    # reset movements to 0.0, since we are "here"
                    mv_x = 0.0
                    mv_y = 0.0
                # progress "down"
                mv_y += self.__inter_dot_distance
            # End of the column. move "back up" 3 rows and over a column
            mv_y -= (self.__inter_dot_distance * 3)
            mv_x += self.__inter_dot_distance
        # and end of cell. 'y' (up/down) is already in the right place, but
        # 'x' is trickier, since we are two-cell-dot-distances over from the
        # left column. We need to subtract those two and then add back the
        # tween-cell X distance.
        mv_x -= (self.__inter_dot_distance * 2)
        mv_x += self.__inter_cell_hz_distance
        return mv_x, mv_y
