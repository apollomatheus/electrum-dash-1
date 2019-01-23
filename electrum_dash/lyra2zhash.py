# -*- coding: utf-8 -*-

import sys


try:
    import Lyra2Z_scrypt
    import_success = True
    loaded = True
except ImportError:
    import_success = False
    loaded = False

print(loaded)
if loaded:
    from ctypes import cdll, create_string_buffer, byref

    if sys.platform == 'darwin':
        name = 'Lyra2Z_scrypt.dylib'
    elif sys.platform in ('windows', 'win32'):
        name = 'Lyra2Z_scrypt.dll'
    else:
        name = 'Lyra2Z_scrypt.so'

    try:
        llyra2z = cdll.LoadLibrary(name)
        lyra2z = llyra2z.Lyra2Z_scrypt
    except: 
        loaded = False
        
# Try to import direct from library
if loaded or not loaded and import_success:

    def getL2zPoWHash(header):
        if loaded:
            return lyra2z(header)
        return getPoWHash(header)

if not import_success and not loaded:
    raise ImportError('Can not import Lyra2Z_script')
