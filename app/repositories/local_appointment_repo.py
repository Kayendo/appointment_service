from uuid import UUID
from datetime import datetime
from app.models.appointment import Appointment

appointments: list[Appointment] = []


class AppointmentsRepo:
    def get_all_appointments(self) -> list[Appointment]:
        return appointments

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        for appointment in appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        raise KeyError("Appointment not found")

    def create_appointment(self, appointment: Appointment) -> Appointment:
        appointments.append(appointment)
        return appointment
