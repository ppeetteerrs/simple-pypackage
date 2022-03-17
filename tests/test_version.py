import simple_pypackage
import pytest


@pytest.fixture
def version():
    return simple_pypackage.__version__


def test_version(version: str):
    assert version is not None
