from flask import Flask

#flask app variable
app=Flask(__name__)

#Routes
@app.route('/')
def home():
    return "Homepage here!"

@app.route('/about/')
def about():
    return "About content goes here!"

"""
when we run the script.py the __name__ = "__main__"
where as when we run another file by importing this script
we will see that the "__name__" = "script.py"
"""

if __name__ == "__main__" :
    app.run(debug=True)    