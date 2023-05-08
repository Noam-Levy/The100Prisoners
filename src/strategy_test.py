import pytest
from strategy import *

class TestStrategy:
    @pytest.mark.parametrize("strategy, success_rate, tolerance", [
        (GuessRandomly(), 0.0, 0.01),
        (GuessOptimized(), 0.31, 0.025),
    ])
    def test_success_rate(self, strategy, success_rate, tolerance):
        successes = 0
        for _ in range(10000):
            success, _, _ = strategy.execute(100)
            if success: successes += 1
        calc_success_rate = successes / 10000
        assert calc_success_rate == pytest.approx(success_rate, abs=tolerance)

    @pytest.mark.parametrize("strategy", [
        GuessRandomly(),
        GuessOptimized(),
    ])
    def test_no_prisoner_guesses_more_than_half(self, strategy):
        _, _, visited_list = strategy.execute(100)
        max_guesses = max([len(guess) for guess in visited_list.values()])
        assert max_guesses <= 50

    @pytest.mark.parametrize("strategy", [
        GuessRandomly(),
        GuessOptimized(),
    ])
    def test_no_prisoner_continues_guessing_after_finding_number(self, strategy):
        _, _, visited_list = strategy.execute(100)
        for prisoner_number, guesses in visited_list.items():
            if prisoner_number in guesses:
                assert guesses[-1] == prisoner_number
                
