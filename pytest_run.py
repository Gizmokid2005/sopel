#!/usr/bin/env python
"""This is a script for running pytest from the command line.

This script exists so that the project directory gets added to sys.path, which
prevents us from accidentally testing the globally installed sopel version.

pytest_run.py
Copyright 2013, Ari Koivula, <ari@koivu.la>
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
from __future__ import generator_stop

if __name__ == "__main__":
    import sys
    import pytest
    returncode = pytest.main()
    sys.exit(returncode)
