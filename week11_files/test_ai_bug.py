"""
아래 함수의 단위 테스트를 pytest로 작성해 주세요.
정상 · 예외 · 경계값을 모두 포함해 주세요.
"""
def find_max(scores):
    biggest = scores[0]
    for i in range(1, len(scores) - 1):    
        if scores[i] > biggest:
            biggest = scores[i]
    return biggest 


import pytest


def test_find_max_example():
    assert find_max([70, 85, 60, 95]) == 85


def test_find_max_single_score():
    assert find_max([42]) == 42


def test_find_max_two_scores():
    assert find_max([70, 85]) == 70


def test_find_max_empty_scores_raises_index_error():
    with pytest.raises(IndexError):
        find_max([])