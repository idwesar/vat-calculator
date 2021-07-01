# VAT Calculator
A suite of tax calculators to make calculating net and gross figures on a variety of transactions easier when the information is not given on a receipt or invoice.


## The Basics
### The Reverse VAT Calculator
For when you have gross figures and need to calculate the net. Simple and functional, works for one VAT value at a time.
#### How to use:
 - input numbers as a list where directed in the code
 - input the desired VAT you wish to calculate

### The VAT Calculator
For when you have net figures and need to calculate the gross. Simple and functional, works for one VAT value at a time.
#### How to use:
 - input numbers as a list where directed in the code
 - input the desired VAT you wish to calculate


## The Others
### The Multiple VAT Calculator
Designed to tackle both standard 20% VAT and reduced 5% VAT, using the input function to recieve its data.  Written after a few months of learning Python in order to familiarise myself with inputs and input sanitisation. More complex than the Basic calculators, works for both 20 and 5% tax at the same time. Slower than the Basics if you need to do multiple calculations.
#### How to use:
 - When prompted, input the invoice/receipt total (including VAT)
 - When prompted, input all the values subject to 20% VAT separated by a comma and a space (', '). If there are no values subject to 20% VAT, type 'none'.
 - When prompted, input all the values subject to 5% VAT separated by a comma and a space (', '). If there are no values subject to 5% VAT, type 'none'.

### The Original
The first self-directed code project I did after a month of learning Python. This project was created to speed up a regular task at work and has since saved me hours of manual calculation!
#### How to use:
 - Edit 'inv_value; to store the total value of the invoice/receipt
 - Edit 'numbers' to store a list of the values subject to 20% VAT
