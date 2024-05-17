from uuid import UUID
from pydantic import BaseModel, ConfigDict

class Doctor(BaseModel): 
	model_config = ConfigDict(from_attributes=True) 

	doctor_id: int
	doctor_name: str