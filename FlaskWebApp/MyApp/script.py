from flask import Flask,render_template
"""
We use render template method of flask to create html content
To use the render template we need to have the html files in a "templates" folder
in the same folder as script.py

"""
#flask app variable
app=Flask(__name__)


#Routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

"""
when we run the script.py the __name__ = "__main__"
where as when we run another file by importing this script
we will see that the "__name__" = "script.py"
"""

if __name__ == "__main__" :
    app.run(debug=True)    