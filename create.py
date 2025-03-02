import psycopg2
from dotenv import dotenv_values
from const import FILES_DICT

database_config = dotenv_values('.env')

conn = psycopg2.connect(
    database=database_config['DATABASE'],
    user=database_config['USER'],
    password=database_config['PASSWORD'],
    host=database_config['HOST']
)

cursor = conn.cursor()

def recursive_split(line):
    if not line:
        return []
    if '"' not in line:
        return line.strip().split(',')
    l_idx = line.index('"')
    line_properties = []
    left_properties = []
    if line[0] != '"':
        left_properties.extend(line[0: line.index(',"')].strip().split(','))
    line_properties.extend(left_properties)
    line_properties.append(line[l_idx+1: line[l_idx+1:].index('"') + l_idx + 1])
    right_properties = recursive_split(
        line[line[l_idx+1:].index('"') + l_idx + 3:] if line[l_idx+1:].index('"') + l_idx + 3 < len(line) - 1 else ''
    )
    line_properties.extend(right_properties)
    return line_properties

for file in FILES_DICT.values():
    with open(file['file'], 'r') as f:
        print('Working on {f}'.format(f=file['file']))
        cursor.execute(file['drop_table'])
        cursor.execute(file['create_table'])
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