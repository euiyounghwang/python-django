
# --
# Common ES Utils

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