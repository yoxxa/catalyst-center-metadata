import pytest
from collector import BCSOICollector
import os

@pytest.fixture
def bcs_collector():
    yield BCSOICollector(
        os.getenv("BCS_OI_CLIENT_ID"),
        os.getenv("BCS_OI_CLIENT_SECRET"),
        os.getenv("BCS_OI_REGION")
    )