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
from functions import column_info
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

print("Table name not provided:")
rows = column_info(temp_cursor, 'dcris')


print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")

print("Table name provided:")
rows = column_info(temp_cursor, 'dcris', 'pub')

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")
conn.close()