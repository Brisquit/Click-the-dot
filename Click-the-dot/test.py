import unittest
from score import Score
from timer import Timer

class TestScore(unittest.TestCase):
    def test_initial_score(self):
        s = Score()
        self.assertEqual(s.score, 0)
        self.assertEqual(s.highscore >= 0, True)

    def test_scoring_increases(self):
        s = Score()
        old_high = s.highscore
        for _ in range(5):
            s.scoring()
        self.assertEqual(s.score, 5)
        if old_high < 5:
            self.assertEqual(s.highscore, 5)

class TestTimer(unittest.TestCase):
    def test_timer_reset(self):
        t = Timer()
        t.time_left = 5
        t.reset()
        self.assertEqual(t.time_left, 30)

    def test_timer_start(self):
        t = Timer()
        t.start()
        self.assertTrue(t.on)

if __name__ == '__main__':
    unittest.main()