from flask import Blueprint, render_template
from .forms import RegistrationForm

signup_bp = Blueprint('SignupView', __name__)

@signup_bp.route('/register', methods=['POST'])
def register():
    # Handle signup
    form = RegistrationForm()
    return render_template('signup.html', form=form)