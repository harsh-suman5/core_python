# Python Learning & Development Projects

A collection of Python projects and learning materials covering object-oriented programming, data types, and modern development tools. This repository demonstrates core Python concepts with practical examples and a comprehensive development environment setup.

## 📁 Project Structure

### Core Python Learning Files

- **`build_in_class.py`** - Demonstrates Python's built-in data types and type checking
  - Numeric types (int, float, complex)
  - Collections (dictionaries)
  - Functions and type introspection
  
- **`project0.py`** - Object-Oriented Programming fundamentals
  - Employee class implementation
  - Class attributes and instance attributes
  - Object instantiation and method definitions
  - Dynamic attribute assignment and deletion

- **`project1.py`** - Advanced class attributes and introspection
  - Class metadata exploration (`__doc__`, `__name__`, `__module__`)
  - Class bases inspection
  - Dictionary representation of class objects

- **`garbage_collection.py`** - Python memory management (placeholder for future content)

## 🛠️ Environment Setup

The project includes a Python virtual environment (`myenv/`) with extensive dependencies for various development scenarios:

### Key Dependencies

**Core Development:**
- `python-dotenv` - Environment configuration management
- `loguru` - Advanced logging and debugging

**GUI Development:**
- `PySide6` / `PyQt5` - Modern cross-platform GUI frameworks
- `kivy` - Touch and mobile-friendly UI

**Data Science & Machine Learning:**
- `numpy` - Numerical computing
- `pandas` - Data manipulation and CSV/Excel handling
- `scikit-learn` - ML algorithms
- `imbalanced-learn` - Handle imbalanced datasets

**Deep Learning:**
- `torch` / `torchvision` - PyTorch ecosystem
- `tensorflow` - Alternative deep learning framework

**Natural Language Processing:**
- `nltk` - Text tokenization and preprocessing
- `spacy` - Named Entity Recognition and advanced NLP
- `transformers` - HuggingFace pre-trained models
- `textblob` - Sentiment analysis

**Computer Vision:**
- `opencv-python` - Image/video processing
- `pillow` - Image manipulation

**Visualization:**
- `matplotlib` - Basic plotting
- `seaborn` - Statistical visualization
- `plotly` - Interactive dashboards
- `folium` - Map visualization
- `geopandas` - Geospatial analysis

**Security:**
- `cryptography` - Encryption/decryption
- `bcrypt` - Password hashing

**Packaging:**
- `pyinstaller` / `cx_Freeze` - Create standalone executables

## 🚀 Getting Started

### Prerequisites
- Python 3.12+

### Creating the Virtual Environment

If you don't have the `myenv/` directory yet, create it using:

```bash
python -m venv myenv
```

This will create a new virtual environment directory with all necessary Python packages.

### Activation

**Windows (PowerShell):**
```powershell
.\myenv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
myenv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source myenv/bin/activate
```

### Installing Dependencies

After activating the virtual environment, install all required packages:

```bash
pip install -r requirements.txt
```

This will install all dependencies listed in `requirements.txt`, including data science, ML, NLP, and GUI frameworks.

### Running Examples

```python
# Display Python built-in types
python build_in_class.py

# Run OOP examples
python project0.py
python project1.py
```

## 📚 Learning Outcomes

- **Data Types**: Understanding Python's type system (int, float, complex, dict, functions)
- **OOP Concepts**: Classes, objects, attributes, methods, and inheritance
- **Type Introspection**: Using `type()`, `__dict__`, and other metadata attributes
- **Memory Management**: Concepts of garbage collection and object lifecycle

## 🔧 Technologies & Tools

| Category | Tools |
|----------|-------|
| Framework | Python 3.12 |
| Data Science | NumPy, Pandas, Scikit-learn |
| ML/DL | PyTorch, TensorFlow |
| NLP | NLTK, spaCy, Transformers |
| Visualization | Matplotlib, Seaborn, Plotly |
| GUI | PySide6, PyQt5 |
| Database | SQLAlchemy, Alembic |
| Security | Cryptography, bcrypt |

## 📝 Notes

- All code examples follow Python best practices
- The extensive dependency list supports future expansion into data science, ML, and GUI development
- Virtual environment is pre-configured and ready for use

## 📄 License

This project is part of a learning repository.

---

**Last Updated:** December 2025  
**Repository:** [GitHub - core_python](https://github.com/harsh-suman5/core_python)