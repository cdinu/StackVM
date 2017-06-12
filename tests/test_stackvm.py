import unittest
import context

from stackvm.bytecode import *
from stackvm.vm import VM

programs = {}

programs['p9plus8x2plus8'] = [
    ICONST, 9,
    ICONST, 8,
    IADD,
    GSTORE, 0,
    ICONST, 2,
    ICONST, 8,
    IADD,
    GLOAD, 0,
    IMUL,
    PRINT,
    HALT
]

programs['comp2and3'] = [
    ICONST, 3,
    ICONST, 3,
    IEQ,
    BRF, 11,
    ICONST, 1,
    PRINT,
    HALT,
    ICONST, 2,
    PRINT,
    HALT
]

programs['call test no args'] = [
    # SUBROUTINE: INCREMENT VALUE AT DATA #0
    ICONST, 1, # FIRST OPERAND
    GLOAD, 0,  # LOAD VALUE FROM ADDRESS #0
    IADD,      # ADD THEM, PUSH TO STACK
    GSTORE, 0, # STORE THE NEW VALUE
    GLOAD, 0,  # LOAD VALUE (TO HAVE IT RETURNED)
    RET,       # RETURN

    # PROGRAM INIT
    ICONST, 122,  # INITIAL VALUE TO DISPLAY
    GSTORE, 0,  # STORE IT AT DATA #0

    ICONST, 500,  # HOW MANY ITERATIONS TO HAVE
    GSTORE, 1,  # STORE IT AT DATA #2

    ICONST, 0,  # THIS WILL BE OUR LOOP COUNTER
    GSTORE, 2,  # STORE IT AT DATA #2

    # LOOP
    CALL, 0, 0, # CALL THE SUBROUTINE
    PRINT,      # DISPLAY THE RESULT
    GLOAD, 2,   # LOAD THE COUNTER INDEX
    ICONST, 1,  # SECOND OPERAND
    IADD,       # (INCREMENT)
    GSTORE, 2,  # STORE IT AT DATA #1
    GLOAD, 2,   # RETREIVE IT
    GLOAD, 1,   # COMPARE WITH HOW MANY ITERATIONS
    ILT,        # PUT TRUE STACK IF COUNT < 10
    BRT, 22,    # GTOTO "LOOP"
    HALT        # END PROGRAM
]


programs['fibo no params'] = [
    # JUMP TO PROGRAM:
    BR, 16,

    # SUBROUTINE:
    GLOAD, 10,  # FIRST OPERAND
    GLOAD, 11,  # SECOND OPERAND
    IADD,       # ADD THEM, PUSH TO STACK
    GLOAD, 11,  # BRING SECOND OP TO STACK
    GSTORE, 10, # STORE IT IN LIEU OF THE FIRST
    GSTORE, 11, # STORE THE SUM AS THE SECOND OP.
    GLOAD, 11,  # SUM IS TO BE RETURNED
    RET,       # RETURN

    # PROGRAM INIT
    ICONST, 0,   # A1
    GSTORE, 10,  # STORE IT AT DATA #10

    ICONST, 1,  # A2
    GSTORE, 11,  # STORE IT AT DATA #2

    ICONST, 10,  # HOW MANY NUMBERS TO HAVE
    GSTORE, 1,  # STORE IT AT DATA #1

    ICONST, 0,  # THIS WILL BE OUR LOOP COUNTER
    GSTORE, 2,  # STORE IT AT DATA #2

    # LOOP
    CALL, 2, 0, # CALL THE SUBROUTINE WITH NO PARAMS
    PRINT,      # DISPLAY THE RESULT
    GLOAD, 2,   # LOAD THE COUNTER INDEX
    ICONST, 1,  # SECOND OPERAND
    IADD,       # (INCREMENT)
    GSTORE, 2,  # STORE IT AT DATA #1
    GLOAD, 2,   # RETREIVE IT
    GLOAD, 1,   # COMPARE WITH HOW MANY ITERATIONS
    ILT,        # PUT TRUE STACK IF COUNT < 10
    BRT, 32,    # GTOTO "LOOP"
    HALT        # END PROGRAM
]

class TestStackVM(unittest.TestCase):

    def test(self):
        vm = VM(programs['fibo no params'], 0)
        vm.run()

if __name__ == '__main__':
    unittest.main()
