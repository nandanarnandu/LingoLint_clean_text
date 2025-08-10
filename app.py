from flask import Flask, request, render_template
from cleaned_text import clean_text  # import your function from cleaner.py

app = Flask(__name__)

# (Optional) Put the cleaning code as string for display:
cleaning_code = '''
import re

def clean_text(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'http\S+|www\S+', ' ', text)
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'\bvar\b\s*\w*\s*=?\s*\d*;', ' ', text)
    text = re.sub(r'&\w+;', ' ', text)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', ' ', text)
    text = re.sub(r'([!?.#\-])\1{1,}', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.!?\'"-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    return text
    '''
code = ' '

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    cleaned_text = ''
    show_code = False

    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        cleaned_text = clean_text(input_text)
        show_code = True

    return render_template('index.html',
                           input_text=input_text,
                           cleaned_text=cleaned_text,
                           cleaning_code=cleaning_code if show_code else code
                           )

if __name__ == '__main__':
    app.run(debug=True)
