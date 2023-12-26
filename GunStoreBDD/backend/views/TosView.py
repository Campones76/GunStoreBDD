import sys
from flask import Flask, render_template, Blueprint

tosviewer_bp = Blueprint('TosViewer', __name__)

@tosviewer_bp.route("/tosviewer")
def tosviewer():
    # Abra o arquivo de texto no modo de leitura
    with open("TOS.txt", "r", encoding="utf-8") as f:
        # Leia o conteúdo
        content = f.read()
    # Divida o conteúdo em linhas
    lines = content.split("\n")
    # Renderize o modelo HTML com as linhas como argumento
    return render_template("tos.html", lines=lines)
