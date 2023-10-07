# PearlThoughts

Creating a full-fledged API system involves a lot of code and files, which can't be provided here in entirety. However, I can certainly help you with the structure, and you can use it as a basis for your implementation. Below is a simplified version of how you can structure your code using Python and Flask, a popular web framework for building APIs.

**Folder Structure:**

```
- /app
  - /controllers
    - doctor_controller.py
    - appointment_controller.py
  - /models
    - doctor.py
    - appointment.py
  - /services
    - doctor_service.py
    - appointment_service.py
  - app.py
- requirements.txt
- config.py
```

**doctor.py (models)**
```python
class Doctor:
    def __init__(self, id, name, available_slots):
        self.id = id
        self.name = name
        self.available_slots = available_slots
```

**appointment.py (models)**
```python
class Appointment:
    def __init__(self, id, doctor_id, patient_name, slot):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_name = patient_name
        self.slot = slot
```

**doctor_service.py (services)**
```python
from models.doctor import Doctor

class DoctorService:
    def get_all_doctors(self):
        # Logic to get all doctors from database
        pass

    def get_doctor_by_id(self, doctor_id):
        # Logic to get doctor by ID from database
        pass
```

**appointment_service.py (services)**
```python
from models.appointment import Appointment

class AppointmentService:
    def book_appointment(self, doctor_id, patient_name, slot):
        # Logic to book appointment and save it to the database
        pass
```

**doctor_controller.py (controllers)**
```python
from flask import Blueprint, jsonify
from services.doctor_service import DoctorService

doctor_api = Blueprint('doctor_api', __name__)
doctor_service = DoctorService()

@doctor_api.route('/doctors', methods=['GET'])
def get_all_doctors():
    doctors = doctor_service.get_all_doctors()
    # Convert doctors to JSON and return
    pass

@doctor_api.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    # Convert doctor to JSON and return
    pass
```

**appointment_controller.py (controllers)**
```python
from flask import Blueprint, request
from services.appointment_service import AppointmentService

appointment_api = Blueprint('appointment_api', __name__)
appointment_service = AppointmentService()

@appointment_api.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.get_json()
    doctor_id = data['doctor_id']
    patient_name = data['patient_name']
    slot = data['slot']
    appointment = appointment_service.book_appointment(doctor_id, patient_name, slot)
    # Convert appointment to JSON and return
    pass
```

**app.py**
```python
from flask import Flask
from controllers.doctor_controller import doctor_api
from controllers.appointment_controller import appointment_api

app = Flask(__name__)
app.register_blueprint(doctor_api, url_prefix='/api')
app.register_blueprint(appointment_api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
```

In this structure, you would have your model classes in the `models` folder, service classes in the `services` folder, and the API endpoint handling in the `controllers` folder. The `app.py` file initializes your Flask app and registers the blueprints for doctors and appointments API.

Please note that this is a basic structure and does not include actual database connections or error handling. For a real application, you would need to integrate a database, handle exceptions, and add security features like authentication and authorization.
