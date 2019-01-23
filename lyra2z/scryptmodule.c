#include <Python.h>

#include "lyra2z.h"

static PyObject *lyra2z_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    lyra2z_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    lyra2z_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef ScryptMethods[] = {
    { "getPoWHash", lyra2z_getpowhash, METH_VARARGS, "Returns the proof of work hash using scrypt" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef Lyra2ZModule = {
    PyModuleDef_HEAD_INIT,
    "Lyra2Z_scrypt",
    "...",
    -1,
    ScryptMethods
};

PyMODINIT_FUNC PyInit_Lyra2Z_scrypt(void) {
    return PyModule_Create(&Lyra2ZModule);
}

#else
PyMODINIT_FUNC initLyra2Z_scrypt(void) {
    (void) Py_InitModule("Lyra2Z_scrypt", ScryptMethods);
}
#endif
