class Frame:
    """
        Frame class.
        Represents a single frame.
    """

    def __init__(self, rolls):
        """
            Initialises Frame.

            Parameters
            ----------
            rolls : :obj:`str`
                string of the rolls.
        """
        if len(rolls) == 1:
            self.first_roll = rolls
            if rolls is "-":
                self.second_roll = rolls
                self.len_rolls = 2
            else:
                self.second_roll = None
                self.len_rolls = 1
        else:
            self.first_roll = rolls[0]
            self.second_roll = rolls[1]
            self.len_rolls = 2

        self.isStrike = self.first_roll is "X"
        self.isSpare = self.second_roll is "/"

    @staticmethod
    def _score_roll(roll):
        """
            Calculates score for a single roll.

            Parameters
            ----------
            roll : :obj:`str`
                string of a valid roll.

            Returns
            -------
            int
                Score of roll.
        """

        if roll is "X":
            return 10

        if roll is "-" or roll is None:
            return 0

        return int(roll)

    def score_frame(self):
        """
            Calculates score for a single frame.

            Returns
            -------
            int
                Score of frame.
        """
        if self.len_rolls == 1:
            return self._score_roll(self.first_roll)

        if self.isSpare:
            return 10

        return self._score_roll(self.first_roll) + self._score_roll(self.second_roll)

    def score(self, next_frame, second_next_frame):
        """
            Calculates score for a single frame.

            Parameters
            ----------
            next_frame : :obj:`Frame`
                next frame object.

            second_next_frame : :obj:`Frame`
                second to next frame object.

            Returns
            -------
            int
                Score of frame.
        """

        # Score calculation
        if self.isStrike:

            # Score current frame + next two rolls
            if next_frame.len_rolls == 2:
                return self.score_frame() \
                        + next_frame.score_frame()
            else:
                return self.score_frame() \
                        + Frame._score_roll(next_frame.first_roll) \
                        + Frame._score_roll(second_next_frame.first_roll)

        # Length of current frame is 2
        if self.isSpare:
            # Score current frame + next roll

            return self.score_frame() + Frame._score_roll(next_frame.first_roll)

        return self.score_frame()


class BowlingGame:
    """
        BowlingGame class.
        Represents a bowling game defined by its frames.
    """

    def __init__(self, frames=None):
        """
            Initialises BowlingGame.

            Parameters
            ----------
            frames : :obj:`str`, optional
                string of valid frames.
        """

        self.frames = []
        for rolls in frames.split():
            self.frames.append(Frame(rolls))

    def optional_frame(self, index):

        if index < len(self.frames):
            return  self.frames[index]
        return None

    def score(self):
        """
            Calculates score for the game.

            Returns
            -------
            int
                Score of the game.
        """
        total_score = 0

        for i in range(10):
            current_frame = self.frames[i]
            next_frame = self.optional_frame(i + 1)
            second_next_frame = self.optional_frame(i + 2)

            total_score += current_frame.score(next_frame, second_next_frame)

        return total_score
