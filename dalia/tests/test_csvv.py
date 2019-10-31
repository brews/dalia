import io

import pytest
import numpy as np

from dalia import read_csvv


@pytest.fixture
def csvv_filebuffer():
    fl_content = """---
oneline: oneline
version: version
dependencies: dependencies
description: description
csvv-version: csvv_version
variables:
  k1: v1
...
observations
123
prednames
a,b,c
covarnames
1,1,1
gamma
1.0,2.0,3.0
gammavcv
1.0,2.0,3.0
1.0,2.0,3.0
1.0,2.0,3.0
residvcv
123.0
"""
    return io.StringIO(fl_content)


@pytest.mark.parametrize(
    "target_attr,expected",
    [
        ("oneline", "oneline"),
        ("version", "version"),
        ("dependencies", "dependencies"),
        ("csvv_version", "csvv_version"),
        ("variables", {"k1": "v1"}),
        ("observations", 123),
        ("prednames", ["a", "b", "c"]),
        ("covarnames", ["1", "1", "1"]),
        ("residvcv", 123.0),
    ],
)
def test_read_csvv(csvv_filebuffer, target_attr, expected):
    """Test that read_csvv() gives Csvv with correct non-ndarray attributes"""
    csvv = read_csvv(csvv_filebuffer)
    assert getattr(csvv, target_attr) == expected


@pytest.mark.parametrize(
    "target_attr,expected",
    [
        ("gamma", np.array([1, 2, 3], dtype="float")),
        (
            "gammavcv",
            np.repeat(np.array([[1, 2, 3]], dtype="float"), repeats=3, axis=0),
        ),
    ],
)
def test_read_csvv_arrays(csvv_filebuffer, target_attr, expected):
    """Test that read_csvv() gives Csvv with correct ndarray attributes"""
    csvv = read_csvv(csvv_filebuffer)
    np.testing.assert_allclose(getattr(csvv, target_attr), expected)
