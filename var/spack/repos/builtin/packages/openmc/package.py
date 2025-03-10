# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Openmc(CMakePackage):
    """OpenMC is a community-developed Monte Carlo neutron and photon transport
       simulation code. It is capable of performing fixed source, k-eigenvalue, and
       subcritical multiplication calculations on models built using either a
       constructive solid geometry or CAD representation. OpenMC supports both
       continuous-energy and multigroup transport. The continuous-energy particle
       interaction data is based on a native HDF5 format that can be generated from ACE
       files produced by NJOY. Parallelism is enabled via a hybrid MPI and OpenMP
       programming model."""

    homepage = "https://docs.openmc.org/"
    url = "https://github.com/openmc-dev/openmc/tarball/v0.13.0"
    git = "https://github.com/openmc-dev/openmc.git"

    version('develop', branch='develop', submodules=True)
    version('master', branch='master', submodules=True)
    version('0.13.0', commit='cff247e35785e7236d67ccf64a3401f0fc50a469', submodules=True)
    version('0.12.2', commit='cbfcf908f8abdc1ef6603f67872dcf64c5c657b1', submodules=True)
    version('0.12.1', commit='36913589c4f43b7f843332181645241f0f10ae9e', submodules=True)
    version('0.12.0', commit='93d6165ecb455fc57242cd03a3f0805089c0e0b9', submodules=True)
    version('0.11.0', sha256='19a9d8e9c3b581e9060fbd96d30f1098312d217cb5c925eb6372a5786d9175af')
    version('0.10.0', sha256='47650cb45e2c326ae439208d6f137d75ad3e5c657055912d989592c6e216178f')

    variant('mpi', default=False, description='Enable MPI support')
    variant('openmp', default=True, description='Enable OpenMP support')
    variant('optimize', default=False, description='Enable optimization flags')
    variant('debug', default=False, description='Enable debug flags')

    depends_on('git', type='build')
    depends_on('hdf5+hl~mpi', when='~mpi')
    depends_on('mpi', when='+mpi')
    depends_on('hdf5+hl+mpi', when='+mpi')

    def cmake_args(self):
        options = ['-DCMAKE_INSTALL_LIBDIR=lib']  # forcing bc sometimes goes to lib64

        if '+mpi' in self.spec:
            options += ['-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc,
                        '-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx]

        options += [self.define_from_variant('openmp')]
        options += [self.define_from_variant('optimize')]
        options += [self.define_from_variant('debug')]

        if '+optimize' in self.spec:
            self.spec.variants['build_type'].value = 'Release'

        if '+debug' in self.spec:
            self.spec.variants['build_type'].value = 'Debug'

        return options
