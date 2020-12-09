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
def publications(cursor, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = publications(cursor)
    Use: rows = publications(cursor, title=v1)
    Use: rows = publications(cursor, pub_type_id=v2)
    Use: rows = publications(cursor, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a')
        If title and pub_type_id are None
            returns the entire table
        If partial title and/or pub_type are given
            returns only matching results
        Rows sorted by last name, first name, title
        (list of ?)
    -------------------------------------------------------
    """
    if(title == None and pub_type_id == None):
        sql = "SELECT * FROM pub"
        parameter = []
    elif (title == None):
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc FROM pub AS p
                 JOIN member AS m ON m.member_id = p.member_id
                 JOIN pub_type AS pt ON pt.pub_type_id = p.pub_type_id
                 WHERE p.pub_type_id = %s 
                 ORDER BY m.last_name, m.first_name, p.p_title
              """
        parameter = [pub_type_id]
    elif (pub_type_id == None):
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc 
                 FROM pub AS p JOIN member AS m 
                 ON m.member_id = p.member_id
                 JOIN pub_type AS pt 
                 ON pt.pub_type_id = p.pub_type_id
                 WHERE p.p_title LIKE %s
                 ORDER BY m.last_name, m.first_name, p.p_title
              """  
        parameter = ["%" + title + "%"]
    else: 
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc 
                 FROM pub AS p JOIN  member AS m ON m.member_id = p.member_id
                 JOIN pub_type AS pt ON pt.pub_type_id = p.pub_type_id
                 WHERE p.p_title LIKE %s AND pt.pub_type_id = %s
                 ORDER BY m.last_name, m.first_name, p.p_title
             """
        parameter = ["%" + title + "%", pub_type_id]
    cursor.execute(sql, parameter)
    rows = cursor.fetchall()   
    return rows

def pub_counts(cursor, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor, member_id=v1)
    Use: rows = pub_counts(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the number of publications of type pub_type
        If pub_type_id is None
            returns the count of all their publications
        otherwise
            returns the count of publications of type pub_type_id
        (list of ?)
    -------------------------------------------------------
    """
    if (pub_type_id == None):
        sql = """SELECT p.member_id, m.last_name, m.first_name, COUNT(p.pub_type_id) AS total_of_publications
                 FROM pub AS p INNER JOIN member AS m ON p.member_id = m.member_id 
                 WHERE m.member_id = %s GROUP BY p.member_id
              """
        parameter = [member_id]
    else:
        sql = """SELECT p.member_id, m.last_name, m.first_name, COUNT(p.pub_type_id) AS total_of_publications
                 FROM pub AS p INNER JOIN member AS m ON p.member_id = m.member_id 
                 WHERE m.member_id = %s AND p.pub_type_id = %s  GROUP BY p.member_id
              """
        parameter = [member_id, pub_type_id]
    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    return rows

def member_expertise_count(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member and keyword tables.
    Use: rows = member_expertise_count(cursor)
    Use: rows = member_expertise_count(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the count of the number of expertises (i.e. keywords)
            they hold 
        If member_id is None
            returns the keyword count for all members
        otherwise
            returns the keyword count for the member matching member_id
        Sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """
    if (member_id == None):
        sql = """SELECT m.last_name, m.first_name, count(k.k_desc) AS keyword_count FROM member AS m 
                 INNER JOIN member_keyword AS mk 
                 ON m.member_id = mk.member_id  
                 INNER JOIN keyword AS k 
                 ON mk.keyword_id = k.keyword_id
                GROUP BY m.last_name, m.first_name
                 ORDER BY m.last_name, m.first_name
              """
        parameter = []
    else:     
        sql = """SELECT m.last_name, m.first_name, count(k.k_desc) AS keyword_count
                 FROM member AS m INNER JOIN member_keyword AS mk
                    ON m.member_id = mk.member_id  
                    INNER JOIN keyword AS k 
                    ON mk.keyword_id = k.keyword_id
                    WHERE m.member_id = %s
                    GROUP BY m.last_name, m.first_name
                    ORDER BY m.last_name, m.first_name
              """
        parameter = [member_id]
    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    return rows

def all_expertise(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member, keyword, and supp_key tables
    Use: rows = all_expertise(cursor)
    Use: rows = all_expertise(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, a keyword description, and a supplementary keyword description
        If member_id is None
            returns descriptions for all members
        Otherwise
            returns descriptions for the member matching member_id
        Sorted by last_name, first_name, keyword description, supplementary
                keyword description
        (list of ?)
    ------------
"""
    if (member_id == None):
        sql = """SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc  FROM member AS m INNER JOIN member_keyword AS mk 
                 ON m.member_id = mk.member_id INNER JOIN keyword AS k 
                 ON mk.keyword_id = k.keyword_id INNER JOIN supp_key AS sk 
                 ON k.keyword_id = sk.keyword_id
                 ORDER BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
              """
        parameter = []
    else:
        sql = """SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc 
                 FROM member AS m INNER JOIN member_keyword AS mk 
                 ON m.member_id = mk.member_id INNER JOIN keyword AS k 
                 ON mk.keyword_id = k.keyword_id INNER JOIN supp_key AS sk 
                 ON k.keyword_id = sk.keyword_id
                 WHERE m.member_id = %s
                 ORDER BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
              """
        parameter = [member_id]
    cursor.execute(sql, parameter)
    rows = cursor.fetchall()
    return rows