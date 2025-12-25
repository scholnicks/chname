
import os
from chname.__main__ import append, arguments
import pathlib

def test_append_performs_rename(tmp_path):
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
