from templates.psql import *

def get_lang_sql():

    cur.execute('''SELECT name FROM LANGUAGES''')
    lang = cur.fetchall()
    languages = []
    for i in range (len(lang)):
        languages.append(''.join(lang[i]))
    return languages
    