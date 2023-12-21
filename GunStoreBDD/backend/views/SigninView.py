from flask import Blueprint, render_template

signin_bp = Blueprint('SigninView', __name__)

@signin_bp.route('/login', methods=['POST'])
def login():
    # Handle signin
    pass