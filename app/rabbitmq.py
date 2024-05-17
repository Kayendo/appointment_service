import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage
from app.settings import settings
from app.services.appointment_service import AppointmentService


async def process_appointment_request(msg: IncomingMessage, appointment_service: AppointmentService):
    try:
        data = json.loads(msg.body.decode())
        doctors_name = data['doctors_name']
        cabinet = data['cabinet']
        appointment_service.create_appointment(doctors_name, cabinet)
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()
    appointment_queue = await channel.declare_queue('appointment_requests_queue', durable=True)

    await appointment_queue.consume(process_appointment_request)

    print('Started RabbitMQ consuming...')

    return connection