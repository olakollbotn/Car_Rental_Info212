from database import db_session
from .utils import node_to_dict  # Import the utility function

class Car:
    @staticmethod
    def create_from_json(json_data):
        with db_session() as session:
            result = session.run(
                "CREATE (car:Car {make: $make, model: $model, year: $year, location: $location, status: 'available'}) RETURN car",
                **json_data
            )
            return result.single()[0]

    @staticmethod
    def get_all():
        with db_session() as session:
            result = session.run("MATCH (car:Car) RETURN car")
            return [node_to_dict(record['car']) for record in result]

    @staticmethod
    def update(car_id, json_data):
        with db_session() as session:
            session.run(
                "MATCH (car:Car) WHERE id(car) = $car_id SET car += $properties",
                car_id=car_id, properties=json_data
            )

    @staticmethod
    def delete(car_id):
        with db_session() as session:
            session.run("MATCH (car:Car) WHERE id(car) = $car_id DETACH DELETE car", car_id=car_id)

    def to_dict(self):
        return dict(self)
