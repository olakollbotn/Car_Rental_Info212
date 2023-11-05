from database import db_session
from .utils import node_to_dict  # Import the utility function

class Customer:
    @staticmethod
    def create_from_json(json_data):
        with db_session() as session:
            result = session.run(
                "CREATE (customer:Customer { id: $id, name: $name, age: $age, address: $address}) RETURN customer",
                **json_data
            )
            return result.single()[0]

    @staticmethod
    def get_all():
        with db_session() as session:
            result = session.run("MATCH (customer:Customer) RETURN customer")
            return [node_to_dict(record['customer']) for record in result]

    @staticmethod
    def update(customer_id, json_data):
        with db_session() as session:
            session.run(
                "MATCH (customer:Customer) WHERE id(customer) = $customer_id SET customer += $properties",
                customer_id=customer_id, properties=json_data
            )

    @staticmethod
    def delete(customer_id):
        with db_session() as session:
            session.run("MATCH (customer:Customer) WHERE id(customer) = $customer_id DETACH DELETE customer", customer_id=customer_id)

    def to_dict(self):
        return dict(self)
