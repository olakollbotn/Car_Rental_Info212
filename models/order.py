from database import db_session

class Order:
    @staticmethod
    def order_car(customer_id, car_id):
        with db_session() as session:
            session.run(
                "MATCH (customer:Customer) WHERE id(customer) = $customer_id "
                "MATCH (car:Car) WHERE id(car) = $car_id AND car.status = 'available' "
                "MERGE (customer)-[:BOOKED]->(car) "
                "SET car.status = 'booked'",
                customer_id=customer_id, car_id=car_id
            )

    @staticmethod
    def cancel_order_car(customer_id, car_id):
        with db_session() as session:
            session.run(
                "MATCH (customer:Customer)-[r:BOOKED]->(car:Car) WHERE id(customer) = $customer_id AND id(car) = $car_id "
                "DELETE r "
                "SET car.status = 'available'",
                customer_id=customer_id, car_id=car_id
            )

    @staticmethod
    def rent_car(customer_id, car_id):
        with db_session() as session:
            session.run(
                "MATCH (customer:Customer)-[:BOOKED]->(car:Car) WHERE id(customer) = $customer_id AND id(car) = $car_id "
                "SET car.status = 'rented'",
                customer_id=customer_id, car_id=car_id
            )

    @staticmethod
    def return_car(customer_id, car_id, status):
        with db_session() as session:
            session.run(
                "MATCH (customer:Customer)-[:BOOKED]->(car:Car) WHERE id(customer) = $customer_id AND id(car) = $car_id "
                "SET car.status = $status "
                "REMOVE customer-[:BOOKED]->car",
                customer_id=customer_id, car_id=car_id, status=status
            )
