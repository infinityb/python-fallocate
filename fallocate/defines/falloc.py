from collections import namedtuple
import os as _os
import ctypes as _ctypes

from .. import defines as _definemod
from ..ext.cconst import cdefineread as _cdefineread

FILENAME = 'libfallocdefines.so'
EXPORTS = ['falloc_defs', 'errcode_defs']

_opus_defines = _ctypes.CDLL(_os.path.join(
    _definemod.__path__[0], FILENAME))


def _make_module(module_name):
    members = _cdefineread.load(_opus_defines, module_name).members
    return [(x.name, x.value) for x in members]

falloc_defs = _make_module('falloc_defs')
errcode_defs = _make_module('errcode_defs')
