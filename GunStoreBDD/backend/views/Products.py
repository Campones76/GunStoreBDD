from flask import Blueprint, render_template
products_page = Blueprint('products', __name__)

@products_page.route('/products')
def products():
    return render_template('products.html')