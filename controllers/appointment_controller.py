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
    appointment = appointment_service.book_appointment(
        doctor_id, patient_name, slot)
    # Convert appointment to JSON and return
    pass
