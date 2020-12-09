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
from functions import table_info
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

print("Table name not provided:")
rows = table_info(temp_cursor, 'dcris', None)

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)

print("")
print("")

print("Table name provided")
rows = table_info(temp_cursor, "dcris", "keyword")
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)

print("")
print("")
conn.close()