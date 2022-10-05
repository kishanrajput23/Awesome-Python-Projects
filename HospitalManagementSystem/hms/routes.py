from flask import render_template, url_for, flash, redirect, request
from hms import app
from hms.forms import PatientCreationForm, UserStoreLoginForm, PatientUpdationForm, PatientSearchForm, MedicineIssueForm, DiagnosticIssueForm
from hms import db
from hms.models import *
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date


@app.route("/home")
@login_required
def home():
    return render_template('base.html')


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = UserStoreLoginForm()
    if form.validate_on_submit():
        user = UserStore.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            flash(f'You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please recheck username and password', 'danger')

    return render_template('staff_login.html', title='Login', form=form)



@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/all_patients")
@login_required
def allPatients():
    patients = Patient.query.all()
    return render_template('all_patients.html', title="All patient details", patients=patients)



@app.route("/patient", methods=['GET', 'POST'])
@login_required
def createPatient():
    form = PatientCreationForm()
    if form.validate_on_submit():
        patient = Patient(ssn=form.patient_ssn_id.data, 
                          name=form.patient_name.data, 
                          age=form.patient_age.data , 
                          date_of_joining=form.date_of_admission.data, 
                          room_type=form.type_of_bed.data, 
                          address=form.address.data, 
                          state=form.state.data, 
                          city=form.city.data)
        db.session.add(patient)
        db.session.commit()
        flash(f'Patient with SNN {form.patient_ssn_id.data} has been created!', 'success')
        return redirect(url_for('createPatient'))
    return render_template('patient_creation_form.html', title='Create New Patient', form=form)




@app.route("/update", methods=['GET', 'POST'])
@login_required
def updateQuery():
    form = PatientSearchForm()
    if form.validate_on_submit():
        ssn = form.search.data
        return redirect(url_for('updatePatient', ssn=ssn))
    return render_template('patient_search_form.html', form=form)




@app.route("/update/<int:ssn>", methods=['GET', 'POST'])
@login_required
def updatePatient(ssn):
    form = PatientUpdationForm()
    patient = Patient.query.filter_by(ssn=ssn).first()
    form.patient_ssn_id.data = ssn
    if form.validate_on_submit():
        patient.ssn = form.patient_ssn_id.data
        patient.name = form.patient_name.data
        patient.age = form.patient_age.data
        patient.date_of_joining = form.date_of_admission.data
        patient.room_type = form.type_of_bed.data
        patient.address = form.address.data
        patient.state = form.state.data
        patient.city = form.city.data
        db.session.add(patient)
        db.session.commit()
        flash('Patient account has been updated', 'success')
        return redirect(url_for('updatePatient', ssn=patient.ssn))

    elif request.method == 'GET':
        form.patient_ssn_id.data = patient.ssn
        form.patient_name.data = patient.name
        form.patient_age.data = patient.age
        form.date_of_admission.data = patient.date_of_joining
        form.type_of_bed.data = patient.room_type
        form.address.data = patient.address
        form.state.data = patient.state
        form.city.data = patient.city

    return render_template('patient_update_form.html', title='Update Patient Details', form=form,citi=form.city.data)



@app.route("/delete", methods=['GET', 'POST'])
@login_required
def deleteQuery():
    form = PatientSearchForm()
    if form.validate_on_submit():
        ssn = form.search.data
        return redirect(url_for('deletePatient', ssn=ssn))
    return render_template('patient_search_form.html', form=form)



@app.route("/delete/<int:ssn>", methods=['GET', 'POST'])
@login_required
def deletePatient(ssn):
    form = PatientUpdationForm()
    patient = Patient.query.filter_by(ssn=ssn).first()

    if request.method == 'POST':
        db.session.delete(patient)
        db.session.commit()
        flash('Patient has been deleted', 'success')
        return redirect(url_for('home'))
    else:
        context = {
            'ssn': patient.ssn,
            'name': patient.name,
            'age': patient.age,
            'admission': patient.date_of_joining,
            'bed': patient.room_type,
            'address': patient.address,
            'state': patient.state,
            'city': patient.city
        }

        return render_template('patient_delete_form.html', title='Delete Patient Details', form=form, p=context)



