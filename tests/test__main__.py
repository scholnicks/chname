# vi: set syntax=python ts=4 sw=4 sts=4 et ff=unix ai si :
#
# (c) Steven Scholnick <scholnicks@gmail.com>
# The chname source code is published under a MIT license.

import os
import pathlib

from chname.__main__ import append, arguments, lower, prepend, remove, substitute


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
