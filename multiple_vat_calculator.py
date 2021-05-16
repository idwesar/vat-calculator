import math


def calc_vat(value, percent):
    '''VAT calculation'''
    return value * (percent*0.01)


def main():
    '''main funcion'''

    numbers20 = []
    numbers5 = []
    
    # Input statements
    #TODO: add better input sanitisation, add check for valid input, ask user to re-input if invalid entry
    inv_value = input("What is the total of the invoice/receipt (including VAT)? ")
    twenty = input("What values are subject to 20% VAT? If none, please type 'none'. Please separate values with a comma and a space. ")
    five = input("What values are subject to 5% VAT? If none, please type 'none'. Please separate values with a comma and a space. ")
    
    
    #converting the user input
    inv_value = float(inv_value)

    if twenty == "none":
        numbers20 = []
    else:
        input20 = list(twenty.split(", "))
        for x in input20:
            numbers20.append(float(x))
    
    if five == "none":
        numbers5 = []
    else:
     input5 = list(five.split(", "))
     for x in input5:
        numbers5.append(float(x))

    # Checking which VAT values to run
    vat20 = False if (len(numbers20) == 0) else True
    vat5 = False if (len(numbers5) == 0) else True

    # Calculating - do not input here
    total_vat = 0
    vat_check = 0

    if vat20:
        numbers20 = [float(l) for l in numbers20]
        vat20_sum = sum([calc_vat(n, 20) for n in numbers20])
        print(f"VAT at 20%: {vat20_sum}")
 
        total_vat += vat20_sum
        vat_check += sum(numbers20)*0.2

    if vat5:
        numbers5 = [float(l) for l in numbers5]
        vat5_sum = sum([calc_vat(n, 5) for n in numbers5])
        print(f"VAT at 5%: {vat5_sum}")

        total_vat += vat5_sum
        vat_check += sum(numbers5)*0.05

    #Printing the values    
    print(f"Goods Value: {inv_value - total_vat}")
    print(f"Total VAT: {total_vat}")

    if math.fabs(total_vat - vat_check) > 0.0001:
        print(f"VAT Check: {vat_check}")
    else:
        print("VAT Check: Consistent")

    print(f"Invoice Value: {inv_value}")

#TODO add restart option
    
    
if __name__ == "__main__":
    main()
    
    
