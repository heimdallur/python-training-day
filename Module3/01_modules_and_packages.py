# In this section we will:
# What are modules and packages
# Installing a packages
# Creating a module
# Importing your module
# Using your module
# Alias a module
# API Demo

import module_demo as md
from module_demo import add_4
import modules.another_module as am


print(md.add_2(10))
print(am.myfunction(10))
print(add_4(20))