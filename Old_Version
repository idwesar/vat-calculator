##old version, 20% VAT only

def calc_vat(n):
    return n*0.2

import math

inv_value = 115.18

numbers = [0.75, 2, 1, 1, 6, 4.50, 3.75, 6, 1]
numbers = [float(l) for l in numbers]

vat_value = [calc_vat(n) for n in numbers]
total_vat = sum(vat_value)

gross_total = sum(numbers)
vat_check = gross_total * 0.2

print(f"Goods Value: {inv_value - total_vat}")

print(f"Total VAT: {total_vat}")

if math.fabs(total_vat - vat_check) > 0.0001:
    print(f"VAT Check: {vat_check}")
else:
    print("VAT Check: Consistent")

print(f"Invoice Value: {inv_value}")
print("FYI, the Tesco VAT number is 220430231")



