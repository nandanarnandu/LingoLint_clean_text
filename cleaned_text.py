import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', ' ', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', ' ', text)
    
    # Remove variable/script-like patterns (optional)
    text = re.sub(r'\bvar\b\s*\w*\s*=?\s*\d*;', ' ', text)
    
    # Remove HTML entities like &amp;, &lt;, &gt;
    text = re.sub(r'&\w+;', ' ', text)
    
    # Remove phone numbers (simple pattern)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', ' ', text)
    
    # Remove repeated punctuation sequences of length 2 or more, e.g. --- !!! ... ###
    text = re.sub(r'([!?.#\-])\1{1,}', ' ', text)
    
    # Remove any remaining special characters except basic punctuation and alphanumeric
    text = re.sub(r'[^a-zA-Z0-9\s,.!?\'"-]', ' ', text)
    
    # Replace multiple whitespace with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing spaces
    text = text.strip()
    
    return text


