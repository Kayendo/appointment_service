import pytest

from app.models.doctor import Doctor
from app.repositories.local_doctor_repo import DoctorsRepo

@pytest.fixture()
def doctors_list() -> list[Doctor]:
	return [
	    Doctor(doctor_id=1, doctor_name='Steve'),
    	Doctor(doctor_id=2, doctor_name='Bill')
	]

@pytest.fixture()
def doctors_repo() -> DoctorsRepo:
	return DoctorsRepo()

def test_get_all_doctors(doctors_list: list[Doctor], doctors_repo: DoctorsRepo):
	assert doctors_repo.get_all_doctors() == doctors_list

def test_get_doctor_by_name(doctors_list: list[Doctor], doctors_repo: DoctorsRepo):
    assert doctors_repo.get_doctor_by_name(doctors_list[0].doctor_name) == doctors_list[0]