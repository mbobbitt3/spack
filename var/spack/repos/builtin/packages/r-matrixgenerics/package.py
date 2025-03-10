# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixgenerics(RPackage):
    """S4 Generic Summary Statistic Functions that Operate on Matrix-Like
    Objects.

    S4 generic functions modeled after the 'matrixStats' API for alternative
    matrix implementations. Packages with alternative matrix implementation can
    depend on this package and implement the generic functions that are defined
    here for a useful set of row and column summary statistics. Other package
    developers can import this package and handle a different matrix
    implementations without worrying about incompatibilities."""

    bioc = "MatrixGenerics"

    version('1.8.0', commit='e4cc34d53bcfb9a5914afd79fda31ecd5037a47a')
    version('1.6.0', commit='4588a60e5cc691424c17faa281bdd7d99d83ec34')
    version('1.2.1', commit='abcc9ca0504e0b915cd7933a3169a8e9e5bd2fe9')

    depends_on('r-matrixstats@0.57.1:', type=('build', 'run'))
    depends_on('r-matrixstats@0.60.1:', type=('build', 'run'), when='@1.6.0:')
