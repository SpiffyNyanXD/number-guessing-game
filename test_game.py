from unittest.mock import patch
from game import choose_difficulty

def test_choose_difficulty_easy():
    with patch('game.get_integer') as mocked_get_integer:
        mocked_get_integer.return_value = 1
        result = choose_difficulty()
        assert result == (20, 7)

def test_choose_difficulty_medium():
    with patch('game.get_integer') as mocked_get_integer:
        mocked_get_integer.return_value = 2
        result = choose_difficulty()
        assert result == (50, 8)

def test_choose_difficulty_hard():
    with patch('game.get_integer') as mocked_get_integer:
        mocked_get_integer.return_value = 3
        result = choose_difficulty()
        assert result == (100, 10)
