from lukaspackage.lib import try_me

def test_math():
    res = False
    if len(try_me()) > 0:
        res = True
    return res
