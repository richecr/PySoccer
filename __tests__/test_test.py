import pytest


@pytest.fixture
def init():
    test = "TESTE"
    return test


class TestTest:
    def test_1(self, init):
        assert init == "TESTE"
