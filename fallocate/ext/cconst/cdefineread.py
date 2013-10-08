import ctypes

class constdef(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('value', ctypes.c_int),
    ]

    def __repr__(self):
        return "constdef(name=%s, value=%s)" % (self.name, self.value)

class constdefs(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('_members', ctypes.POINTER(constdef))
    ]

    def __repr__(self):
        return "constdefs(name=%r, members=%r)" % (
            self.name, self.members)

    @property
    def members(self):
        o = list()
        i = 0
        while True:
            if not self._members[i].name:
                break;
            o.append(self._members[i])
            i += 1
        return o

def load(library, symbol):
    return constdefs.in_dll(library, symbol)

