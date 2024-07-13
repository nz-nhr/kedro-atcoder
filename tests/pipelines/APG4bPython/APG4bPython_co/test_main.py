from kedro_atcoder.pipelines.APG4bPython.APG4bPython_co.main import solve

def test_main(test_data):
    n,al,bl,ex = test_data
    res = solve(n,al,bl)
    assert res == ex