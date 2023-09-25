from flask import Blueprint, render_template 

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/submit')
def submit():
    return render_template('submit.html')