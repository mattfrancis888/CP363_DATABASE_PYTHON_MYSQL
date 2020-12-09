"""
-------------------------------------------------------
Fall 2020
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880
Email:   fran0880@mylaurier.ca
__updated__ = "2020-11-14"
-------------------------------------------------------
"""

from functions import constraint_info
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

print("Constraint type not provided:")
rows = constraint_info(temp_cursor,'dcris')


print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")


print("Constraint type provided:")
rows = constraint_info(temp_cursor,'dcris', 'FOREIGN KEY')
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
conn.close()