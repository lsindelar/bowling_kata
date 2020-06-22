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

    def _score_frame(self, frame):
        """
            Calculates score for a single frame.

            Parameters
            ----------
            frame : :obj:`Frame`
                frame object.

            Returns
            -------
            int
                Score of frame.
        """
        if frame.len_rolls == 1:
            return self._score_roll(frame.first_roll)

        if frame.second_roll is "/":
            return 10

        return self._score_roll(frame.first_roll) + self._score_roll(frame.second_roll)

    def score(self):
        """
            Calculates score for the game.

            Returns
            -------
            int
                Score of the game.
        """
        total_score = 0
        num_rolls = len(self.frames)

        for i in range(10):
            # Frames
            current_frame = self.frames[i]

            next_frame = None
            if i + 1 < num_rolls:
                next_frame = self.frames[i + 1]

            second_next_frame = None
            if i + 2 < num_rolls:
                second_next_frame = self.frames[i + 2]

            # Score calculation
            if current_frame.first_roll is "X":
                # Score current frame + next two rolls

                if next_frame.len_rolls == 2:
                    score = self._score_frame(current_frame)\
                            + self._score_frame(next_frame)
                else:
                    score = self._score_frame(current_frame)\
                            + self._score_roll(next_frame.first_roll)\
                            + self._score_roll(second_next_frame.first_roll)

                total_score += score
                continue

            if current_frame.len_rolls == 1:
                score = self._score_frame(current_frame)
                total_score += score
                continue

            # Length of current frame is 2
            if current_frame.second_roll is "/":
                # Score current frame + next roll

                score = self._score_frame(current_frame) + self._score_roll(next_frame.first_roll)
                total_score += score
                continue

            total_score += self._score_frame(current_frame)

        return total_score
