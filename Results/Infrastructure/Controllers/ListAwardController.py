from flask import Blueprint, request, jsonify
from Awards.Application.ListAwardsUseCase import ListAwardsUseCase

get_list_awards_blueprint = Blueprint('get_list_awards', __name__)

def initialize_endpoints(award_repo):
    listAwardsUseCase = ListAwardsUseCase(award_repo)

    @get_list_awards_blueprint.route('/', methods=['GET'])
    def get_list_awards():
        try:
            awards = listAwardsUseCase.execute()
            awards = [award.to_dict() for award in awards]
            return jsonify(awards), 200
        except Exception as e:
            return jsonify({"message": "Error getting awards", "error": str(e)}), 400