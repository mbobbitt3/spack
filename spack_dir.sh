export SPACK_USER_CONFIG_PATH=/dev/shm/spack/user_config
export SPACK_SYSTEM_CONFIG_PATH=/dev/shm/spack/sys_config
export SPACK_USER_CACHE_PATH=/dev/shm/spack/user_cache
export TEMPDIR=/dev/shm/spack/t
mkdir \
		${SPACK_USER_CONFIG_PATH}  \
		${SPACK_SYSTEM_CONFIG_PATH}\
		${SPACK_USER_CACHE_PATH}   \
		${TEMPDIR}

