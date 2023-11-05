from flask import Blueprint, request, jsonify, render_template
from models.employee import Employee

employee_blueprint = Blueprint('employee_blueprint', __name__)

@employee_blueprint.route('/', methods=['POST'])
def create_employee():
    if request.is_json:
        employee = Employee.create_from_json(request.get_json())
        return jsonify(employee.to_dict()), 201
    return jsonify({"error": "Request must be JSON"}), 415

@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    employees = Employee.get_all()
    return render_template('employees.html', employees=employees)

@employee_blueprint.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    if request.is_json:
        Employee.update(employee_id, request.get_json())
        return jsonify({"success": "Employee updated successfully"}), 200
    return jsonify({"error": "Request must be JSON"}), 415

@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    Employee.delete(employee_id)
    return jsonify({"success": "Employee deleted successfully"}), 200
