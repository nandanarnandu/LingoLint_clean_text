# 🧹 Text Cleaner

A simple and efficient **Flask web application** for cleaning raw text by removing unwanted characters, HTML tags, email addresses, URLs, and other unnecessary elements.  
This tool is designed for writers, students, developers, and anyone who needs clean, readable text.

---

## 📌 Features

- **Lowercases** the input text for uniform formatting.
- **Removes HTML tags** and HTML entities.
- **Strips email addresses** entirely.
- **Simplifies URLs** by keeping only the main domain name (removing `www` and `.com` / `.org` etc.).
- **Deletes phone numbers** (US-format: `123-456-7890`).
- **Removes repeated punctuation** (e.g., `!!!` → `!`).
- **Removes JavaScript variable/script-like patterns** (e.g., `var x = 10;`).
- **Keeps only basic punctuation** (periods, commas, quotes, etc.).
- **Collapses multiple spaces** into a single space.
- **Web UI** built with TailwindCSS for a clean and responsive look.

---

## 🛠 Tech Stack

- **Python 3**
- **Flask** – Web framework
- **Regular Expressions (re)** – Text cleaning
- **TailwindCSS** – UI styling
- **HTML + Jinja2** – Templates

---

## 📂 Project Structure

