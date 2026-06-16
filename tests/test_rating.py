from scraper import get_rating


def test_one_star():
    tag = {"class": ["star-rating", "One"]}
    assert get_rating(tag) == 1


def test_three_stars():
    tag = {"class": ["star-rating", "Three"]}
    assert get_rating(tag) == 3


def test_five_stars():
    tag = {"class": ["star-rating", "Five"]}
    assert get_rating(tag) == 5