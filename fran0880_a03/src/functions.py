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
def pub_counts_all(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the numbers of publications of each type. Name these
            three fields "articles", "papers", and "books".
        If member_id is None
            returns numbers of publications for all members
        Otherwise
            returns numbers of publications for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """ 
    if (member_id == None):
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "a") AS Articles,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "p") AS Papers,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "b") AS Books
                FROM member AS m 
                ORDER BY last_name, first_name
             """
        params = []
        cursor.execute(sql, params)
    else: 
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "a") AS Articles,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "p") AS Papers,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "b") AS Books
                FROM member AS m 
                WHERE m.member_id = %s
                ORDER BY last_name, first_name
             """
        params = [member_id]
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def expertise_count(cursor, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(cursor)
    Use: rows = expertise_count(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the number of keywords and supplementary keywords
            for the member. Name these fields "keywords" and "supp_keys".
        If member_id is None
            returns numbers of expertises for all members
        Otherwise
            returns numbers of expertises for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """
    if (member_id == None):
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = m.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = m.member_id) AS supp_keys
                FROM member AS m 
                ORDER BY last_name, first_name
             """
        params = []
        cursor.execute(sql, params)

    else: 
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = m.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = m.member_id) AS supp_keys
                FROM member AS m 
                WHERE m.member_id = %s
                ORDER BY last_name, first_name
             """
        params = [member_id]
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def keyword_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(cursor)
    Use: rows = keyword_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
            supplementary keywords that belong to it. Name the second field
            "supp_key_count".
        If keyword_id is None
            returns numbers of supplementary keywords for all keywords
        Otherwise
            returns numbers of supplementary keywords for the keyword matching
                keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if (keyword_id == None):
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = k.keyword_id) AS supp_keys
                FROM keyword AS k 
                ORDER BY k_desc
             """
             
#        Simmilar to:   sql = """SELECT
#                 k_desc,
#                 (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = k.keyword_id) AS supp_keys
#                 FROM keyword AS k 
#                 ORDER BY k_desc
#              """
        params = []
        cursor.execute(sql, params)

    else: 
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = k.keyword_id) AS supp_keys
                FROM keyword AS k 
                WHERE keyword_id = %s
                ORDER BY k_desc
             """
        params = [keyword_id]
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def keyword_member_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(cursor)
    Use: rows = keyword_member_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword description and the number of members
            that have it. Name the second field "member_count".
        If keyword_id is None
            returns numbers of members for all keywords
        Otherwise
            returns numbers of members for the keyword matching keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if (keyword_id == None):
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = k.keyword_id) AS member_count
                FROM keyword AS k 
                ORDER BY k_desc
             """
        params = []
        cursor.execute(sql, params)
    else: 
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = k.keyword_id) AS member_count
                FROM keyword AS k 
                WHERE keyword_id = %s
                ORDER BY k_desc
             """
        params = [keyword_id]
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def supp_key_member_count(cursor, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(cursor)
    Use: rows = supp_key_member_count(cursor, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
            keyword description, and the number of members that have that
            supplementary expertise. Name the last field "member_count".
        If supp_key_id is None
            returns numbers of members for all supplementary keywords
        Otherwise
            returns numbers of members for the supplementary keyword
            matching supp_key_id
        Sorted by keyword description and then supplementary keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if (supp_key_id == None):
        sql = """
        SELECT k.k_desc , sk_desc,
            (SELECT COUNT(mk.member_id)
            FROM member_supp_key AS mk
            WHERE sk.supp_key_id = mk.supp_key_id) AS member_count
            FROM keyword AS k
            INNER JOIN supp_key AS sk
            ON sk.keyword_id = k.keyword_id
            ORDER BY k.k_desc, sk_desc
        """
        params = []
        cursor.execute(sql, params)
    else: 
        sql = """
        SELECT k.k_desc , sk_desc,
            (SELECT COUNT(mk.member_id)
            FROM member_supp_key AS mk
            WHERE sk.supp_key_id = mk.supp_key_id) AS member_count
            FROM keyword AS k
            INNER JOIN supp_key AS sk
            ON sk.keyword_id = k.keyword_id
            WHERE sk.supp_key_id = %s
            ORDER BY k.k_desc, sk_desc
             """
        params = [supp_key_id]
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows