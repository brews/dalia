"""
Utility functions to read and parse regional hierarchy CSV files
"""

from csv import reader as csvreader
from anytree import Node


def _parse_csv_buffer(b, skiplines):
    reader = csvreader(b)

    root = Node(
        region_key="World",
        parent_key="",
        name="World",
        alternatives="",
        is_terminal="",
        gadmin="",
        agglomid="",
        notes="",
    )
    nodes = {"World": root}

    for ln in reader:
        if reader.line_num <= skiplines:
            continue

        region_key = str(ln[0])
        parent_key = str(ln[1])

        nodes[region_key] = Node(
            parent=nodes[parent_key],
            region_key=region_key,
            parent_key=parent_key,
            name=str(ln[2]),
            alternatives=str(ln[3]),
            is_terminal=str(ln[4]),
            gadmin=str(ln[5]),
            agglomid=str(ln[6]),
            notes=str(ln[7]),
        )
    return root


def read_hierarchy(path_or_buffer, skiplines=32):
    """Read a region hierarchy CSV file, return hier root
    """
    root = None
    if isinstance(path_or_buffer, str):
        with open(path_or_buffer, "r") as fl:
            root = _parse_csv_buffer(fl, skiplines=skiplines)
    else:
        root = _parse_csv_buffer(path_or_buffer, skiplines=skiplines)
    return root
