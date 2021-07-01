##Functions for tax calculators

def onePercentStartGross(taxValue, num):
    #Start with tax applied, for removing tax
    value = 100 + float(taxValue)
    onePC = num/value

    return onePC

def onePercentStartNet(taxValue, num):
    #start with no tax applied, for adding tax
    value = float(taxValue)
    onePC = num/value

    return onePC


#Standard functions for calculation
def desiredPercentage(onePC, desired):
    value = onePC * desired

    return value


def calcTax(tax, num, desired):
    onePC = onePercent(tax, num)
    total = desiredPercentage (onePC, desired)

    return total
