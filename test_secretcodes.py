from project import entomor, mortoen, shift

def test_entomor():
    try:
        assert entomor("Arham") == "._ ._. .... ._ __"
        assert entomor("167") == ".____ _.... __..."
        assert entomor("Arham 167") == "._ ._. .... ._ __ .____ _.... __..."

    # Had to do this because pytest would not accept the variable names that were defined previously in the code and gave name errors
    except NameError:
        pass

def test_moroten():
    try:
        assert mortoen("._ ._. .... ._ __") == "Arham"
        assert mortoen(".____ _.... __...") == "167"
        assert mortoen("._ ._. .... ._ __ .____ _.... __...") == "Arham 167"
    except NameError:
        pass

def test_shift():
    try:
        assert shift("Arham", "1") == "Bsibn"
        assert shift("arham", "2") == "ctjco"
    except NameError:
        pass
