import pytest

from app.models.appointment import Appointment
from app.repositories.local_appointment_repo import AppointmentsRepo

@pytest.fixture()
def appointment_list() -> list[Appointment]:
	return [
	    Appointment(appointment_id=1, cabinet = 2, doctors_name='Steve')
	]

@pytest.fixture()
def appointments_repo() -> AppointmentsRepo:
	return AppointmentsRepo()

@pytest.fixture()
def test_appointment() -> Appointment:
    return Appointment(appointment_id=2, cabinet = 432, doctors_name='Bill')

appointment_test_repo = AppointmentsRepo()

def test_get_all_appointments(appointment_list: list[Appointment], appointments_repo: AppointmentsRepo):
	assert appointments_repo.get_all_appointments() == appointment_list

def test_get_appointment_by_id(appointment_list: list[Appointment], appointments_repo: AppointmentsRepo):
    assert appointments_repo.get_appointment_by_id(appointment_list[0].appointment_id) == appointment_list[0]

def test_create_appointment(test_appointment: Appointment) -> Appointment:
    assert appointment_test_repo.create_appointment(test_appointment) == test_appointment

    appointments = appointment_test_repo.get_all_appointments()

    assert len(appointments) == 2
    assert appointments[1] == test_appointment