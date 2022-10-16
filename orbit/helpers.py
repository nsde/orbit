import json
import base64
import requests
import pandas as pd

def read_json(filename: str):
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def write_json(config, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(config, f)
    return config

def get_sidenav() -> dict:
    return read_json('sidebar.json')

def dict_to_table(input_data: dict) -> str:
    table = pd.DataFrame(data=input_data).to_html(escape=False) # XSS WARNING
    inner_table = table.split('<table border="1" class="dataframe">')[1].split('</table>')[0]
    inner_table = inner_table.replace('\n', '\n\t')

    table = f"""
    <table id="demo-table" class="stats">
        {inner_table}
    </table>
    """
    return table

def get_css(sheets):
    css = ''
    
    for sheet in sheets:
        css += f'/* {"="*20}{sheet}{"="*20} */\n'
        
        if '://' in sheet:
            css += requests.get(sheet).text.replace('\n', '')
        else:
            with open(f'orbit/static/stylesheets/{sheet}.css') as f:
                css += f.read().replace('\n', '')

        css += '\n'

    return css

def base64_source(url: str) -> str:
    data = str(base64.b64encode(requests.get(url).content))
    data = data[2:]
    return f'data:image/png;base64,{data[:-3]}'