@app.route("/search",methods=['GET','POST'])
@login_required
def searchQuery():
    form=PatientSearchForm(request.form)
    if form.validate_on_submit():
        ssn=form.search.data
        return redirect(url_for('patientDetails', ssn=ssn))
    return render_template('patient_search_form.html',form=form)



@app.route("/search/<int:ssn>", methods=['GET', 'POST'])
@login_required
def patientDetails(ssn):
    form = PatientUpdationForm()
    patient = Patient.query.filter_by(ssn=ssn).first()
    context = {
        'ssn': patient.ssn,
        'name': patient.name,
        'age': patient.age,
        'admission': patient.date_of_joining,
        'bed': patient.room_type,
        'address': patient.address,
        'state': patient.state,
        'city': patient.city
    }
    return render_template('patient_details.html', title='Patient Details', form=form, p=context)




@app.route("/billing", methods=['GET', 'POST'])
@login_required
def billingQuery():
    form = PatientSearchForm()
    if form.validate_on_submit():
        ssn = form.search.data
        return redirect(url_for('calculateBill', ssn=ssn))
    return render_template('patient_search_form.html', form=form)




@app.route("/billing/<int:ssn>",methods=['GET','POST'])
@login_required
def calculateBill(ssn):
    medicine_details=[]
    diagnostic_details=[]
    
    #Retriving Medicine details from two medicines tables.
    patient=Patient.query.filter_by(ssn=ssn).first()
    medicine_issued=MedicineIssuedToPatient.query.filter_by(patient_id=patient.id).all()
    for i in range (0,len(medicine_issued)):
        medicine_id=medicine_issued[i].medicine_id
        medicine=Medicine.query.filter_by(id=medicine_id).first()
        medicine_details.append({'name':medicine.name,'quantity':medicine_issued[i].quantity_issued,'rate':medicine.rate,'amount':medicine_issued[i].quantity_issued*medicine.rate})

    
    
    #Retriving Diagnostic details from two diagnostic tables.
    diagnostic_issued=DiagnosticIssuedToPatient.query.filter_by(patient_id=patient.id).all()
    for i in range (0,len(diagnostic_issued)):
        diagnostic_id=diagnostic_issued[i].test_id
        diagnostic=Diagnostic.query.filter_by(id=diagnostic_id).first()
        diagnostic_details.append({'name':diagnostic.name,'amount':diagnostic.charge})


    date1=patient.date_of_joining.date()
    date2=date.today()
    diff=date2-date1
    days=diff.days
    room_rent=0
    if patient.room_type=='Single':
        room_rent=days*8000
    elif patient.room_type=='Semi':
        room_rent=days*4000
    else:
        room_rent=days*2000
    
    room_rent_details={'days':days,'room_rent':room_rent}

    bill_for_pharmacy = 0
    bill_for_diagnostic = 0

    for bill in medicine_details:
        bill_for_pharmacy += bill['amount']

    for bill in diagnostic_details:
        bill_for_diagnostic += bill['amount']

    bill = {
        'bill_for_pharmacy': bill_for_pharmacy,
        'bill_for_diagnostic': bill_for_diagnostic
    }
    payable_bill=room_rent_details['room_rent']+bill['bill_for_pharmacy']+bill['bill_for_diagnostic']
     
    return render_template('patient_billing_screen.html',patient=patient,medicine=medicine_details,diagnostic=diagnostic_details, bill=bill,room_rent_details=room_rent_details,payable_bill=payable_bill,date=date.today())



@app.route("/medicine", methods=['GET', 'POST'])
@login_required
def issueMedicineQuery():
    form = PatientSearchForm()
    if form.validate_on_submit():
        ssn = form.search.data
        return redirect(url_for('issueMedicine', ssn=ssn))
    return render_template('patient_search_form.html', form=form)



