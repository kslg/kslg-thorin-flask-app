# We can "import os" from the standard Python library
import os
# we need to do is to import the Flask class.
# The capital F indicates that it's a class name, so it's important to use a capital F here.
from flask import Flask

# In Flask, the convention is that our variable is called 'app'.
# Since we're just using a single module, we can use __name__ 
# which is a built-in Python variable.
# The first argument of the Flask class, is the name of the application's module - our package.
app = Flask(__name__)

# We use the route decorator to tell Flask what URL should trigger the function that follows.
# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.
@app.route("/")
# Create a function called "index", which just returns the string, "Hello, World".
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)