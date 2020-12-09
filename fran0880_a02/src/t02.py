"""
-------------------------------------------------------
Fall 2020
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880
Email:   fran0880@mylaurier.ca
__updated__ = "2020-11-01"
-------------------------------------------------------
"""

from functions import pub_counts
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

print("Only member id given:")
rows = pub_counts(temp_cursor, 33)

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")

print("member id and pub_type_id given:")
rows = pub_counts(temp_cursor, 3, 'b')

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")

# conn.close()