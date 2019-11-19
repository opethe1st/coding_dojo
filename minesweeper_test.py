from minesweeper import solution


def test_minesweeper_1():
    input_ = '''
*...
....
.*..
.... '''
    expected_output = '''*100
2210
1*10
1110'''
    assert solution(input_) == expected_output


def test_minesweeper_2():
    input_ = '''
**...
.....
.*...'''
    expected_output = '''**100
33200
1*100'''
    assert solution(input_) == expected_output


def test_minesweeper_3():
    input_ = '''
*
.
.'''
    expected_output = '''*
1
0'''
    assert solution(input_) == expected_output
