from pathlib import Path
from openpyxl import cell

# Absolute path
# Relative path 

path = Path("ecommerce")
print(path.exists())

""" path2 = Path("emails")
print(path2.mkdir()) """

""" path3 = Path("emails")
path3.rmdir() """

path4 = Path()
for file in (path4.glob('*.py')):
    print(file)