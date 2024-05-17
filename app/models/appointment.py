import enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.doctor import Doctor

class Appointment(BaseModel): 
	model_config = ConfigDict(from_attributes=True) 
	appointment_id: int
	cabinet: int
	doctors_name: str

class CreateAppointmentRequest(BaseModel):
    doctors_name: str
    cabinet: int