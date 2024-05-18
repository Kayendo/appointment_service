import asyncio
from fastapi import FastAPI
from app import rabbitmq
from app.settings import settings
from app.endpoints.router import appointment_router

app = FastAPI(title='Appointment Service') 

@app.on_event('startup') 
def startup(): 
	loop = asyncio.get_event_loop() 
	asyncio.ensure_future(rabbitmq.consume(loop)) 

app.include_router(appointment_router, prefix='/api') 