@app.route("/medicine/<int:ssn>", methods=['GET', 'POST'])
@login_required
def issueMedicine(ssn):
    form = MedicineIssueForm()
    patient=Patient.query.filter_by(ssn=ssn).first()
    issued_medicines = []
    medicines = MedicineIssuedToPatient.query.filter_by(patient_id=patient.id).all()
    all_medicines=Medicine.query.all()
    for medicine in medicines:
        med = Medicine.query.filter_by(id=medicine.medicine_id).first()
        issued_medicines.append({'name':med.name, 'rate':med.rate, 'quantity':medicine.quantity_issued, 'amount':med.rate*medicine.quantity_issued})
    
    
    if request.method == 'GET':
        return render_template('issue_medicines.html', patient=patient, issued_medicines=issued_medicines, form=form,type='get',all_medicines=all_medicines)

    else:
        if form.validate_on_submit():
            name = form.name.data
            quantity = form.quantity.data
            form.name.data=None
            form.quantity.data=None
            medicine = Medicine.query.filter_by(name=name).first()


            issue_status = MedicineIssuedToPatient.query.filter_by(patient_id=patient.id, medicine_id=medicine.id).first()

            if issue_status != None:
                issue_status.quantity_issued = issue_status.quantity_issued + quantity
                db.session.commit()
            else:
                m = MedicineIssuedToPatient(patient_id=patient.id, medicine_id=medicine.id, quantity_issued=quantity)
                db.session.add(m)
                db.session.commit()

            med = Medicine.query.filter_by(name=name).first()
            med.quantity_available = med.quantity_available - quantity
            db.session.commit()


            issued_medicines = []
            medicines = MedicineIssuedToPatient.query.filter_by(patient_id=patient.id).all()
            for medicine in medicines:
                med = Medicine.query.filter_by(id=medicine.medicine_id).first()
                issued_medicines.append({'name':med.name, 'rate':med.rate, 'quantity':medicine.quantity_issued, 'amount':med.rate*medicine.quantity_issued})
            flash(f'Medicine Issued Successfully','success')
            return redirect(url_for('issueMedicine',ssn=ssn))
            
        return render_template('issue_medicines.html',patient=patient,issued_medicines=issued_medicines,form=form,type='post',all_medicines=all_medicines)

    

@app.route("/all_medicines")
@login_required
def medicineInventory():
    medicines = Medicine.query.all()
    return render_template('medicine_inventory.html', medicines=medicines)





@app.route("/diagnostic", methods=['GET', 'POST'])
@login_required
def issueDiagnosticQuery():
    form = PatientSearchForm()
    if form.validate_on_submit():
        ssn = form.search.data
        return redirect(url_for('issueDiagnostic', ssn=ssn))
    return render_template('patient_search_form.html', form=form)



@app.route("/diagnostic/<int:ssn>", methods=['GET', 'POST'])
@login_required
def issueDiagnostic(ssn):
    form = DiagnosticIssueForm()
    patient=Patient.query.filter_by(ssn=ssn).first()
    issued_diagnostics = []
    tests = DiagnosticIssuedToPatient.query.filter_by(patient_id=patient.id).all()
    all_diagnostic=Diagnostic.query.all()
    for test in tests:
        t = Diagnostic.query.filter_by(id=test.test_id).first()
        issued_diagnostics.append({'name':t.name, 'amount':t.charge})

    if request.method == 'GET':
        return render_template('issue_diagnostic.html', patient=patient, issued_diagnostics=issued_diagnostics, form=form,type='get',all_diagnostic=all_diagnostic)

    else:
        if form.validate_on_submit():
            name = form.name.data
            test = Diagnostic.query.filter_by(name=name).first()

            
            m = DiagnosticIssuedToPatient(patient_id=patient.id, test_id=test.id)
            db.session.add(m)
            db.session.commit()

            issued_diagnostics = []
            tests = DiagnosticIssuedToPatient.query.filter_by(patient_id=patient.id).all()
            for test in tests:
                t = Diagnostic.query.filter_by(id=test.test_id).first()
                issued_diagnostics.append({'name':t.name, 'amount':t.charge})
            flash(f'Diagnostic Issued Successfully.','success')
            return redirect(url_for('issueDiagnostic',ssn=ssn))

        return render_template('issue_diagnostic.html', patient=patient, issued_diagnostics=issued_diagnostics, form=form,type='post',all_diagnostic=all_diagnostic)






@app.route("/all_tests")
@login_required
def diagnosticDetails():
    tests = Diagnostic.query.all()
    return render_template('diagnostic_details.html', tests=tests)






