import unittest
from datetime import datetime

from parameterized import parameterized

from task import (
    BerlinTime,
    _convert_to_berlin_time,
    convert_to_berlin_time_rep,
    to_string
)


class TestConvertToBerlinClock(unittest.TestCase):

    @parameterized.expand(
        [
            ('00:00:00', BerlinTime()),
            ('00:00:01', BerlinTime(second_parity=1)),
            ('00:00:59', BerlinTime(second_parity=1)),
            ('00:01:00', BerlinTime(one_min=1)),
            ('23:59:59', BerlinTime(five_hour=4, one_hour=3, five_min=11, one_min=4, second_parity=1)),
            ('00:01:59', BerlinTime(one_min=1, second_parity=1)),
            ('00:35:59', BerlinTime(five_min=7, second_parity=1)),
            ('00:59:59', BerlinTime(five_min=11, one_min=4, second_parity=1)),
            ('12:00:59', BerlinTime(five_hour=2, one_hour=2, second_parity=1)),
            ('12:59:59', BerlinTime(five_hour=2, one_hour=2, five_min=11, one_min=4, second_parity=1)),
        ]
    )
    def test_convert_seconds(self, inp, output):
        dt = datetime.strptime(inp, "%H:%M:%S")
        self.assertEqual(_convert_to_berlin_time(dt), output)


class TestToString(unittest.TestCase):

    @parameterized.expand(
        [
            ('12:00:00', BerlinTime(five_hour=2, one_hour=2), 'O\nRROO\nRROO\nOOOOOOOOOOO\nOOOO'),
            ('06:06:01 ', BerlinTime(five_hour=1, one_hour=1, five_min=1, one_min=1, second_parity=1), 'Y\nROOO\nROOO\nYOOOOOOOOOO\nYOOO'),
        ]
    )
    def test_convert_berlin_time_to_string(self, name, inp, output):
        self.assertEqual(to_string(inp), output)
