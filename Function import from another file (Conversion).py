import functions

addition = functions.add(1,2,5,8,7,8,7,8,4)
print(addition)

division = functions.division(98, 36)
print(division)

multiplying = functions.multiply(1,5,6,8,2)
print(multiplying)

substuction = functions.subs(944, 322)
print(substuction)

import functions
from functions import multiply

usd = 222
rate = 128.13
bdt = multiply(usd, rate)
print(usd, 'usd is equal to:', bdt, 'bdt')

from functions import division as divi
result = divi(25, 3)
print(result)