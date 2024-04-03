import psycopg2
from psycopg2 import sql


def connect_to_db(host, port, dbname, user, password):
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    return conn


def insert_data(conn, table, data):
    cursor = conn.cursor()
    query = sql.SQL("INSERT INTO {} VALUES (%s, %s)").format(sql.Identifier(table))
    for row in data:
        cursor.execute(query, (row['column1'], row['column2']))
    conn.commit()
    cursor.close()
