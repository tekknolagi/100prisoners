#include <Python.h>
#include <algorithm>
#include <stdio.h>
#include <vector>

static long try_find_self(const std::vector<int> &boxes, long start,
                          long limit) {
  long next_box = boxes[start];
  long num_opened = 1;
  while (next_box != start && num_opened < limit) {
    next_box = boxes[next_box];
    num_opened++;
  }
  return next_box == start;
}

static PyObject *seed_random(PyObject * /* self */, PyObject *args) {
  PyObject *seed_obj;
  if (!PyArg_UnpackTuple(args, "seed", 1, 1, &seed_obj)) {
    return nullptr;
  }
  if (!PyLong_CheckExact(seed_obj)) {
    PyErr_Format(PyExc_TypeError,
                 "seed_obj_random expected seed to be an int, instead got %s",
                 Py_TYPE(seed_obj)->tp_name);
    return nullptr;
  }
  long seed = PyLong_AsLong(seed_obj);
  srand(seed);
  Py_RETURN_NONE;
}

static PyObject *sample(PyObject * /* self */, PyObject *args) {
  PyObject *nboxes_obj, *limit_obj;
  if (!PyArg_UnpackTuple(args, "args", 2, 2, &nboxes_obj, &limit_obj)) {
    return nullptr;
  }
  if (!PyLong_CheckExact(nboxes_obj)) {
    PyErr_Format(PyExc_TypeError,
                 "sample expected nboxes to be an int, instead got %s",
                 Py_TYPE(nboxes_obj)->tp_name);
    return nullptr;
  }
  if (!PyLong_CheckExact(limit_obj)) {
    PyErr_Format(PyExc_TypeError,
                 "sample expected limit to be an int, instead got %s",
                 Py_TYPE(limit_obj)->tp_name);
    return nullptr;
  }
  long nboxes = PyLong_AsLong(nboxes_obj);
  long limit = PyLong_AsLong(limit_obj);
  std::vector<int> boxes;
  for (long i = 0; i < nboxes; i++) {
    boxes.push_back(i);
  }
  std::random_shuffle(boxes.begin(), boxes.end());
  long sum = 0;
  for (long i = 0; i < nboxes; i++) {
    sum += try_find_self(boxes, i, limit);
  }
  return PyLong_FromLong(sum);
}

static PyMethodDef simulate_fast_methods[] = {
    {"seed_random", seed_random, METH_VARARGS,
     "Seed the C++ random number generator"},
    {"sample", sample, METH_VARARGS, "Sample the problem space"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef simulate_fast_definition = {
    PyModuleDef_HEAD_INIT, "simulate_fast",
    "A Python module that prints 'hello world' from C code.", -1,
    simulate_fast_methods,
    nullptr,
    nullptr,
    nullptr,
    nullptr};

PyMODINIT_FUNC PyInit_simulate_fast(void) {
  Py_Initialize();
  return PyModule_Create(&simulate_fast_definition);
}
