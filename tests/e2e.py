import pytest
import requests

from datetime import datetime

from app.models.appointment import Appoitment

time.sleep(5) 
base_url = 'http://localhost:8000/api'
@pytest.fixture(scope='session') 
def first_delivery_data() -> tuple[UUID, str, datetime]: 
	return (uuid4(), 'address_1', datetime.now())

def test_get_appoinments_empty() -> None: 
	assert requests.get(f'{base_url}/appointments').json() == []