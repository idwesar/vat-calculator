import math
def calc_vat20(n):
    return n*0.2
def calc_vat5(x):
    return x*0.05

#Values to input
inv_value = 10
numbers20 = [1]
numbers5 = [1, 1, 0.5]

#checking which VAT values to run
if len(numbers20) == 0:
    vat20 = False
else:
    vat20 = True

if len(numbers5) == 0:
    vat5 = False
else:
    vat5 = True
    
#calculating
if vat20: 
    numbers20 = [float(l) for l in numbers20]
    vat20_value = [calc_vat20(n) for n in numbers20]
    vat20_sum = sum(vat20_value)
    print(f"VAT at 20%: {vat20_sum}")
    if vat5 == False:
        total_vat = vat20_sum
        net_total = sum(numbers20)
        vat_check = net_total*0.2
    
if vat5:
    numbers5 = [float(l) for l in numbers5]
    vat5_value = [calc_vat5(n) for n in numbers5]
    vat5_sum = sum(vat5_value)
    print(f"VAT at 5%: {vat5_sum}")
    if vat20 == False:
        total_vat = vat5_sum
        net_total = sum(numbers5)
        vat_check = net_total*0.05
                    
if vat20 and vat5:
    total_vat = vat20_sum + vat5_sum
    net_total = sum(numbers20) + sum(numbers5)
    vat_check = (sum(numbers20)*0.2) + (sum(numbers5)*0.05)

#Printing the values    
print(f"Goods Value: {inv_value - total_vat}")
print(f"Total VAT: {total_vat}")

if math.fabs(total_vat - vat_check) > 0.0001:
    print(f"VAT Check: {vat_check}")
else:
    print("VAT Check: Consistent")

print(f"Invoice Value: {inv_value}")
if vat20 and vat5 == False:
    print("FYI, the Tesco VAT number is 220430231")


