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
from functions import member_expertise
from Connect import Connect

conn = Connect("dcris.txt")

rows = member_expertise(conn, "1", "7")

for row in rows:
    print(row)

conn.close()
