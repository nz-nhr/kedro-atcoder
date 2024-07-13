import pytest
from pathlib import Path

test_path = Path('/home/komikado/project/kedro-atcoder/src/kedro_atcoder/pipelines/APG4bPython/APG4bPython_cr/test')

@pytest.fixture(params=[('sample-1.in','sample-1.out'), ('sample-2.in','sample-2.out')])
def in_out(request):
    in_txt = (test_path / request.param[0]).read_text()
    out_txt = (test_path/ request.param[1]).read_text()
    in_list = list(map(int, in_txt.split()))
    out = int(out_txt)
    return in_list,out
