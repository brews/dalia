import io

import pytest

from dalia import read_hierarchy


@pytest.fixture
def hiercsv_filebuffer():
    fl_content = """region-key,parent-key,name,alternatives,is_terminal,gadmid,agglomid,notes
CAmericas,World,Americas,,False,,,
U021,CAmericas,North America,,False,,,
"""
    return io.StringIO(fl_content)


def test_read_hierarchy(hiercsv_filebuffer):
    """Test that we get a root, populated with children, skips files lines
    """
    victim = read_hierarchy(hiercsv_filebuffer, skiplines=1)
    assert victim.region_key == "World"
    assert victim.children[0].region_key == "CAmericas"
    assert victim.children[0].children[0].region_key == "U021"
