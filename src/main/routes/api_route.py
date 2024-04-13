import base64
from io import BytesIO
from PIL import Image
from flask import Blueprint, jsonify, request
from src.infra.neural_network import Model

api_routes_bp = Blueprint("api_routes", __name__)

model = Model("yolov8s")

@api_routes_bp.route('/detect', methods=['POST'])
def detect():
    image_base64  = request.json['image_base64']
    confidence = request.json['confidence']
    iou = request.json['iou']
    
    image_bytes = base64.b64decode(image_base64)
    image_buffer = BytesIO(image_bytes)
    image = Image.open(image_buffer)
    image_rgb = image.convert('RGB')
    predictions = model(image_rgb, confidence, iou)
    detections = [p.to_dict() for p in predictions]
    
    return jsonify(detections)

@api_routes_bp.route('/health_check', methods=['GET'])
def health_check():
    if model is None:
        return "Model is not loaded"
    return f"Model {model.model_name} is loaded"

@api_routes_bp.route('/load_model', methods=['POST'])
def load_model():
    model_name = request.json['model_name']
    global model
    model = Model(model_name)
    return f"Model {model_name} is loaded"