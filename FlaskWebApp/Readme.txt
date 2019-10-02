Flask App Introduction



Using render templates
    Inorder to use the render templates we need to have a "templates"
    folder within our flask app folder. Flask framework reads throgh 
    this folder and renders the respective htmls.

Styling the htmls
    Styling,images and various other static content must be places inside the 
    static folder of out flask app.

Creating a virtual environment
    pip install virtualenv        ---> Instalation of virtual environment module to create a venv

    create a virtual environment named "virtual"
    in the same folder we have our flask app
    --FlaskWebApp
      --MyApp                     ---> Our Flask App
        --static
        --templates
        --script.py
      --virtual                   ---
        --include                    |
        --Lib                        |   Python Virtual Environment Created using following command
        --Scripts                    |          python -m venv virtual
        --pyvenv.cfg              ---

Creating Requirements.txt
    Once done with importing then necessary modules into the newly created virtual environment.
    use "pip freeze >> requirements.txt" to get the necessary modules. For later use to set the
    web app.

Using Requirements.txt
    As we cant have the entire virtual environment in the repository we make use of requirements.txt.
    Create a new virtual environment. And install the necessary package mentioned in the requirements.
