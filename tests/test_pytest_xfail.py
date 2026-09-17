import pytest

@pytest.mark.xfail(reason="Найден баг, тест падает")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Найден баг, тест падает")
def test_without_bug():
    ...