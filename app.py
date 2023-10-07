from flask import Flask
from controllers.doctor_controller import doctor_api
from controllers.appointment_controller import appointment_api

app = Flask(__name__)
app.register_blueprint(doctor_api, url_prefix='/api')
app.register_blueprint(appointment_api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
