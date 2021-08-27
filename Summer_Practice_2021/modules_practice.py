import converters
print(converters.kg_to_lbs(170))
from converters import kg_to_lbs
print(kg_to_lbs(170))

import utils
numbers = [2, 34, 432, 32, 123, 3]
maximum = utils.find_max(numbers)
print(maximum)

# package is way to organize modules
import ecommerce.shipping
ecommerce.shipping.calc_shpping()
# or
from ecommerce.shipping import calc_shpping
calc_shpping()
