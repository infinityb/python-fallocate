from .defines import falloc as _falloc_const_mod
import errno as _errno
import ctypes as _ctypes
_libc = _ctypes.CDLL('libc.so.6')

_fallocate = _libc.fallocate

# I have no idea how to detect the real type of off_t...
_fallocate.argtypes = [
    _ctypes.c_int,
    _ctypes.c_int,
    _ctypes.c_ulong,
    _ctypes.c_ulong
]

locals().update(dict(_falloc_const_mod.falloc_defs))


def fallocate(file_desc, mode, offset, length):
    if not isinstance(file_desc, int):
        raise TypeError("file_desc must be integer")
    if not isinstance(mode, int):
        raise TypeError("mode must be integer")
    if not isinstance(offset, int):
        raise TypeError("offset must be integer")
    if not isinstance(length, int):
        raise TypeError("length must be integer")
    rv = _fallocate(file_desc, mode, offset, length)
    if rv < 0:
        raise OSError(-rv, _errno.errorcode[-rv])
