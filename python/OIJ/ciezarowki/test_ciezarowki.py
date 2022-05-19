from pathlib import Path
from time import time
from ciezarowki import main


def test_oioioi(input_path):
    output_path = input_path.with_suffix(".out")
    with output_path.open() as fd:
        expected_result = [i.rstrip() for i in fd]
    with input_path.open() as fd:
        start = time()
        raw_result = main(fd)
        stop = time()
    result = list(map(str, raw_result))
    assert result == expected_result
    run_time = stop - start
    assert run_time < 20


def pytest_generate_tests(metafunc):
    test_path = Path(__file__).parent.joinpath("cie")
    paths = list(test_path.glob("*.in"))
    metafunc.parametrize("input_path", paths, ids=[p.stem for p in paths])
