from src.parsers.books import get_rating

def test_rating():
    tag = type("obj", (), {"get": lambda self, x: ["star-rating", "Three"]})
    assert get_rating(tag) == 3