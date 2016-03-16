"""
DeepGraph - Representation & Analysis of Complex Systems
========================================================

DeepGraph is a scalable, general-purpose data analysis package. It
implements a network representation based on pandas DataFrames and
provides methods to construct, partition and plot graphs, to interface
with popular network packages and more.

It is based on a new network representation introduced in (coming
soon..).

This module provides:

   1. A ``deepgraph.DeepGraph`` class for graph representation,
       construction and partitioning, with interfacing methods to common
       network representations and popular Python network packages. This
       class also provides plotting methods to visualize graphs and
       their properties and to benchmark the graph construction
       parameters.

   2. A ``deepgraph.functions`` module, providing auxiliary
       **connector** and **selector** functions to create edges between
       nodes.

Documentation
-------------

See http://deepgraph.readthedocs.org for a full documentation, and
[coming soon..] for the paper describing the theoretical framework.
Otherwise, see the docstrings of the objects in the deepgraph namespace.

>>> import deepgraph as dg
>>> help(dg.DeepGraph)
>>> help(dg.functions)

The docstrings assume that ``deepgraph`` has been imported as ``dg``,
``numpy`` as ``np``, and ``pandas`` as ``pd``.

Citing DeepGraph
----------------

Please acknowledge and cite the use of this software and its authors
when results are used in publications or published elsewhere. You can
use the following BibTex entry (coming soon..):

"""

from __future__ import print_function, division, absolute_import

# Copyright (C) 2016 by
# Dominik Traxl <dominik.traxl@posteo.org>
# All rights reserved.
# BSD license.

from .deepgraph import DeepGraph
from . import functions

__all__ = ['DeepGraph', 'functions']
__version__ = '0.0.4'
__author__ = "Dominik Traxl <dominik.traxl@posteo.org>"
__copyright__ = "Copyright 2014-2016 Dominik Traxl"
__license__ = "BSD"
__URL__ = "https://github.com/deepgraph/deepgraph/"
__bibtex__ = """coming soon.."""
