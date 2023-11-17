import ctypes



class SphericalFuncs(object):
    lib = ctypes.CDLL('./spherical_harmonic.dll')
    spherical_harmonic_real_c = lib.spherical_harmonic_real
    spherical_harmonic_imag_c = lib.spherical_harmonic_imag
    def __init__(self):
        lib = ctypes.CDLL('./spherical_harmonic.dll')
        spherical_harmonic_real_c = lib.spherical_harmonic_real
        spherical_harmonic_imag_c = lib.spherical_harmonic_imag
        
        self.spherical_harmonic_real_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
        self.spherical_harmonic_real_c.restype = ctypes.c_double
        self.spherical_harmonic_imag_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
        self.spherical_harmonic_imag_c.restype = ctypes.c_double
    
    def spherical_harmonic_real(self, theta, phi, l, m):
        return self.spherical_harmonic_real_c(ctypes.c_double(theta), ctypes.c_double(phi), ctypes.c_int(l), ctypes.c_int(m))

    def spherical_harmonic_imag(self, theta, phi, l, m):
        return self.spherical_harmonic_imag_c(ctypes.c_double(theta), ctypes.c_double(phi), ctypes.c_int(l), ctypes.c_int(m))





    