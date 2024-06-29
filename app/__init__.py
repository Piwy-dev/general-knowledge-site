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
    
    @app.route("/privacy")
    def privacy_redirect():
        return redirect('/{}/privacy'.format(lang))
    
    @app.route("/<lang>/privacy")
    def privacy(lang):
        return render_template('{}/privacy.html'.format(lang))
    
    @app.route("/terms")
    def terms_redirect():
        return redirect('/{}/terms'.format(lang))
    
    @app.route("/<lang>/terms")
    def terms(lang):
        return render_template('{}/terms.html'.format(lang))
    
    @app.route("/suppression-request")
    def suppression_request_redirect():
        return redirect('/{}/suppression-request'.format(lang))
    
    @app.route("/<lang>/suppression-request")
    def suppression_request(lang):
        return render_template('{}/suppression-request.html'.format(lang))
        
    return app
