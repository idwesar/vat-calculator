##Remove tax from a payment - start with the gross

def onePercent(taxValue, num):
    value = 100 + float(taxValue)
    onePC = num/value

    return onePC


def desiredPercentage(onePC, desired):
    value = onePC * desired

    return value


def calcTax(tax, num, desired):
    onePC = onePercent(tax, num)
    total = desiredPercentage (onePC, desired)

    return total


def main():
    '''main funcion'''

    numbers = [2, 3 ,4, 5]
    taxRemoved = []
    rounded = []

    for num in numbers:
        taxRemoved.append(calcTax(20, num, 100))

    for num in taxRemoved:
        rounded.append(round(num, 3))


    print(taxRemoved)
    print(rounded)


if __name__ == "__main__":
    main()
