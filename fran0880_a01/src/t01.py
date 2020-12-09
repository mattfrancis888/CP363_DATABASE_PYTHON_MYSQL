"""
-------------------------------------------------------
Fall 2020
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880
Email:   fran0880@mylaurier.ca
__updated__ = "2020-10-18"
-------------------------------------------------------
"""
from functions import keyword_table
from Connect import Connect

conn = Connect("dcris.txt")

rows = keyword_table(conn, "7")

for row in rows:
    print(row)

conn.close()
