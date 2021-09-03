from flask import jsonify, Blueprint, request
from http import HTTPStatus

from src.entities.studio.model import Studio
from src.entities.studio.repository import StudioRepository

studio_controller_api = Blueprint('studio_controller_api', __name__)


@studio_controller_api.route('/api/studios', methods=['GET'])
def get_studios():
    s = StudioRepository()
    obj = s.get()
    return jsonify(obj), HTTPStatus.OK


@studio_controller_api.route('/api/studios/post', methods=['POST'])
def post_studio():
    request.method = 'POST'
    studio_data = request.json
    s = StudioRepository()
    name = studio_data["name"]
    studio = Studio(name)
    s.add(studio)
    return '', HTTPStatus.OK


@studio_controller_api.route('/api/studios/<int:id>', methods=['DELETE'])
def delete_studio(id):
    s = StudioRepository()
    s.delete(id)
    return '', HTTPStatus.OK
