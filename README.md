# Numeric methods
 Numeric methods is a package of tools for analyze functions via numeric methods

## Features
For now this project supports these features:
* One variable methods in `one_variable` module:
  * `half_method`: half division method for equation root searching

## Installation
For installing this package you can use `pip`:
```commandline
py -m pip install numeric-methods
```

## Changing language
This project supports several languages. You can also add yours. For now supports English and Russian. You can set language by using `settings.set_language`:
```Python
from numeric_methods import settings


settings.set_language("en" or "EN" or "english" or "ENGLISH")
# ^^^ Returns True
```
Please note that the default language is English and errors have no translation.

## Example of using
### Half method
```Python
from numeric_methods.one_variable import half_method


for line in half_method(lambda x: x ** 5 - 2, 1, 2, 0.001):
    print(line)

# Prints vvv
#
# (1, 1.0, 2.0, 1.5, 5.59375)
# (2, 1.0, 1.5, 1.25, 1.0517578125)
# (3, 1.0, 1.25, 1.125, -0.197967529296875)
# (4, 1.125, 1.25, 1.1875, 0.3613920211791992)
# (5, 1.125, 1.1875, 1.15625, 0.06661096215248108)
# (6, 1.125, 1.15625, 1.140625, -0.06930162664502859)
# (7, 1.140625, 1.15625, 1.1484375, -0.002269843505928293)
# (8, 1.1484375, 1.15625, 1.15234375, 0.03193706909132743)
# (9, 1.1484375, 1.15234375, 1.150390625, 0.014775536791518107)
# 1.150390625
```
