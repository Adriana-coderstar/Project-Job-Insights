from src.counter import count_ocurrences


def test_counter():
    total_python_words = count_ocurrences("src/jobs.csv", "python")
    assert total_python_words == 1639

    total_javascript_words = count_ocurrences("src/jobs.csv", "javascript")
    assert total_javascript_words == 122
