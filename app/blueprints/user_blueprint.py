from flask import Blueprint
from app.controllers.user_controller import hello

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/hello', methods=['GET'])
def hello_route():
    return hello()

