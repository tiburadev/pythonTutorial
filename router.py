from flask import Blueprint
from ..controllers.mws_customer_shipment_detail_controller import MwsCustomerShipmentDetailController

customer_shipment_bp = Blueprint('customer_shipment', __name__)

customer_shipment_bp.add_url_rule('/mwscustomerShipment', view_func=MwsCustomerShipmentDetailController.get_all, methods=['GET'])
customer_shipment_bp.add_url_rule('/mwscustomerShipment/<id>', view_func=MwsCustomerShipmentDetailController.get_one, methods=['GET'])
customer_shipment_bp.add_url_rule('/mwscustomerShipment', view_func=MwsCustomerShipmentDetailController.create, methods=['POST'])
customer_shipment_bp.add_url_rule('/mwscustomerShipment/<id>', view_func=MwsCustomerShipmentDetailController.save, methods=['POST'])
