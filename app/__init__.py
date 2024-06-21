import os
from flask import Flask, render_template, g, current_app, redirect, request

def create_app(test_config=None):
    """
    Create and configure the app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    lang = 'en'

   # create the pages
    @app.route("/")
    def index():
        print(request.accept_languages)
        return redirect('/{}/home'.format(lang))
    
    @app.route("/<lang>/home")
    def home(lang):
        return render_template('{}/home.html'.format(lang))
    
    @app.route("/<lang>/privacy")
    def privacy(lang):
        return render_template('{}/privacy.html'.format(lang))
        
    return app
