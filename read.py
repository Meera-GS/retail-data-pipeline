import pandas as pd

from util import get_connection

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details('SOURCE_DB')

    connection = get_connection(db_type= SOURCE_DB['DB_TYPE'],
                                db_type= SOURCE_DB['DB_HOST'],
                                db_type= SOURCE_DB['DB_NAME'],
                                db_type= SOURCE_DB['DB_USER'],
                                db_type= SOURCE_DB['DB_PASS'])
    cursor = connection.cursor()
    if limit == 0:
        query = f'select * from {table_name}'
    else:
        query = f'select * from {table_name} LIMIT {limit}'
    cursor.execute(query)

    df = pd.DataFrame(cursor.fetchall())
    df.columns = cursor.column_names

    connection.close()