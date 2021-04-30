import math


def calc_vat(value, percent):
    '''VAT calculation'''
    return value * (percent*0.01)


def main():
    '''main funcion'''

    # Values to input
    # TODO: Look up argparse and implement with that
    inv_value = 10
    numbers20 = [2, 5, 8, 16.44]
    numbers5 = [1, 5, 0.5]

    # Checking which VAT values to run
    vat20 = False if (len(numbers20) == 0) else True
    vat5 = False if (len(numbers5) == 0) else True

    # Calculating - do not input here
    total_vat = 0
    net_total = 0
    vat_check = 0

    if vat20:
        numbers20 = [float(l) for l in numbers20]
        vat20_sum = sum([calc_vat(n, 20) for n in numbers20])
        print(f"VAT at 20%: {vat20_sum}")
 
        total_vat += vat20_sum
        net_total += sum(numbers20)
        vat_check += sum(numbers20)*0.2

    if vat5:
        numbers5 = [float(l) for l in numbers5]
        vat5_sum = sum([calc_vat(n, 5) for n in numbers5])
        print(f"VAT at 5%: {vat5_sum}")

        total_vat += vat5_sum
        net_total += sum(numbers5)
        vat_check += sum(numbers5)*0.05

    #Printing the values    
    print(f"Goods Value: {inv_value - total_vat}")
    print(f"Total VAT: {total_vat}")

    if math.fabs(total_vat - vat_check) > 0.0001:
        print(f"VAT Check: {vat_check}")
    else:
        print("VAT Check: Consistent")

    print(f"Invoice Value: {inv_value}")


if __name__ == "__main__":
    main()
