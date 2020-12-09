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
from functions import publications
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

# print("No title and pub_type_id given:")
# rows = publications(temp_cursor)
# print("COLUMNS:")
# print(temp_cursor.column_names)
# print("DATA:")
# for row in rows:
#     print(row)
#     
# print("")
# print("")
# 
# 
# print("Partial-title only given:")
# rows = publications(temp_cursor, 'ada')
# print("COLUMNS:")
# print(temp_cursor.column_names)
# print("DATA:")
# for row in rows:
#     print(row)
#     
# print("")
# print("")
# 
# print("id only given:")
# rows = publications(temp_cursor, None, 'b')
# print("COLUMNS:")
# print(temp_cursor.column_names)
# print("DATA:")
# for row in rows:
#     print(row)
#     
# print("")
# print("")



print("Title and pub_type_id given:")
rows = publications(temp_cursor, 'ada', 'b')

print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)

conn.close()