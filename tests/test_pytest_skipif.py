import pytest

SYSTEM_VERSION = "1.2.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.3.0",
    reason="Тест не может быть запущен на 130"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "1.2.0",
reason="Тест не может быть запущен на 120"
)
def test_system_version_invalid():
    ...