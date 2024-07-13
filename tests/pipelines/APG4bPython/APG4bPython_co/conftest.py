import pytest

pathd = '/home/komikado/project/kedro-atcoder/src/kedro_atcoder/pipelines/APG4bPython/APG4bPython_co/test'

@pytest.fixture(params=[('sample-1.in','sample-1.out'),('sample-2.in','sample-2.out')])
def test_data(request):
    al = []
    bl = []
    path_in = pathd + '/' + request.param[0]
    with open(path_in, 'r') as fi:
        n = int(fi.readline())
        for line in fi:
            a,b = list(map(int, line.split()))
            al.append(a)
            bl.append(b)    

    path_out = pathd + '/' + request.param[1]
    with open(path_out, 'r') as fo:
        cl = []
        for line in fo:
            c = str(line).strip('\n')
            cl.append(c)

    return n,al,bl,cl 