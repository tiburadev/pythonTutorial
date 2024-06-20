from app.database import db

class MwsCustomerShipmentDetail(db.Model):
    __tablename__ = 'mws_customer_shipment_details'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created_by = db.Column(db.Integer)
    modified_by = db.Column(db.Integer)
    company_id = db.Column(db.Integer)
    name = db.Column(db.String(150))
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
