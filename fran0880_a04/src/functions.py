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

def table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = table_info(cursor, table_schema)
    Use: rows = table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, TABLE_TYPE
        (list of ?)
    -------------------------------------------------------
    """
    if table_name is None:  
        sql = """
        SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = %s
        ORDER BY TABLE_NAME, TABLE_TYPE
        """
        params = [table_schema]
    else:
        sql = """
        SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
        FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s 
        ORDER BY TABLE_NAME, TABLE_TYPE
        """
        params = [table_schema, table_name]
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = column_info(cursor, table_schema)
    Use: rows = column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if table_name is None:  
        sql = """
        SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        param = [table_schema]
    else:
        sql = """
        SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        param = [table_schema,table_name]
    cursor.execute(sql, param)
    rows = cursor.fetchall()
    return rows

def constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = constraint_info(cursor, table_schema)
    Use: rows = constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields.
        If constraint_type is None
            returns data for all constraints
        Otherwise
            returns data for constraint whose type matches constraint_type
        Sorted by CONSTRAINT_NAME, TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if constraint_type is None:
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME
        """
        params = [table_schema]
    else:
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA = %s AND CONSTRAINT_TYPE = %s
        ORDER BY CONSTRAINT_NAME, TABLE_NAME
        """
        params = [table_schema, constraint_type]
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = foreign_key_info(cursor, constraint_schema)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if (table_name is None and ref_table_name is None):
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE CONSTRAINT_SCHEMA = %s
        ORDER BY CONSTRAINT_NAME,TABLE_NAME, REFERENCED_TABLE_NAME
        """
        params = [constraint_schema]
    elif table_name is None and ref_table_name is not None:
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE CONSTRAINT_SCHEMA = %s AND REFERENCED_TABLE_NAME = %s
        ORDER BY CONSTRAINT_NAME,TABLE_NAME, REFERENCED_TABLE_NAME
        """
        params = [constraint_schema, ref_table_name]
    elif table_name is not None and ref_table_name is None:
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s
        ORDER BY CONSTRAINT_NAME,TABLE_NAME, REFERENCED_TABLE_NAME
        """
        params = [constraint_schema, table_name]
    else:
        sql = """
        SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME
        FROM information_schema.REFERENTIAL_CONSTRAINTS
        WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s AND REFERENCED_TABLE_NAME = %s
        ORDER BY CONSTRAINT_NAME,TABLE_NAME, REFERENCED_TABLE_NAME
        """
        params = [constraint_schema,table_name, ref_table_name]
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows

def key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = key_info(cursor, constraint_schema)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if (table_name is None and ref_table_name is None):
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
         WHERE CONSTRAINT_SCHEMA = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params = [constraint_schema]
    elif table_name is None and ref_table_name is not None:
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = %s AND REFERENCED_TABLE_NAME = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params = [constraint_schema, ref_table_name]
    elif table_name is not None and ref_table_name is None:
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params = [constraint_schema, table_name]
    else:
        sql = """
        SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s AND REFERENCED_TABLE_NAME = %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params = [constraint_schema, table_name, ref_table_name]
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows
