# Installation
./configure --with-pydebug --prefix $PWD/installation/
make clean
make -j`nproc` # -s = silent
make test
make install OR cp python $PWD/installation/bin/python3 if re-compiling

# Explorations

Below works with a fresh copy of the repo, but fails if trying to clean / re-build :/
1. Configure
2. Grammar/Grammar -> pass_stmt: 'pass' -> pass_stmt: 'pass' | 'proceed'
3. make regen-grammar
4. make -j`nproc` && make install 

Running the code fails `name 'proceed' is not defined`.

Giving up.

# Python/pyareana.c
Contains the object allocation and internpretet memory blocks.
Objects are added to areana, inref, then later decref and free'ed.

Objects/listobject.c contains object utility functions
Include/listobject.h

# Starting process
The three source files you need to inspect to see this process are:

- Programs/python.c is a simple entry point.
- Modules/main.c contains the code to bring together the whole process, loading configuration, executing code and clearing up memory.
- Python/initconfig.c loads the configuration from the system environment and merges it with any command-line flags.

See https://files.realpython.com/media/swim-lanes-chart-1.9fb3000aad85.png

can use -v for debug / verbose, e.g., python3 -v -c "print('hello world')"

Python/compile.c 

# Excecution
https://realpython.com/cpython-source-code-guide/#execution
Python/pythonrun.c -> Python/ceval.c -> _PyEval_EvalCodeWithName ... interp->eval_frame()
Python/pystate.c:    interp->eval_frame = _PyEval_EvalFrameDefault;
Python/ceval.c _PyEval_EvalFrameDefault()

Include/cpython/pystate.h
Include/cpython/frameobject.h
Include/code.h contains the PyCodeObject definition
Objects/frameobject.c

Include/opcode.h CALL_FUNCTION
#define CALL_FUNCTION_KW        141
#define CALL_FUNCTION_EX        142 
??

PyUnicode_AsUTF8AndSize

# Updates
frame creation and deletetion and clearing -> cap = 0
except if there is a previous stack frame, in which case inheritance
set the cap to max = 10 in _PyEval_EvalCodeWithName
in call_function, update the cap based on policy
added code CFI-like to catch function pointer overwrite cross packages.