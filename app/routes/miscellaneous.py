from flask import Blueprint, Flask, jsonify, request
from app.models import Category, Product, Banner, FeaturedProduct
from app.extensions import db, csrf
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
misc_bp = Blueprint('miscellaneous', __name__)

@misc_bp.route('/categories', methods=['GET'])
@cross_origin()
@csrf.exempt
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories]), 200

@misc_bp.route('/featured-products', methods=['GET'])
@cross_origin()
@csrf.exempt
def get_featured_products():
    category_name = request.args.get('category')

    if category_name:
        # Query products that are featured and belong to the specified category
        featured_products = Product.query \
            .join(Product.categories) \
            .filter(Product.is_featured == True, Category.name == category_name) \
            .all()
    else:
        # Query all featured products
        featured_products = Product.query.filter(Product.is_featured == True).all()

    # Filter to get the first 4 unique categories
    unique_categories = set()
    filtered_products = []
    for product in featured_products:
        # Assuming each product can have multiple categories
        for category in product.categories:
            if category.name not in unique_categories:
                unique_categories.add(category.name)
                filtered_products.append(product)
                break  # Proceed to next product if one of the categories is added
        if len(filtered_products) >= 4:
            break

    return jsonify([product.to_dict() for product in filtered_products]), 200

@misc_bp.route('/banners', methods=['GET'])
@cross_origin()
@csrf.exempt
def get_banners():
    banners = Banner.query.all()
    return jsonify([banner.to_dict() for banner in banners]), 200
