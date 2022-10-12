# Load the runtime properties
import sys
from util import get_tables

from config import DB_DETAILS
#from read import read_table
#from write import load_table

# Load the run time properties

def main():
    env = sys.argv[1]
    db_details = DB_DETAILS[env]

    tables = get_tables('table_list')
    for table in tables["table_name"]:
        print(table)

# read the data from retail_db
'''df = read_table(db_details, 'orders', limit=10)
for i, rec in df.iterrows():
    print (rec)

# Process the data using Pandas
# Write the data to retail_dw
load_table(db_details, df)'''

if __name__ == '__main__':
    main()

