import pytest

from toolz import partition_all


@pytest.mark.parametrize(
    ("size", "error"), [(0, ValueError), (-1, ValueError), (1.5, TypeError)]
)
def test_invalid_size_does_not_start_source(size, error):
    class GuardedSource:
        calls = 0

        def __iter__(self):
            self.calls += 1
            raise AssertionError("source iteration was started")

    source = GuardedSource()
    with pytest.raises(error):
        next(partition_all(size, source))
    assert source.calls == 0
