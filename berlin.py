from dataclasses import dataclass
from datetime import datetime


def convert_to_berlin_time_rep(timestring):
    dt = datetime.strptime(timestring, "%H:%M:%S")
    clock = _convert_to_berlin_time(date=dt)
    return to_string(clock)


def _convert_to_berlin_time(time: datetime):
    return BerlinTime(
        five_hour=time.hour//5,
        one_hour=time.hour % 5,
        five_min=time.minute//5,
        one_min=time.minute % 5,
        second_parity=time.second % 2,
    )


@dataclass
class BerlinTime:
    five_hour: int = 0
    one_hour: int = 0
    five_min: int = 0
    one_min: int = 0
    second_parity: int = 0

    def __post_init__(self):
        check_assert_num_in_range(self.five_hour, 0, 4)
        check_assert_num_in_range(self.one_hour, 0, 4)
        check_assert_num_in_range(self.five_min, 0, 11)
        check_assert_num_in_range(self.one_min, 0, 4)
        check_assert_num_in_range(self.second_parity, 0, 1)


def to_string(berlin_time: BerlinTime):
    return '\n'.join([
        'Y' if berlin_time.second_parity else 'O',
        'R' * berlin_time.five_hour + 'O' * (4 - berlin_time.five_hour),
        'R' * berlin_time.one_hour + 'O' * (4 - berlin_time.one_hour),
        'Y' * berlin_time.five_min + 'O' * (11 - berlin_time.five_min),
        'Y' * berlin_time.one_min + 'O' * (4 - berlin_time.one_min),
    ])


def check_assert_num_in_range(num, start=0, end=0):
    if not(start <= num <= end):
        raise Exception(f'this {num} needs to be in this range: ({start}, {end})')
