#include <Python.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"


// ---------------
// PYTHON FUNCTIONS
// ---------------
static PyObject* vb_load_image(PyObject *self, PyObject *args, PyObject *kwds) {
    Py_buffer buffer;
    int components = 0;
    if (!PyArg_ParseTuple(args, "y*|i", &buffer, &components))
        return NULL;

    char* bitmap = NULL;
    int x, y, n;

    Py_BEGIN_ALLOW_THREADS
    bitmap = (char*) stbi_load_from_memory(buffer.buf, buffer.len, &x, &y, &n, components);
    Py_END_ALLOW_THREADS

    if (!bitmap) {
        PyErr_SetString(PyExc_NotImplementedError, "stb_images can't load bitmap");
        return NULL;
    }

    PyObject* pybitmap = PyMemoryView_FromMemory(bitmap, x*y*n, PyBUF_READ);

    PyObject* result = Py_BuildValue("(Oiii)", pybitmap, x, y, n);
    if (!result)
        return NULL;

    return result;
}


// ---------------
// METHOD DOCSTRING
// ---------------
static char vb_load_image_doc[] = "Load png or jpeg image and convert it to bitmap.\n\n*Parameters:*\n\n"
"- `data`: Image in binary format\n- `nb_components`: Force image to have `nb_components` by pixel\n\n"
"*Returns:*\n\nTuple containing (memoryview(bitmap), width, height, num_components)";


// ---------------
// REGISTER VULKBARE METHODS
// ---------------
static PyMethodDef VulkBareMethods[] = {
    {"load_image", (PyCFunction)vb_load_image, METH_VARARGS, vb_load_image_doc},
    {NULL, NULL, 0, NULL}
};


// ---------------
// CREATE PYTHON MODULE
// ---------------
static struct PyModuleDef vulkbaremodule = {
    PyModuleDef_HEAD_INIT, "vulkbare", "VulkBare Module", -1, VulkBareMethods
};


// ---------------
// PYTHON ENTRY POINT
// ---------------
PyMODINIT_FUNC PyInit_vulkbare(void) {
    PyObject* module = PyModule_Create(&vulkbaremodule);

    if (module == NULL)
        return NULL;

    return module;
}
