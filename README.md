# LingoLint: A Text Cleaner 🧹

**An NLP Project for Text Cleaning**

LingoLint is an efficient and simple **Flask web application** designed for basic text cleaning, a foundational task in Natural Language Processing (NLP). It helps to normalize raw text data by removing unwanted elements, making it more suitable for further analysis, processing, or simply for improved readability.

This tool is designed for writers, students, developers, and anyone who needs clean, readable text.

<img width="1069" height="819" alt="Screenshot 2025-09-07 001353" src="https://github.com/user-attachments/assets/23bea615-5321-4786-930e-b2e2eede0526" />

### ✨ Features

* **Lowercase** the input text for uniform formatting.

* **Removes HTML tags** and HTML entities.

* Strips **email addresses** entirely.

* Simplifies **URLs** by keeping only the main domain name (e.g., removing `www` and `.com` / `.org`, etc.).

* Deletes **phone numbers** (US-format: 123-456-7890).

* Removes **repeated punctuation** (e.g., `!!!` → `!`).

* Removes **JavaScript variable/script-like patterns** (e.g., `var x = 10;`).

* Keeps only **basic punctuation** (periods, commas, quotes, etc.).

* Collapses **multiple spaces** into a single space.

* **Web UI** built with TailwindCSS for a clean and responsive look.

### 🛠 Tech Stack

* **Python 3**

* **Flask** – Web framework

* **Regular Expressions (`re`)** – Text cleaning

* **TailwindCSS** – UI styling

* **HTML + Jinja2** – Templates

### 📂 Project Structure

```
LingoLint/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── tailwind.css
│   └── js/
│       └── app.js
├── venv/
└── README.md
```

### 🚀 Installation & Usage

Follow these steps to get a copy of the project up and running on your local machine.

#### Prerequisites

Make sure you have **Python 3** installed on your system.

#### Steps

1. **Clone the repository:**

   ```
   git clone https://github.com/nandanarnandu/LingoLint_clean_text.git)
   cd LingoLint
   ```

2. **Create a virtual environment** to manage project dependencies:

   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   * **On macOS/Linux:**

     ```
     source venv/bin/activate
     ```

   * **On Windows:**

     ```
     venv\Scripts\activate
     ```

4. **Install the required packages:**

   ```
   pip install Flask
   ```

5. **Run the Flask application:**

   ```
   python app.py
   ```

The application will be available at `http://127.0.0.1:5000` in your web browser.

### 👋 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).

4. Push to the Branch (`git push origin feature/AmazingFeature`).

5. Open a Pull Request.
