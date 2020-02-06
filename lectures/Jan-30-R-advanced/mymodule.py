# -*- coding: utf-8 -*-
""" A single short line summrizing the module.

A more lengthy explanation of the module if needed.
This can be as many lines as you want.

Modules can contain any number of things.
"""

class vec3:
    """ (x, y, z) vector
    
    Supports operations such as translation.
    """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        """ Return (x, y, z)
        """
        return f"({self.x}, {self.y}, {self.z})"
    
    def translate(self, dx, dy, dz):
        """ Translate by (dx, dy, dz)
        """
        self.x += dx
        self.y += dy
        self.z += dz
    
    def add(self, vec):
        """ Return the sum of this vector and the input vector. 
        """
        newvec = vec3()
        newvec.x = self.x + vec.x
        newvec.y = self.y + vec.y
        newvec.z = self.z + vec.z
        return newvec


class vec4(vec3):
    """ (x, y, z, w) vector
    """
    def __init__(self, x=0, y=0, z=0, w=1):
        vec3.__init__(self, x, y, z)
        self.w = w
    
    def __repr__(self):
        """ Return (x, y, z, w)
        """
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
