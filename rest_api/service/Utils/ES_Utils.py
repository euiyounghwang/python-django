
# --
# Common ES Utils

import json
import re
import sys

def transform_trim_string(to_replace):
    """
    SEARCH-323: Trim whitespace for metadata fields, permanent fix for leading space jinja bug
    Remove all whitespaces and \t
    """
    if sys.version_info[0] >= 3:
        unicode = str
#     my_string = unicode('This program resolves \u0061 "NameError" in PythØn!')
#     print(my_string)
        
    if isinstance(to_replace, (unicode, str)):
        to_replace = to_replace.strip()
        to_replace = re.sub(r'\n|\\n', ' ', to_replace)
        to_replace = re.sub(r'\t|\\t', ' ', to_replace)
        to_replace = re.sub(r'\f|\\f', ' ', to_replace)
        to_replace = re.sub(r'\s+', ' ', to_replace)

    return to_replace


def json_value_to_transform_trim(raw_json):
    def get_recursive_nested_all(d):
        if isinstance(d, list):
            for i in d:
                get_recursive_nested_all(i)
        elif isinstance(d, dict):
            for k, v in d.items():
                if not isinstance(v, (list, dict)):
                    print("%%%%", k, v)
                    d[k] = transform_trim_string(v)
                else:
                #     print('########', v)
                    get_recursive_nested_all(v)
        return d

    return get_recursive_nested_all(raw_json)


def sanitize_and_trim_text(self, text):
        # remove punctuation
        regex = r'[\$\{\}\[\]\\\|\)\(<>\+\./%\"\',\-\&\?\!=;\*#:@`~^_]|[0-9]'
        text = re.sub(regex, '', text)

        # remove newlines
        regex = r'\n'
        text = re.sub(regex, ' ', text)

        # remove duplicate spaces
        regex = r' +'
        text = re.sub(regex, ' ', text)

        return text[:2000]
    
    
def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}