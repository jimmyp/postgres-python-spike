import psycopg2


try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')

    conn = psycopg2.connect(
        "host=db dbname=postgres user=postgres password=postgres")

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

    # close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
