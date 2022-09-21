from templates.psql import *
from templates.sql import *

def save_api_request(user_name, module, data):
    cur.execute(f'''INSERT INTO LOGS(TIME_STAMP, USER, MODULE, DATA) VALUES(current_timestamp, {user_name}, '{module}', '{data}')''')
    c.commit()

create_table(table_name='LOGS', columns={"TIME_STAMP": "TIMESTAMP", "USER": "TEXT", "MODULE": "TEXT", "DATA": "JSONB"})
