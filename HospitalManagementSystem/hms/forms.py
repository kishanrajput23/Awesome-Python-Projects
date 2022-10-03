from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField, TextAreaField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Optional
from hms.models import *
from flask_login import current_user


class PatientCreationForm(FlaskForm):
    patient_ssn_id = IntegerField('Patient SSN ID', validators=[DataRequired(message="Numeric data is required"), NumberRange(min=99999999, max=999999999, message="patient ssn id must be 9 digit numeric")])
    patient_name = StringField('Patient Name', validators=[DataRequired(), Length(min=2, max=20)])
    patient_age = IntegerField('Patient Age', validators=[DataRequired(), NumberRange(min=1, max=999, message="patient's age must be numeric")])
    date_of_admission = DateTimeField('Date of Admission (YYYY-MM-DD)', format='%Y-%m-%d', validators=[DataRequired()])
    type_of_bed = SelectField('Type of Bed', choices=[('','Choose Room Type'),('General', 'General'), ('Semi', 'Semi'), ('Single', 'Single')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)])
    state = SelectField('State', choices=[('','Choose State'),('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'),('Bihar','Bihar'),('Chandigarh','Chandigarh'),('Chhattisgarh','Chhattisgarh'),('Dadra & Nagar Haveli and Daman & Diu','Dadra & Nagar Haveli and Daman & Diu'),('New Delhi','New Delhi'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),('Jammu and Kashmir','Jammu and Kashmir'),('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),('Lakshadweep','Lakshadweep'),('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Odisha','Odisha'),('Puducherry','Puducherry'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),('Uttarakhand','Uttarakhand'),('Uttar Pradesh','Uttar Pradesh'),('West Bengal','West Bengal')], validators=[DataRequired()])
    city = SelectField('City', choices=[],validate_choice=False)
    submit = SubmitField('Create')

    # custom validation for patient ssn id
    def validate_patient_ssn_id(self, patient_ssn_id):
        patient = Patient.query.filter_by(ssn=patient_ssn_id.data).first()
        if patient:
            raise ValidationError('Patient Already Exists')
    
    # custom validation for city
    def validate_city(self,city):
        if city.data==None or city.data=="" or city.data=='Choose City':
            raise ValidationError('This field is required')



class UserStoreLoginForm(FlaskForm):
    username = StringField('User',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class PatientUpdationForm(FlaskForm):
    patient_ssn_id = IntegerField('Patient SSN ID', validators=[DataRequired(message="Numeric data is required"), NumberRange(min=99999999, max=999999999, message="patient ssn id must be 9 digit numeric")])
    patient_name = StringField('Patient Name', validators=[DataRequired(), Length(min=2, max=20)])
    patient_age = IntegerField('Patient Age', validators=[DataRequired(), NumberRange(min=1, max=999, message="patient's age must be numeric")])
    date_of_admission = DateTimeField('Date of Admission (YYYY-MM-DD)', format='%Y-%m-%d', validators=[DataRequired()])
    type_of_bed = SelectField('Type of Bed', choices=[('','Choose Room Type'),('General', 'General'), ('Semi', 'Semi'), ('Single', 'Single')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)])
    state = SelectField('State', choices=[('','Choose State'),('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'),('Bihar','Bihar'),('Chandigarh','Chandigarh'),('Chhattisgarh','Chhattisgarh'),('Dadra & Nagar Haveli and Daman & Diu','Dadra & Nagar Haveli and Daman & Diu'),('New Delhi','New Delhi'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),('Jammu and Kashmir','Jammu and Kashmir'),('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),('Lakshadweep','Lakshadweep'),('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Odisha','Odisha'),('Puducherry','Puducherry'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),('Uttarakhand','Uttarakhand'),('Uttar Pradesh','Uttar Pradesh'),('West Bengal','West Bengal')], validators=[DataRequired()])
    city = SelectField('City', choices=[],validate_choice=False)
    submit = SubmitField('Update')

    def validate_city(self,city):
        if city.data==None or city.data=="" or city.data=='Choose City':
            raise ValidationError('This field is required')



class PatientSearchForm(FlaskForm):
    search=IntegerField('SSN Id',validators=[DataRequired("Numeric data is required."), NumberRange(min=99999999, max=999999999, message="patient ssn id must be 9 digit numeric")])
    submit=SubmitField('Search')

    def validate_search(self, search):
        patient = Patient.query.filter_by(ssn=search.data).first()
        if patient == None:
            raise ValidationError('Patient with this SSN ID does not exists')



class MedicineIssueForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity',validators=[DataRequired("Numeric data is required.")])
    submit=SubmitField('Add')

    def validate_name(self, name):
        medicine = Medicine.query.filter_by(name=name.data).first()
        if medicine == None:
            raise ValidationError('Not Available')

    def validate_quantity(self,quantity):
        medicine=Medicine.query.filter_by(name=self.name.data).first()
        if medicine != None:
            if quantity.data > medicine.quantity_available:
                raise ValidationError('Insufficient quantity present in stock. Quantity presents: '+str(medicine.quantity_available))
       


class DiagnosticIssueForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit=SubmitField('Add')
    
    def validate_name(self, name):
        diagnostic = Diagnostic.query.filter_by(name=name.data).first()
        if diagnostic == None:
            raise ValidationError('Not Available')