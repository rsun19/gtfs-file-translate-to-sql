import psycopg2
from dotenv import dotenv_values
from const import FILES_DICT
from createUtils import recursive_split

database_config = dotenv_values('.env.local')

conn = psycopg2.connect(
    database=database_config['DATABASE'],
    user=database_config['USER'],
    password=database_config['PASSWORD'],
    host=database_config['HOST']
)

cursor = conn.cursor()

for file in FILES_DICT.values():
    with open(file['file'], 'r') as f:
        print('Working on {f}'.format(f=file['file']))
        cursor.execute(file['drop_table'])
        cursor.execute(file['create_table'])
        f.readline()
        for line in f:
            line_properties = []
            line_properties = recursive_split(line)
            cursor.execute(
                file['insert_command'],
                tuple(line_properties)
            )
        f.close()

conn.commit()
cursor.close()
conn.close()