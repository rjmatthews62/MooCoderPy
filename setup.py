#!/usr/bin/env python

import sys,os
from distutils.core import setup
# MOST of this is handled in setup.cfg.
# Dragging version from __init__.py
fullpath=os.path.abspath("src")
if not fullpath in sys.path:
    sys.path.insert(1,fullpath)
import MooCoderPy

setup(
    version=MooCoderPy.__VERSION__
     )