# -*- coding: utf-8 -*-

import sys


try:
    from neoscrypt import getPoWHash
    import_success = True
    loaded = True
except ImportError:
    import_success = False
    loaded = False


if loaded:
    from ctypes import cdll, create_string_buffer, byref

    if sys.platform == 'darwin':
        name = 'libneoscrypt.dylib'
    elif sys.platform in ('windows', 'win32'):
        name = 'libneoscrypt-0.dll'
    else:
        name = 'libneoscrypt.so'

    try:
        lneoscrypt = cdll.LoadLibrary(name)
        neoscrypt = lneoscrypt.neoscrypt
    except: 
        loaded = False
        
if loaded or not loaded and import_success:
    hash_out = create_string_buffer(32)

    def getNeoPoWHash(header):
        if loaded:
            return neoscrypt(header)
        return getPoWHash(header)

if not import_success and not loaded:
    raise ImportError('Can not import neoscrypt')
