from uuid import UUID
from app.models.doctor import Doctor

doctors: list[Doctor] = [
    Doctor(doctor_id=1, doctor_name='Steve'),
    Doctor(doctor_id=2, doctor_name='Bill')
]


class DoctorsRepo:
    def get_all_doctors(self) -> list[Doctor]:
        return doctors

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        raise KeyError("Doctor not found")

    def get_doctor_by_name(self, doctor_name: str) -> Doctor:
        for doctor in doctors:
            if doctor.doctor_name == doctor_name:
                return doctor
        raise KeyError("Doctor not found")
