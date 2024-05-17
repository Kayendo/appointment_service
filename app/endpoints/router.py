from uuid import UUID
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Body

from app.services.appointment_service import AppointmentService
from app.models.appointment import Appointment, CreateAppointmentRequest

appointment_router = APIRouter(prefix='/appointments', tags=['Appointments'])


@appointment_router.get('/')
def get_all_appointments(appointment_service: AppointmentService = Depends(AppointmentService)) -> list[Appointment]:
    return appointment_service.get_all_appointments()


@appointment_router.post('/')
def create_appointment(create_appointment: CreateAppointmentRequest, appointment_service: AppointmentService = Depends(AppointmentService)) -> Appointment:
    try:
        appointment = appointment_service.create_appointment(
            cabinet=create_appointment.cabinet, doctors_name=create_appointment.doctors_name
        )
        return appointment.dict()
    except KeyError:
        raise HTTPException(status_code=400, detail="Doctor not found")

