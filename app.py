from flask import Flask, request, render_template
from cleaned_text import clean_text  # import your function from cleaner.py

app = Flask(__name__)

# (Optional) Put the cleaning code as string for display:
cleaning_code = '''
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\S+@\S+', ' ', text)

    def strip_www_and_tld(match):
        url = match.group()
        url = re.sub(r'^www\.', '', url)  
        url = re.sub(r'\.(com|org|net|edu|gov|in|co|io|info|biz|us|uk|au)$', '', url) 
        return url.split('.')[0]  

    text = re.sub(r'\\b(?:https?://)?(?:www\.)?\w+\.(?:com|org|net|edu|gov|in|co|io|info|biz|us|uk|au)\\b', strip_www_and_tld, text)
    text = re.sub(r'\\b(?:https?://\S*|www\.\S*|www\\b)\\b', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\\bvar\\b\s*\w*\s*=?\s*\d*;', ' ', text)
    text = re.sub(r'&\w+;', ' ', text)
    text = re.sub(r'\\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\\b', ' ', text)
    text = re.sub(r'([!?.#\-])\\1{1,}', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.!?\\'"-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
    '''

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    cleaned_text = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        cleaned_text = clean_text(input_text)
    return render_template('index.html',
                           input_text=input_text,
                           cleaned_text=cleaned_text,
                           cleaning_code=cleaning_code)

if __name__ == '__main__':
    app.run(debug=True)
