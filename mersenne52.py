# Largest Known Prime Number (Mersenne 52)
# More information at https://www.mersenne.org/
# More information at https://t5k.org/largest.html#references

import sys
sys.set_int_max_str_digits(41024321) # WARNING: MAKE SURE THERE IS ENOUGH MEMORY

print("Max string digits: ", sys.get_int_max_str_digits())

print("!START OF MERSENNE 52!")
mersenne52 = (2 ** 136279841) - 1
strM52 = str(mersenne52)
print(strM52)

print("!END OF MERSENNE 52!")
print("Digits printed: ", len(strM52))

