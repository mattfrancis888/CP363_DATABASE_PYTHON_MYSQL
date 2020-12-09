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
from functions import all_expertise
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

# print("No member id given:")
# rows = all_expertise(temp_cursor)
#  
# print("COLUMNS:")
# print(temp_cursor.column_names)
# print("DATA:")
#  
# for row in rows:
#     print(row)
#      
# print("")
# print("")

print("member id given:")
rows = all_expertise(temp_cursor, 1)

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
print("")
print("")