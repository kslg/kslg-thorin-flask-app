# We can "import os" from the standard Python library
import os
# Import JSON Library
import json
# we need to do is to import the Flask class.
# The capital F indicates that it's a class name,
# so it's important to use a uppercase F here.
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# In Flask, the convention is that our variable is called 'app'.
# Since we're just using a single module, we can use __name__
# which is a built-in Python variable.
# The first argument of the Flask class,
# is the name of the application's module - our package.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# We use the route decorator to tell Flask what
# URL should trigger the function that follows.
# In Python, a decorator starts with the
# @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.

# Create render template functions to route the html pages.
# Make sure that 2 blank lines separate each
# function to keep it PEP8 compliant.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# if name is equal to "main" (both wrapped in double underscores),
# then we're going to run our app with the following arguments.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
