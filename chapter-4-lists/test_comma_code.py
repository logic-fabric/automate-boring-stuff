from comma_code import comma_code


def test_with_empty_list():
    assert comma_code([]) == ""

def test_with_one_component():
    assert comma_code(["one component"]) == "one component"
    assert comma_code([True]) == "True"

def test_with_2_components():
    assert comma_code(["first", "second"]) == "first and second"

def test_with_3_components():
    assert comma_code(["first", "second", "third"]) == "first, second and third"
