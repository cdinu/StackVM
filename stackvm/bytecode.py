# opcodes
IADD = 1  # int add
ISUB = 2  # int sub
IMUL = 3  # int multiply
ILT = 4   # int less than
IEQ = 5   # int equal
BR = 6    # branch
BRT = 7   # branch if true
BRF = 8   # branch if false
ICONST = 9   # push int const
LOAD = 10    # load from local
GLOAD = 11   # load from global
STORE = 12   # store
GSTORE = 13  # global store
CALL = 14    # call a subroutine
RET = 15     # return after a call
PRINT = 16   # print stack top
POP = 17     # throw away the top of the stack
HALT = 18    # well, halt

names = [
    "NONE",
    "IADD", "ISUB", "IMUL", "ILT", "IEQ",
    "BR", "BRT", "BRF",
    "ICONST", "LOAD", "GLOAD", "STORE", "GSTORE",
    "CALL", "RET",
    "PRINT", "POP", "HALT"
]