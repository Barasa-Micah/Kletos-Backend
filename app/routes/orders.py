from flask import Blueprint, Flask, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Order, CartItem, OrderItem, Product
from app.extensions import db, csrf
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)
orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
@cross_origin()
@csrf.exempt
@jwt_required()
def place_order():
    user_id = get_jwt_identity()
    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return jsonify({'error': 'No items in cart'}), 400

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    new_order = Order(user_id=user_id, total_price=total_price)

    db.session.add(new_order)
    db.session.commit()

    order_details = {
        'created_at': new_order.created_at.isoformat(),
        'id': new_order.id,
        'products': [],
        'status': new_order.status,
        'total_price': new_order.total_price,
        'user_id': new_order.user_id
    }

    for item in cart_items:
        product = Product.query.get(item.product_id)
        if product:
            product_dict = {
                'created_at': product.created_at.isoformat(),
                'description': product.description,
                'image_url': product.image_url,
                'name': product.name,
                'price': product.price,
                'product_id': product.id,
                'quantity': item.quantity,
                'stock': product.stock
            }
            order_details['products'].append(product_dict)

            order_item = OrderItem(order_id=new_order.id, product_id=item.product_id, quantity=item.quantity)
            db.session.add(order_item)

        db.session.delete(item)

    db.session.commit()

    return jsonify({'message': 'Order placed successfully', 'order': order_details}), 201

@orders_bp.route('/<int:id>', methods=['GET'])
@cross_origin()
@csrf.exempt
@jwt_required()
def get_order(id):
    user_id = get_jwt_identity()
    order = Order.query.filter_by(id=id, user_id=user_id).first()

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    return jsonify({
        'id': order.id,
        'user_id': order.user_id,
        'total_price': order.total_price,
        'status': order.status,
        'created_at': order.created_at
    }), 200

@orders_bp.route('/user_orders/', methods=['GET'])
@cross_origin()
@csrf.exempt
@jwt_required()
def get_user_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).all()

    if not orders:
        return jsonify({'message': 'No orders found for this user'}), 404

    orders_list = []
    for order in orders:
        order_details = {
            'id': order.id,
            'user_id': order.user_id,
            'total_price': order.total_price,
            'status': order.status,
            'created_at': order.created_at.isoformat(),
            'products': []
        }

        order_items = OrderItem.query.filter_by(order_id=order.id).all()
        for item in order_items:
            product = Product.query.get(item.product_id)
            if product:
                product_dict = {
                    'created_at': product.created_at.isoformat(),
                    'description': product.description,
                    'image_url': product.image_url,
                    'name': product.name,
                    'price': product.price,
                    'product_id': product.id,
                    'quantity': item.quantity,
                    'stock': product.stock
                }
                order_details['products'].append(product_dict)

        orders_list.append(order_details)

    return jsonify(orders_list), 200
