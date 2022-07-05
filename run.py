# We can "import os" from the standard Python library
import os
# we need to do is to import the Flask class.
# The capital F indicates that it's a class name, so it's important to use a uppercase F here.
from flask import Flask, render_template 

# In Flask, the convention is that our variable is called 'app'.
# Since we're just using a single module, we can use __name__ 
# which is a built-in Python variable.
# The first argument of the Flask class, is the name of the application's module - our package.
app = Flask(__name__)

# We use the route decorator to tell Flask what URL should trigger the function that follows.
# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.
@app.route("/")
# Create render template functions to route the html pages. 
# Make sure that 2 blank lines separate each function to keep it PEP8 compliant.
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# if name is equal to "main" (both wrapped in double underscores), 
# then we're going to run our app with the following arguments.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)