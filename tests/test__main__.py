import os
import pathlib

from chname.__main__ import append, arguments, prepend


def test_append(tmp_path):
    f = tmp_path / "another.txt"
    f.write_text("data")
    arguments.clear()
    arguments["<files>"] = [str(f)]
    arguments["<suffix>"] = "_suf"
    arguments["--dry-run"] = False
    arguments["--verbose"] = False

    append()

    assert not f.exists()
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

    assert not f.exists()
    assert (tmp_path / f"pre_{f.name}").exists()
