import bytecode

class VM:
    """Virtual Stack Machine"""

    def __init__(self, code, main, ram=16, stack=8):
        """
        :type code: int[]
        :type main: int
        :type ram: int
        :type stack: int
        :param code: the bytecode to be executed as an array of integers
        :param main: starting address
        :param ram: ram size in bytes
        :param stack: stack size in bytes
        """

        self.__code = code  # code memory
        self.__data =  [0] * ram # data memory
        self.__stack = [0] * stack  # stack

        self.__ip = main  # instruction pointer
        self.__sp = -1  # stack pointer
        self.__fp = None  # foreign pointer

        __running = False  # if the machine is runn

    def __fetch(self):
        """ Fetch
        :return: opcode or data parameter
        :rtype: int
        """
        opcode =  self.__code[self.__ip]
        self.__ip += 1
        return opcode

    def __push(self, value):
        """ Push on the top of the stack and increments the stack pointer
        :type value: int
        """
        self.__sp += 1
        self.__stack[self.__sp] = value

    def __pop(self):
        """ Returns the top of the stack and decrements the stack pointer
        :rtype: int
        """
        value = self.__stack[self.__sp]
        self.__sp -= 1
        return value

    def execute(self, opcode):
        """ Executes the instruction received in the opcode
        :type opcode: int
        :param opcode: the opcode of the instruction
        """
        # print(self.__stack)
        # print("Mem: 0:{0}, 1:{1}, 2:{2}".format(self.__data[0], self.__data[1], self.__data[2]))
        # print("Executing {0}, IP={1} SP={2}".format(bytecode.names[opcode], self.__ip, self.__sp))

        if opcode == bytecode.IADD:
            op1 = self.__pop()
            op2 = self.__pop()
            self.__push(op1 + op2)
            return

        if opcode == bytecode.ISUB:
            op1 = self.__pop()
            op2 = self.__pop()
            self.__push(op2 - op1)
            return

        if opcode == bytecode.IMUL:
            op1 = self.__pop()
            op2 = self.__pop()
            self.__push(op1 * op2)
            return

        if opcode == bytecode.ILT:
            op1 = self.__pop()
            op2 = self.__pop()
            value = 1 if op2 < op1 else 0
            self.__push(value)

        if opcode == bytecode.IEQ:
            op1 = self.__pop()
            op2 = self.__pop()
            value = 1 if op2 == op1 else 0
            self.__push(value)

        if opcode == bytecode.BR:
            address = self.__fetch()
            self.__ip = address

        if opcode == bytecode.BRT:
            address = self.__fetch()
            condition = self.__pop()
            if condition == 1:
                self.__ip = address

        if opcode == bytecode.BRF:
            address = self.__fetch()
            condition = self.__pop()
            if condition == 0:
                self.__ip = address

        if opcode == bytecode.ICONST:
            data = self.__fetch()
            self.__push(data)
            return

        if opcode == bytecode.GSTORE:
            address = self.__fetch()
            data = self.__pop()
            self.__data[address] = data
            return

        if opcode == bytecode.GLOAD:
            address = self.__fetch()
            data = self.__data[address]
            self.__push(data)
            return

        if  opcode == bytecode.CALL:
            # expects all arguments on stack
            address = self.__fetch()
            nargs = self.__fetch()
            self.__push(nargs) # how many arguments were pushed
            self.__push(self.__fp) # save fp
            self.__push(self.__ip) # return address
            self.__fp = self.__sp # now point to the return address in the stack
            self.__ip = address # jump to the new address
            return

        if opcode == bytecode.RET:
            rvalue = self.__pop()
            self.__sp = self.__fp # new stack pointer is the current FP
            self.__ip = self.__pop() # new address is the instruction after call
            self.__fp = self.__pop() # recover FP (in case we need multiple returns)
            nargs = self.__pop() # learn how many args we need to throw
            self.__sp -= nargs
            self.__push(rvalue)
            return

        if opcode == bytecode.PRINT:
            data = self.__pop()
            print(data)
            return

        if opcode == bytecode.POP:
            data = self.__pop()
            return

        if opcode == bytecode.HALT:
            self.__running = False
            return

    def run(self):
        self.__running = True

        print('Code to execute ({1} bytes): {0}'.format(
            ' '.join('%02d'%i for i in self.__code),
            len(self.__code)
        ))

        while self.__ip < len(self.__code) and self.__running:
            opcode = self.__fetch()
            self.execute(opcode)
