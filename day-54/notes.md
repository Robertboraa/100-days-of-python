# Day 54 — Introduction to Flask & Decorators

## Topics Covered
- Python decorators — how they wrap functions to add behaviour without modifying them
- The `@` syntax and how it works under the hood
- Introduction to Flask — a lightweight Python web framework
- How Flask uses decorators (`@app.route`) to map URLs to functions
- Running a basic Flask development server

## Key Concepts

### Decorators
```python
def decorator(func):
    def wrapper():
        # code before
        func()
        # code after
    return wrapper

@decorator
def my_function():
    pass
```

### Flask Hello World
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```
