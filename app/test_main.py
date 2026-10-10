from app.main import get_human_age


def test_human_age_ist_a_list() -> None:
    assert isinstance(get_human_age(24, 24), list)


def test_human_age_list_length_is_2() -> None:
    assert len(get_human_age(24, 24)) == 2


def test_human_age_if_age_animals_lover_then_15() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_human_age_if_age_animals_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_human_age_if_age_animals_greater_then_15() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
