from name_fromating import get_formated_name
"""test of get_name_formatting"""
def test_first_last_name():
    formatted_name = get_formated_name('ahmed', 'ali')
    assert formatted_name == 'ahmed ali'.title()


def test_first_middle_last():
    formated_name = get_formated_name('ahmed', 'muhammed','ali' )
    assert formated_name == 'ahmed ali muhammed'.title()