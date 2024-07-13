import pytest

pathd = '/home/komikado/project/kedro-atcoder/src/kedro_atcoder/pipelines/APG4bPython/APG4bPython_cn/test'

@pytest.fixture(params=[('sample-1.in','sample-1.out'),('sample-2.in','sample-2.out'),('sample-3.in','sample-3.out'),('sample-4.in','sample-4.out')])
def test_data_fixture(request):
    path = pathd + '/' + request.param[0] 
    with open(path) as f:
        tokens = iter(f.read().split())
        a = int(next(tokens))
        b = [None for _ in range(a)]
        c = [None for _ in range(a)]
        for i in range(a):
            b[i] = int(next(tokens))
            c[i] = next(tokens)
        d = int(next(tokens))
    return a,b,c,d,request.param[1]