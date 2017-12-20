from flask import render_template, Blueprint, request

blueprint = Blueprint('pages', __name__)


################
#### routes ####
################


@blueprint.route('/')
def home():
    return render_template('pages/home.html')


@blueprint.route('/about')
def about():
    return render_template('pages/about.html')
