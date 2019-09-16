from braille import BrailleTranslator


def test_instantiate_translator():
    t = BrailleTranslator('basil')
    assert t is not None


def test_basil_grade_1_len():
    t = BrailleTranslator('basil')
    us1 = t.as_grade_1
    assert len(us1) == len('basil')


def test_basil_grade_1_unicode_string():
    t = BrailleTranslator('basil')
    us1 = t.as_grade_1
    uni = us1.as_unicode
    assert len(uni) == len('basil')
    assert uni == u'⠃⠁⠎⠊⠇'


def test_lowercase_alphabet_grade_1_unicode_string():
    t = BrailleTranslator('abcdefghijklmnopqrstuvwxyz')
    us1 = t.as_grade_1
    uni = us1.as_unicode
    assert uni == u'⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
