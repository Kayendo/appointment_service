import pytest
import requests

from datetime import datetime

from app.models.appointment import Appoitment

time.sleep(5) 
base_url = 'http://localhost:8000/api'

def test_get_appoinments_empty() -> None: 
	assert requests.get(f'{base_url}/appointments').json() == [Appointment(appointment_id=1, cabinet = 2, doctors_name='Steve')]