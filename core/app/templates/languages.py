import json
from templates.curl_to_code import *
from templates.sql import *
from templates.post import button_clicked

def lang_gen(lang):
    data = {}

    if button_clicked[0] == "Kubernetes":
        data['namespace'] = button_clicked[0]
        data['action'] = button_clicked[1]
        data['target_name'] = button_clicked[5]
        data['target_kind'] = button_clicked[2]
        data_json = json.dumps(data)
    else:
        data['action'] = button_clicked[1]
        data['target_name'] = button_clicked[5]
        data['target_kind'] = button_clicked[2]
        data_json = json.dumps(data)
        
    helbreder_url = 'helbreder.online' #this should be parametrized in the future, ideally as an input from user
    curl = f'''curl -X POST -H "Content-Type: application/json" -d '{str(data_json)}' http://{button_clicked[3]}:{button_clicked[4]}@{helbreder_url}/api/{button_clicked[0]}'''
    
    if lang == 'shell':
        code = f'''curl    -X POST \n\t -H "Content-Type: application/json" \n\t -d '{str(data_json)}' http://{button_clicked[3]}:{button_clicked[4]}@{helbreder_url}/api/{button_clicked[0]}'''
    else:
        code = curl_to_code(curl, lang.lower())
    
    return code

def lang_buttonized():
    try:
        languages = get_lang_sql()
    except psycopg2.errors.UndefinedTable:
        cur.execute("ROLLBACK")
        create_table(table_name='LANGUAGES', columns={"id": "int", "name": "varchar(255)"})
        languages = get_lang_sql()
        print('Helbreder started with an empty languages table, please fill it in.')  

    langs = []
    for lang in languages:
        langs.append('<button class="language_logo" id="' + lang.lower() + '_butt" type="button" value="' + lang + '"><img src="../static/images/' + lang.lower() + '.png"/></button>')
    langs = ' '.join(langs)    
    return langs
