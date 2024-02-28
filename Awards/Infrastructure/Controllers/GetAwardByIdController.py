from flask import Blueprint, request, jsonify
from Awards.Application.GetAwardUseCase import GetAwardUseCase

get_Award_blueprint = Blueprint('get_award', __name__)

def initialize_endpoints(repository):
    getAwardUseCase = GetAwardUseCase(repository)

    @get_Award_blueprint.route('/<int:id>', methods=['GET'])
    def get_award(id):
        award = getAwardUseCase.execute(id)
        return jsonify(award.to_dict()), 200