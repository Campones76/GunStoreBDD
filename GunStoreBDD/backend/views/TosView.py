import sys
from flask import Flask, render_template, Blueprint

tosviewer_bp = Blueprint('TosViewer', __name__)

@tosviewer_bp.route("/tosviewer")
def tosviewer():
    return render_template("toc.html")
