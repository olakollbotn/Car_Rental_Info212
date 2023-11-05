from flask import Blueprint, request, jsonify, render_template
from models.car import Car

car_blueprint = Blueprint('car_blueprint', __name__)

@car_blueprint.route('/', methods=['POST'])
def create_car():
    if request.is_json:
        car = Car.create_from_json(request.get_json())
        return jsonify(car.to_dict()), 201
    return jsonify({"error": "Request must be JSON"}), 415

@car_blueprint.route('/', methods=['GET'])
def get_cars():
    cars = Car.get_all()
    return render_template('cars.html', cars=cars)

@car_blueprint.route('/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    if request.is_json:
        Car.update(car_id, request.get_json())
        return jsonify({"success": "Car updated successfully"}), 200
    return jsonify({"error": "Request must be JSON"}), 415

@car_blueprint.route('/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    Car.delete(car_id)
    return jsonify({"success": "Car deleted successfully"}), 200
