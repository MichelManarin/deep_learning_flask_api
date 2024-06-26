from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.infra.neural_network import Model
from src.main.adapter import flask_adapter
from src.main.composer import (
    register_user_input_composer,
    register_detection_results_composer,
    list_historic_composer
)

api_routes_bp = Blueprint("api_routes", __name__)
CORS(api_routes_bp, resources={r"/api/*": {"origins": "https://deeplearningreact-production.up.railway.app"}})

model = Model("yolov8s")

@api_routes_bp.route("/api/user-input", methods=["POST"])
def register_user():
    """ register user input route """

    message = {}
    response = flask_adapter(request=request, api_route=register_user_input_composer())

    if response.status_code < 300:
        message = {
            "type": "user-input",
            "data": response.body.id,
            "attributest": {"path": response.body.path, "iou": response.body.iou," confidence": response.body.confidence },
        }

        return jsonify(message), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/detection-result", methods=["POST"])
def register_detection_result():
    """ register detection result """

    message = {}
    response = flask_adapter(request=request, api_route=register_detection_results_composer())

    if response.status_code < 300:
        message = {
            "type": "detection-result",
            "data": response.body[0],
        }

        return jsonify(message), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

@api_routes_bp.route("/api/historic", methods=["GET"])
def list_historic_result():
    """ list historic result """

    message = {}
    response = flask_adapter(request=request, api_route=list_historic_composer())

    if response.status_code < 300:
        historics_dicts = [historic._asdict() for historic in response.body]
        message = {
            "type": "list-historic",
            "data": historics_dicts,
        }

        return jsonify(message), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


# TODO: refactor endpoints below in future
@api_routes_bp.route('/api/health_check', methods=['GET'])
def health_check():
    if model is None:
        return "Model is not loaded"
    return f"Model {model.model_name} is loaded"

@api_routes_bp.route('/api/load_model', methods=['POST'])
def load_model():
    model_name = request.json['model_name']
    global model
    model = Model(model_name)
    return f"Model {model_name} is loaded"