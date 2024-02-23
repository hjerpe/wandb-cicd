import random


def test_random_number():
    random.seed(1)
    assert random.randint(1, 100) == 18