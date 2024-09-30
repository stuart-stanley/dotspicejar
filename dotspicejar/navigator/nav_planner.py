import logging
import gcody
log = logging.getLogger(__name__)


class NavigatorMove(object):
    def __init__(self, x_move_mm=0.0, y_move_mm=0.0, comment=None):
        self.x_move_mm = x_move_mm
        self.y_move_mm = y_move_mm
        if comment is None:
            comment = ''
        self.comment = comment


class NavigatorDrill(object):
    def __init__(self, comment=None):
        if comment is None:
            comment = ''
        self.comment = comment


class NavigatorPlanner(object):
    def __init__(self, field, home_x, home_y):
        self.__field = field
        self.__home_x = home_x
        self.__home_y = home_y
        self.__steps = []
        self.__move_speed = 6.75
        self.__down_drill_speed = 0.1
        self.__up_drill_speed = 1.0
        self.__locked = False

    @property
    def locked(self):
        return self.__locked

    def __check_locked(self):
        assert not self.__locked, \
            'attempting to modify once locked'

    def add_move(self, x_move_mm=0.0, y_move_mm=0.0, comment=None):
        log.info("  move added: x=%s, y=%s, comment='%s'", x_move_mm, y_move_mm, comment)
        self.__check_locked()
        step = NavigatorMove(x_move_mm, y_move_mm, comment=comment)
        self.__steps.append(step)

    def add_drill(self, comment=None):
        log.info("  drill added: comment='%s'", comment)
        self.__check_locked()
        step = NavigatorDrill(comment=comment)
        self.__steps.append(step)

    def for_now_emit(self):
        """
        temp method to continue making code without committing to ultimate paths
        """
        g = gcody.gcode()
        g.rel_move(com='Start of nav-planner dump, relative')
        g.move(-84, -30, -20, speed=self.__move_speed)
        for step in self.__steps:
            if isinstance(step, NavigatorMove):
                g.move(step.x_move_mm, step.y_move_mm, com=step.comment, speed=self.__move_speed)
            elif isinstance(step, NavigatorDrill):
                g.move(z=-2.0, speed=self.__down_drill_speed)
                g.move(z=2.0, speed=self.__up_drill_speed)
            else:
                assert False, "wtf"
        code = g.code
        return code
