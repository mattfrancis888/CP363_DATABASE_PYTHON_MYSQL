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
from Connect import Connect
conn = Connect("dcris.txt")
def keyword_table(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the keyword table.
    Use: rows = keyword_table(cursor)
    Use: rows = keyword_table(cursor, keyword_id=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the contents of the keyword table;
        the entire table if keyword_id is None, else the row
        matching keyword_id (list of ?)
    -------------------------------------------------------
    """
   
    if keyword_id == None:
        sql = "SELECT * FROM keyword"
        params = []
    else:
        sql = "SELECT * FROM keyword WHERE keyword_id = %s"
        params = [keyword_id]
        
    conn.cursor.execute(sql, params)
    print("COLUMNS:")
    print(conn.cursor.column_names)
    print("DATA:")
    rows = conn.cursor.fetchall()
    return rows
    
    
def pub_table(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_table(cursor)
    Use: rows = pub_table(cursor, member_id=v1)
    Use: rows = pub_table(cursor, pub_type_id=v2)
    Use: rows = pub_table(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with the contents of the pub table;
            the entire table if member_id and pub_type_id are None,
        else
            rows matching member_id and pub_type_id if given
        (list of ?)
    -------
    """
    if member_id == None and pub_type_id == None:
        sql = "SELECT * FROM pub"
        params = []
    elif member_id == None:
        sql = "SELECT * FROM pub WHERE pub_type_id = %s"
        params = [pub_type_id]
    elif pub_type_id == None:
        sql = "SELECT * FROM pub WHERE member_id = %s"
        params = [member_id]
    else:
        sql = "SELECT * FROM pub WHERE member_id = %s AND pub_type_id = %s"
        params = [member_id, pub_type_id]
    conn.cursor.execute(sql, params)
    print("COLUMNS:")
    print(conn.cursor.column_names)
    print("DATA:")
    rows = conn.cursor.fetchall()
    return rows

def member_expertise(cursor, member_id=None, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = member_expertise(cursor)
    Use: rows = member_expertise(cursor, member_id=v1)
    Use: rows = member_expertise(cursor, keyword_id=v2)
    Use: rows = member_expertise(cursor, member_id=v1, keyword_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the last name, first name, and keyword
            description of the v_member_keyword view:
        the entire view if member_id and keyword_id are None,
            sorted by last name, first name, keyword description
        rows matching member_id if keyword_id is None:
            sorted by last name, first name, keyword description
        rows matching keyword_id if member_id is None:
            sorted by keyword description, last name, first name
        otherwise:
            rows unsorted if both member_id and keyword_id given
        (list of ?)
    -------------------------------------------------------
    """
    if member_id == None and keyword_id == None:
        sql = "SELECT * FROM v_member_keyword"
        params = []
    elif keyword_id == None:
        sql = "SELECT * FROM v_member_keyword WHERE member_id = %s"
        params = [member_id]
    elif member_id == None:
        sql = "SELECT * FROM v_member_keyword WHERE keyword_id = %s"
        params = [keyword_id]
    else:
        sql = "SELECT * FROM v_member_keyword WHERE member_id = %s AND keyword_id = %s"
        params = [member_id, keyword_id]
    conn.cursor.execute(sql, params)
    print("COLUMNS:")
    print(conn.cursor.column_names)
    print("DATA:")
    rows = conn.cursor.fetchall()
    return rows

def expertise(cursor, keyword=None, supp_key=None):
    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = expertise(cursor)
    Use: rows = expertise(cursor, keyword=v1)
    Use: rows = expertise(cursor, supp_key=v2)
    Use: rows = expertise(cursor, keyword=v1, supp_key=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword - a partial keyword description (str)
        supp_key - a partial supplementary description (str)
    Returns:
        rows - a list with the keyword and supplementary keyword descriptions
            of the v_keyword_supp_key view:
        the entire view if keyword and supp_key are None,
            sorted by keyword description, supplementary keyword description
        rows containing keyword if supp_key is None:
            sorted by keyword description, supplementary keyword description
        rows matching supp_key if keyword is None:
            sorted by supplementary keyword description, keyword description
        otherwise:
            rows sorted by keyword description, supplementary keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if keyword == None and supp_key == None:
        sql = "SELECT * FROM v_keyword_supp_key"
        params = []
    elif supp_key == None:
        sql = "SELECT * FROM v_keyword_supp_key WHERE k_desc LIKE %s"
        params = ["%" + keyword + "%"]  
    elif keyword == None:
        sql = "SELECT * FROM v_keyword_supp_key WHERE sk_desc LIKE %s"
        params = ["%" + supp_key + "%"]
    else:
        sql = "SELECT * FROM v_keyword_supp_key WHERE k_desc LIKE %s AND sk_desc LIKE %s"
        params = ["%" + keyword + "%", "%" + supp_key + "%"]
    conn.cursor.execute(sql, params)
    print("COLUMNS:")
    print(conn.cursor.column_names)
    print("DATA:")
    rows = conn.cursor.fetchall()
    return rows