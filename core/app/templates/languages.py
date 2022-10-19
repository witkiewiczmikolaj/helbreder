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
        
    curl = f'''curl --request POST --url http://helbreder_url/api/endpoint --header 'Accept: application/json' --header 'Authorization: Basic " + '{button_clicked[3]}' + '{button_clicked[4]}' + "' --header 'Content-Type: application/json' --data '" + '{data_json}' '''
    
    if lang == 'Shell':
        code = curl
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
