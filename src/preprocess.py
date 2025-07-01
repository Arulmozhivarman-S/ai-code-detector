import re

def clean_code(code):
    code = re.sub(r'#.*', '', code)  
    code = re.sub(r'\n\s*\n', '\n', code)  
    return code.strip()
