# 🔢 Number Base & Gray Code Converter

A web-based tool built with **Python and Flask** to perform number system conversions and generate Gray Code tables.
Developed as a final project for the Computer Architecture course ("ECO").

**Developed by:** [Tiago Pereira](https://github.com/TiagoPereira001), Caio Dias, and Mário Eduardo.

## 🚀 Project Overview

This application provides a web interface to visualize and compute conversions between different number systems used in digital electronics. Unlike simple wrappers, the conversion algorithms are **implemented manually** to demonstrate the underlying mathematical logic.

### Key Features
* **Decimal to Binary:** Converts integers to binary strings with optional bit-width padding.
* **Decimal to Hexadecimal:** Custom implementation using modulo operators to map values to `0-9` and `A-F`.
* **Hexadecimal to Decimal:** Parses hex strings back to integer values.
* **Gray Code Generator:** Generates a complete truth table for $N$ bits, showing the relationship between Decimal, Binary, Gray Code, and Hexadecimal values.

## 💻 Technical Implementation

* **Backend:** Python 3 (Flask Framework).
* **Frontend:** HTML5, CSS3, Jinja2 Templating.
* **Algorithmic Highlights:**
    * **Gray Code Logic:** Implemented using bitwise XOR operations: `gray = i ^ (i >> 1)`.
    * **Manual Conversion:** Uses `while` loops and modulus math (`%`) instead of relying solely on Python's built-in `bin()` or `hex()` functions to demonstrate algorithmic understanding.

## 📂 Project Structure

The project follows the standard Flask application structure:

```text
├── app.py                  # Main application controller and logic
├── templates/              # HTML templates
│   ├── index.html          # Main Menu
│   ├── tabela_de_gray.html # Input form for Gray Code
│   └── resultado_*.html    # Result display pages
├── static/
│   └── css/
│       └── estilos.css     # Styling for the application
└── README.md
