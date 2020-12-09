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
from functions import supp_key_member_count
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

rows = supp_key_member_count(temp_cursor,36)
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
conn.close()