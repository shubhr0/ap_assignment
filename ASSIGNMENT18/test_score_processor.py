import pytest
from score_processor import ScoreProcessor


def test_process_score_file_success(tmp_path):
    test_file = tmp_path / "score.txt"
    test_file.write_text("7")

    processor = ScoreProcessor()

    result = processor.process_score_file(str(test_file))

    assert result == 70


def test_process_score_file_missing_file():
    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")
