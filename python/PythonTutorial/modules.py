import converters
from converters import kg_to_lbs
from utils import find_max
import ecommerce.shipping
from ecommerce.shipping import calc_shipping



print(converters.kg_to_lbs(30))

print(kg_to_lbs(70))

print(find_max([1,4,7,4,6,2]))

print(max([1,2,6,5,3]))

calc_shipping()