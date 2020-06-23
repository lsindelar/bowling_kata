from unittest import TestCase, main
from bowling import BowlingGame


class TestGame(TestCase):
    """
        Test suite for BowlingGame class
    """
    
    def test_score_only_strikes(self):
        """
            Example Test 1: Test strikes.
        """
        print("Example Test 1: Test strikes.")
        test_game = BowlingGame("X X X X X X X X X X X X")
        self.assertEqual(test_game.score(), 300)

    def test_score_following_misses(self):
        """
            Example Test 2: Test nines.
        """
        print("Example Test 2: Test nines.")
        test_game = BowlingGame("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
        self.assertEqual(test_game.score(), 90)

    def test_score_only_splits(self):
        """
            Example Test 3: Test splits.
        """
        print("Example Test 3: Test spare.")
        test_game = BowlingGame("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5")
        self.assertEqual(test_game.score(), 150)

    def test_score_only_misses(self):
        """
            Own Test 1: Test only misses.
        """
        print("Own Test 1: Test only misses.")
        test_game = BowlingGame("- - - - - - - - - -")
        self.assertEqual(test_game.score(), 0)

    def test_score_mixed_cases(self):
        """
            Own Test 2: Test mixed cases, i.e. a mix of spares, strikes and misses.
        """
        print("Own Test 2: Test mixed cases, i.e. a mix of spares, strikes and misses.")
        # 0 + (10+10) + (10+0+0) + 0 + 7 + (10+6) + (10+10) + (10 + 0+0) + (10+0) = 93
        test_game = BowlingGame("- 2/ X - 52 4/ 6/ X - 8/ -")
        self.assertEqual(test_game.score(), 93)

    def test_score_no_special_cases(self):
        """
            Own Test 3: Test no special cases like strikes, spares, misses.
        """
        print("Own Test 3: Test no special cases like strikes, spares, misses.")
        # 10*3 = 30
        test_game = BowlingGame("12 12 12 12 12 12 12 12 12 12")
        self.assertEqual(test_game.score(), 30)

    def test_score_single_spare(self):
        """
            Own Test 4: Test a single spare.
        """
        print("Own Test 4: Test a single spare.")
        # (10 + 1) + 9*3 = 38
        test_game = BowlingGame("1/ 12 12 12 12 12 12 12 12 12")
        self.assertEqual(test_game.score(), 38)

    def test_score_single_strike(self):
        """
            Own Test 5: Test a single strike.
        """
        print("Own Test 5: Test a single strike.")
        # (10 + 3) + 9*3 = 40
        test_game = BowlingGame("X 12 12 12 12 12 12 12 12 12")
        self.assertEqual(test_game.score(), 40)

    def test_score_single_miss(self):
        """
            Own Test 6: Test a single miss.
        """
        print("Own Test 6: Test a single miss.")
        # 0 + 9*3 = 27
        test_game = BowlingGame("- 12 12 12 12 12 12 12 12 12")
        self.assertEqual(test_game.score(), 27)

    def test_score_preceding_misses(self):
        """
            Own Test 7: Test misses preceding hits.
        """
        print("Own Test 7: Test misses preceding hits.")
        # 10*2 = 20
        test_game = BowlingGame("-2 -2 -2 -2 -2 -2 -2 -2 -2 -2")
        self.assertEqual(test_game.score(), 20)

    def test_score_second_to_last_strike(self):
        """
            Own Test 8: Test with a strike second to last.
        """
        print("Own Test 8: Test with a strike second to last.")
        # 8*3 + 10 + 2*3 = 40
        test_game = BowlingGame("12 12 12 12 12 12 12 12 X 12")
        self.assertEqual(test_game.score(), 40)

    def test_score_output_type(self):
        """
            Own Test 9: Test output type.
        """
        test_game = BowlingGame("12 12 12 12 12 12 12 12 X 12")
        self.assertIsInstance(test_game.score(), int)


if __name__ == "__main__":
    main()
