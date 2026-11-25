"""
아래 명세를 만족하는 함수의 단위 테스트를 pytest로 작성해 주세요.
정상 · 예외 · 경계값을 모두 포함해 주세요.
"""

import pytest

from ai_B import parse_grade_csv


def test_parses_valid_csv_into_name_score_pairs():
	csv_text = "name,score\nAlice,85\nBob,92"

	assert parse_grade_csv(csv_text) == [("Alice", 85), ("Bob", 92)]


def test_accepts_zero_and_one_hundred_as_boundary_scores():
	csv_text = "name,score\nZero,0\nPerfect,100"

	assert parse_grade_csv(csv_text) == [("Zero", 0), ("Perfect", 100)]


def test_parses_quoted_name_containing_comma():
	csv_text = 'name,score\n"Doe, Jane",88'

	assert parse_grade_csv(csv_text) == [("Doe, Jane", 88)]


def test_keeps_rows_with_duplicate_names():
	csv_text = "name,score\nAlex,70\nAlex,95"

	assert parse_grade_csv(csv_text) == [("Alex", 70), ("Alex", 95)]


@pytest.mark.parametrize("score", ["101", ""])
def test_rejects_score_over_one_hundred_or_missing(score):
	with pytest.raises(ValueError):
		parse_grade_csv(f"name,score\nStudent,{score}")


def test_rejects_malformed_row():
	with pytest.raises(ValueError):
		parse_grade_csv("name,score\nStudent")
