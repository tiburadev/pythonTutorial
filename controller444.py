from flask import request, jsonify
import MwsCustomerShipmentDetail
import db
import app.responses as responses
import datetime

class MwsCustomerShipmentDetailController:

    @staticmethod
    def get_all():
        # Your logic to get all shipments
        shipments = MwsCustomerShipmentDetail.query.all()
        return jsonify(responses.get(200, "Ok", [shipment.to_dict() for shipment in shipments], False)), 200

    @staticmethod
    def get_one(id):
        # Your logic to get a specific shipment by id
        shipment = MwsCustomerShipmentDetail.query.get_or_404(id)
        return jsonify(responses.get(200, "Ok", shipment.to_dict(), False)), 200

    @staticmethod
    def save(id):
        # Your logic to save/update a specific shipment by id
        shipment = MwsCustomerShipmentDetail.query.get_or_404(id)
        data = request.json
        shipment.update(data)
        db.session.commit()
        return jsonify(responses.get(200, "Ok", shipment.to_dict(), False)), 200

    @staticmethod
    def create():
        # Your logic to create a new shipment
        data = request.json
        data['created_by'] = 1  # Example user ID, replace with actual user logic
        data['modified_by'] = 1  # Example user ID, replace with actual user logic
        data['company_id'] = 1  # Example company ID, replace with actual company logic
        data['created'] = datetime.datetime.now()
        data['modified'] = datetime.datetime.now()
        data['name'] = f"{data.get('first_name', '')} {data.get('middle_name', '')} {data.get('last_name', '')}".strip()

        new_shipment = MwsCustomerShipmentDetail(**data)
        db.session.add(new_shipment)
        db.session.commit()
        return jsonify(responses.get(201, "Created", new_shipment.to_dict(), False)), 201
