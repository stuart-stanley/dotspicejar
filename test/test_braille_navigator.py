from navigator import NavigatorPlanner, BrailleStringPlanner
import pytest
import hack_config  # noqa: F401 -- we need this to hack-init our config for now


@pytest.fixture
def basil_g1str():
    """
    provides the grade-1 translated BrailleString of 'basil'
    """
    from braille import BrailleTranslator
    bbt = BrailleTranslator('basil')
    g1s = bbt.as_grade_1
    return g1s


@pytest.fixture
def planner():
    """
    provides a basic NavigatorPlanner for steps
    """
    return NavigatorPlanner(field="todo", home_x=0.0, home_y=0.0)


def test_basil_fixture_smells_nice(basil_g1str):
    assert basil_g1str.as_unicode == u'⠃⠁⠎⠊⠇'


def test_planner_fixture_ok(planner):
    assert not planner.locked


def test_basil_g1_loads(planner, basil_g1str):
    bsp = BrailleStringPlanner(planner, basil_g1str)
    assert bsp is not None


def test_basil_g1_plans(planner, basil_g1str):
    bsp = BrailleStringPlanner(planner, basil_g1str)
    bsp.plan()


def test_basil_g1_code(planner, basil_g1str):
    bsp = BrailleStringPlanner(planner, basil_g1str)
    bsp.plan()
    c = planner.for_now_emit()
    for l in c:
        print(l)
    assert c is None, c
