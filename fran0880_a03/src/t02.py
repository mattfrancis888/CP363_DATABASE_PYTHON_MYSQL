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
from functions import expertise_count
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

rows = expertise_count(temp_cursor, 1)
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)

conn.close()