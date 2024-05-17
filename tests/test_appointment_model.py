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


def test_doctors_name_required():
	with pytest.raises(ValidationError):
		Appointment(appointment_id = 1, cabinet=22)

def test_cabinet__required():
	with pytest.raises(ValidationError):
		Appointment(appointment_id = 1, doctors_name='Bill')



