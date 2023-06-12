#include "lists.h"
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int n;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (n = 0; n < size; n++)
		printf("Element %d: %s\n", n, Py_TYPE(obj->ob_item[n])->tp_name);
}
