from tableauhyperapi import *

def build_hyper(forhyper, extract_table, hypername):
    '''Takes nested list and inserts into .hyper file based on extract_table structure.'''
    
    print("Adding data to Hyper...")
    
    filename = hypername + ".hyper"

    # starts hyper process
    with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
        with Connection(endpoint=hyper.endpoint,
                        database=filename,
                        create_mode=CreateMode.CREATE_AND_REPLACE) as connection:
            connection.catalog.create_table(extract_table)

            # inserts into extract
            with Inserter(connection, extract_table) as inserter:
                inserter.add_rows(forhyper)
                inserter.execute()


def build_table(apikeys):
    '''This function intakes the formatted information from the RESTful source and builds matching tables in hyper'''

    sqlbig_int = SqlType.big_int()
    sqlbool = SqlType.bool()
    sqlbytes = SqlType.bytes()
    # sqlchar = SqlType.char()
    sqldate = SqlType.date()
    sqldouble = SqlType.double()
    sqlgeography = SqlType.geography()
    sqlint = SqlType.int()
    sqlinterval = SqlType.interval()
    sqljson = SqlType.json()
    # sqlnumeric = SqlType.numeric()
    sqloid = SqlType.oid()
    sqlsmallint = SqlType.small_int()
    sqltext = SqlType.text()
    sqltimestamp = SqlType.timestamp()
    sqltimestamp_tz = SqlType.timestamp_tz()
    # sqlvarchar = SqlType.varchar()

    sqltypes = [sqlbig_int, sqlbool, sqlbytes, sqldate, sqldouble, sqlgeography, sqlint, sqlinterval, 
        sqljson, sqloid, sqlsmallint, sqltext, sqltimestamp, sqltimestamp_tz]
        # missing char, numeric, and varchar because of argument stuff I can't figure out yet :)

    #create table
    extract_table = TableDefinition(
        table_name=TableName(apikeys['tablename'])
    )
    
    fieldlist = apikeys['fields']
    
    #add base columns
    for field in fieldlist:
        for sqltype in sqltypes:
            lowersql = str(sqltype).lower()
            if field[2] == lowersql:
                field[2] = sqltype
        column = TableDefinition.Column(field[1],field[2])
        extract_table.add_column(column)

    return extract_table