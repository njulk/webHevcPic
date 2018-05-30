#include<stdio.h>
#include<python.h>
#include<iostream>

using namespace std;
char *filename = "11.JPG";
char* dir = "F:\\11.JPG";

char* model = "basketball";
int main() {
	Py_Initialize();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('F:/webHevcPic/request/')");
	//PyObject* pName = PyString_FromString("aa");
	PyObject* pyMod = PyImport_ImportModule("aa");
	if (!pyMod) {
		cout << "创建main.py失败" << endl;
		return 0;
	} 
	PyObject* pFunc = PyObject_GetAttrString(pyMod, "sendPic");
	if (!pFunc) {
		cout << "创建函数失败" << endl;
		return 0;
	}
	int size = 32;
	PyObject* paras = Py_BuildValue("ssis", filename, dir, size, model);
	PyObject* pyRet = PyEval_CallObject(pFunc, paras);
	int ok = -1;
	int retok = PyArg_Parse(pyRet, "i", &ok); // 从返回值从取出int型返回值  
	cout << ok << endl;
	Py_Finalize();
	return 0;
}