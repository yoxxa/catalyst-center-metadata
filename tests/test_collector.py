import os
from collector import BCSOICollector

def test_collector_construction(bcs_collector: BCSOICollector):
    assert isinstance(bcs_collector, BCSOICollector)
    