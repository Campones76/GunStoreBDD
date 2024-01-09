from flask import Blueprint, render_template

sobre_page = Blueprint('sobre', __name__)

@sobre_page.route('/sobre')
def sobre():
    return render_template('sobre.html')
