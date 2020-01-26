import math

class Part:

    def __init__(self, sign, const, var, power):
        self.sign = sign
        self.const = const
        self.var = var
        self.power = power


    # Allows to get sign mulitpiled by constant while keeping starting state
    def getMathConst(self):

        if self.sign == False:
            return float(self.const) * -1
        else:
            return float(self.const)


    def __str__(self):

        return "{0}{1} to the power of {2}".format(self.getMathConst(), self.var, float(self.power))

    def toString(self):

        return "{0}{1} to the power of {2}".format(self.getMathConst(), self.var, float(self.power))



    def equals(self, varFill):

        total = self.getMathConst()*(float(varFill) ** float(self.power))

        return "{} for {} equals {}".format(varFill, self.var, total)

