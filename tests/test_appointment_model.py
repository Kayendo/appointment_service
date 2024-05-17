import pytest
from uuid import uuid4
from pydantic import ValidationError

from app.models.appointment import Appointment

def test_appointment_creation():
	id = 1
	cabinet = 234
	name = 'Bill'

	appointment = Appointment(appointment_id = id, cabinet = cabinet, doctors_name = name)

	assert dict(appointment) == {'appointment_id': id, 'cabinet': cabinet, 'doctors_name': name}


