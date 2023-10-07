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
