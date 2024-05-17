from uuid import UUID
import random
from datetime import datetime

from app.models.appointment import Appointment
from app.repositories.local_appointment_repo import AppointmentsRepo
from app.repositories.local_doctor_repo import DoctorsRepo


class AppointmentService:
    def __init__(self) -> None:
        self.appointments_repo = AppointmentsRepo()
        self.doctors_repo = DoctorsRepo()

    def get_all_appointments(self):
        return self.appointments_repo.get_all_appointments()

    def get_appointment_by_id(self, appointment_id: int):
        return self.appointments_repo.get_appointment_by_id(self, appointment_id)

    def create_appointment(self, doctors_name, cabinet):
        doctor = self.doctors_repo.get_doctor_by_name(doctors_name)
        appointment = Appointment(appointment_id = random.randint(0, 19), doctors_name = doctors_name,  cabinet = cabinet )
        return self.appointments_repo.create_appointment(appointment)
