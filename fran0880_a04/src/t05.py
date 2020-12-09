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
from functions import key_info
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

#rows = key_info(temp_cursor,'dcris', None, None)
#rows = key_info(temp_cursor,'dcris', None , 'keyword')
#rows = key_info(temp_cursor,'dcris', 'member', None)
print("table name and ref table name provided:")
rows = key_info(temp_cursor,'dcris', 'pub', 'member')
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
conn.close()