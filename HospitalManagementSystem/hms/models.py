from datetime import datetime
from hms import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return UserStore.query.get(int(user_id))


class UserStore(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)


class MedicineIssuedToPatient(db.Model):
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.id'), primary_key=True)
    quantity_issued = db.Column(db.Integer)


class DiagnosticIssuedToPatient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('diagnostic.id'))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20),  nullable=False)
    age = db.Column(db.Integer, nullable=False)
    date_of_joining = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    room_type = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Active')

    def __repr__(self):
        return f"Patient('{self.name}')"


class Medicine(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Medicine('{self.name}')"



class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    charge = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"Test('{self.name}')"



