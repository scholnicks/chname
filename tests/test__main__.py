# vi: set syntax=python ts=4 sw=4 sts=4 et ff=unix ai si :
#
# (c) Steven Scholnick <scholnicks@gmail.com>
# The chname source code is published under a MIT license.

import os
import pathlib

import pytest

from chname.__main__ import append, arguments, calculateExtension, lower, order, prepend, remove, substitute


def test_append(tmp_path):
    f = tmp_path / "another.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["<suffix>"] = "_suf"
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    append()
    assert (tmp_path / f"{f.name}_suf").exists()


def test_prepend(tmp_path):
    f = tmp_path / "another.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["<prefix>"] = "pre_"
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    prepend()
    assert (tmp_path / f"pre_{f.name}").exists()


def test_lower(tmp_path):
    f = tmp_path / "Another.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    lower()
    assert (tmp_path / "another.txt").exists()


def test_substitute(tmp_path):
    f = tmp_path / "an111other.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["<old>"] = "111"
    arguments["<new>"] = "222"
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    substitute()
    assert (tmp_path / "an222other.txt").exists()


def test_remove(tmp_path):
    f = tmp_path / "an111other.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["<pattern>"] = "111"
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    remove()
    assert (tmp_path / "another.txt").exists()


def test_calculate_extension_single_extension():
    files = ["one.txt", "two.txt"]
    assert calculateExtension(files) == ".txt"


def test_calculate_extension_case_insensitive():
    files = ["ONE.TXT", "two.Txt", "three.txt"]
    assert calculateExtension(files) == ".txt"


def test_calculate_extension_no_extension_returns_empty_string():
    files = ["one", "two", "three"]
    assert calculateExtension(files) == ""


def test_calculate_extension_multiple_extensions_raises_systemexit():
    files = ["one.txt", "two.mp3"]
    with pytest.raises(SystemExit) as excinfo:
        calculateExtension(files)
    msg = str(excinfo.value)
    assert "Only one extension allowed" in msg
    assert ".txt" in msg and ".mp3" in msg


def test_order(tmp_path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("data")
    b.write_text("data")

    arguments.clear()
    # provide in reverse order to ensure sorting is used
    arguments["<files>"] = [str(b), str(a)]
    arguments["--dry-run"] = False
    arguments["--verbose"] = False
    arguments["--quiet"] = False

    order()

    assert (tmp_path / "01 - a.txt").exists()
    assert (tmp_path / "02 - b.txt").exists()
