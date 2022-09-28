import re

from templates.psql import *

def get_lang_sql():
    cur.execute('''SELECT name FROM LANGUAGES''')
    lang = cur.fetchall()
    languages = []
    for i in range (len(lang)):
        languages.append(''.join(lang[i]))
    return languages

def create_table(table_name, columns):
    columns = re.sub(r"'|:|{|}", "", str(columns))
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns})")
    c.commit()
    c.close()
