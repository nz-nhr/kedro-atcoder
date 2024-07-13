import pytest
import testbook
from pytest_lazyfixture import lazy_fixture
from src.kedro_atcoder.pipelines.APG4bPython.APG4bPython_cr.main import solve

def test_solve(in_out):
    in_list = in_out[0]
    out = in_out[1]
    assert solve(*in_list) == out 
