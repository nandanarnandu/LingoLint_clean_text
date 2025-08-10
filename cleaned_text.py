import re

def clean_text(text):
    # Lowercase for consistent cleaning (optional)
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Remove email addresses first so domains are handled separately
    text = re.sub(r'\S+@\S+', ' ', text)

    # Extract words from URLs like www.mits.com and replace them with just the domain name (no www, no .com)
    def strip_www_and_tld(match):
        url = match.group()
        url = re.sub(r'^www\.', '', url)  # Remove www.
        url = re.sub(r'\.(com|org|net|edu|gov|in|co|io|info|biz|us|uk|au)$', '', url)  # Remove common TLDs
        return url.split('.')[0]  # Keep only the main domain part

    text = re.sub(r'\b(?:https?://)?(?:www\.)?\w+\.(?:com|org|net|edu|gov|in|co|io|info|biz|us|uk|au)\b', strip_www_and_tld, text)

    # Remove any leftover full URLs
    text = re.sub(r'\b(?:https?://\S*|www\.\S*|www\b)\b', ' ', text, flags=re.IGNORECASE)

    # Remove variable/script-like patterns (optional)
    text = re.sub(r'\bvar\b\s*\w*\s*=?\s*\d*;', ' ', text)

    # Remove HTML entities like &amp;, &lt;, &gt;
    text = re.sub(r'&\w+;', ' ', text)

    # Remove phone numbers (simple pattern)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', ' ', text)

    # Remove repeated punctuation sequences
    text = re.sub(r'([!?.#\-])\1{1,}', ' ', text)

    # Remove special characters except basic punctuation and alphanumeric
    text = re.sub(r'[^a-zA-Z0-9\s,.!?\'"-]', ' ', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
