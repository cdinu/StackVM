class Context:
    def __init__(self):
        self.__instructions = [];

    def emit(self, instruction):
        print 'I:%d'%instruction
        self.__instructions.append(instruction)

    def emitWithParam(self, instruction, param):
        print 'I:%d D:%d'%(instruction, param)
        self.__instructions.append(instruction)
        self.__instructions.append(param)

    def getCode(self):
        return self.__instructions
