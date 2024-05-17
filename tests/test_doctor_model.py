import pytest
from uuid import uuid4
from pydantic import ValidationError

from app.models.doctor import Doctor

def test_doctor_creation():
	id = 1
	name = 'Bill'
	doctor = Doctor(doctor_id=id, doctor_name=name)

	assert dict(doctor) == {'doctor_id': id, 'doctor_name': name}

def test_doctor_name_required():
    with pytest.raises(ValidationError):
        Doctor(doctor_id=id)

