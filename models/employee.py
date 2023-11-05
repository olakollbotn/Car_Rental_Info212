from database import db_session
from .utils import node_to_dict  # Import the utility function

class Employee:
    @staticmethod
    def create_from_json(json_data):
        with db_session() as session:
            result = session.run(
                "CREATE (employee:Employee {name: $name, address: $address, branch: $branch}) RETURN employee",
                **json_data
            )
            return result.single()[0]

    @staticmethod
    def get_all():
        with db_session() as session:
            result = session.run("MATCH (employee:Employee) RETURN employee")
            return [node_to_dict(record['employee']) for record in result]

    @staticmethod
    def update(employee_id, json_data):
        with db_session() as session:
            session.run(
                "MATCH (employee:Employee) WHERE id(employee) = $employee_id SET employee += $properties",
                employee_id=employee_id, properties=json_data
            )

    @staticmethod
    def delete(employee_id):
        with db_session() as session:
            session.run("MATCH (employee:Employee) WHERE id(employee) = $employee_id DETACH DELETE employee", employee_id=employee_id)

    def to_dict(self):
        return dict(self)
