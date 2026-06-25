# call entire function

import calci
print(calci.add(10,20))
print(calci.sub(10,40))

# call limited functions

from calci import add
print(add(10,20))
from calci import sub
print(sub(10,40))
    