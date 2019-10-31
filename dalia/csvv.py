"""
Reading and representing CSVV text files
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict

import numpy as np
import yaml


@dataclass
class Csvv:
    """Data from a CSVV file
    """

    oneline: str
    version: str
    dependencies: str
    description: str
    csvv_version: str
    variables: Dict[str, str]
    observations: int
    prednames: List[str]
    covarnames: List[str]
    gamma: np.ndarray
    gammavcv: np.ndarray
    residvcv: float


def _parse_csvvlines(lines, sep=","):
    """List of str from CSVV file to dict

    Parameters
    ----------
    lines : sequence of str
        To parse.
    sep : str or None, optional
        Value delimiter for the body of the CSVV file. If None, delimits white
        space.

    Returns
    -------
    meta : dict
    """
    # This all could be done better...
    header_sections = [
        "oneline",
        "version",
        "dependencies",
        "description",
        "csvv-version",
        "variables",
    ]
    body_sections = [
        "observations",
        "prednames",
        "covarnames",
        "gamma",
        "gammavcv",
        "residvcv",
    ]
    # Divide into header an body
    header_lines = []
    body = defaultdict(list)

    inheader = False
    inbody = False

    # Grab header. Find start idx of body.
    n_lines = len(lines)
    for idx, l in enumerate(lines):

        if l.strip() == "---":
            # First line of file, indicates header incoming.
            inheader = True
            inbody = False
            continue

        if l.strip() == "..." and n_lines > idx:
            # First transition to body.
            inheader = False
            inbody = True
            continue
        elif l.strip() == "...":
            raise IndexError("CSVV body has too few lines")

        if inheader:
            header_lines.append(l.rstrip())
            continue

        if inbody:
            if l.strip() in body_sections:
                # This is a body section.
                inbody = l.strip()
                continue
            elif inbody in body_sections:
                # This is a data section.
                body[inbody].append([x.strip() for x in l.split(sep)])

    meta = yaml.load("\n".join(header_lines), Loader=yaml.SafeLoader)
    # Combine sections
    meta.update(body)

    assert set(list(meta.keys())) == set(header_sections + body_sections)

    # Clean body data
    # Flatten nested lists where needed.
    for k in ["prednames", "covarnames", "gamma", "residvcv", "observations"]:
        meta[k] = [item for sublist in meta[k] for item in sublist]

    # Check for correct len.
    n = len(meta["gammavcv"])
    for k in ["prednames", "covarnames", "gamma"]:
        assert len(meta[k]) == n, f"{k} does not contain {n} elements"

    # Cast numerics from strings
    for k in ["gamma", "gammavcv", "residvcv"]:
        meta[k] = np.array(meta[k], dtype="float")
    meta["observations"] = np.array(meta["observations"], dtype="int")

    # Arrays to scalars
    meta["observations"] = meta["observations"].item()
    meta["residvcv"] = meta["residvcv"].item()

    # meta keys eventually become attrs, so remove "-"
    meta["csvv_version"] = meta.pop("csvv-version")
    return meta


def read_csvv(filepath_or_buffer, sep=","):
    """Read a CSVV file into a CSVV object

    Parameters
    ----------
    filepath_or_buffer
        str path to target file or opened buffer.
    sep : str or None, optional
        Value delimiter for the body of the CSVV file. If None, delimits
        whitespace.

    Returns
    -------
    Csvv
    """
    if isinstance(filepath_or_buffer, str):
        with open(filepath_or_buffer, "r") as fl:
            fl_guts = fl.readlines()
    else:
        fl_guts = filepath_or_buffer.readlines()

    return Csvv(**_parse_csvvlines(fl_guts, sep=sep))
