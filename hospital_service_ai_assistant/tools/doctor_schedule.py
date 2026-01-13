from langchain.tools import Tool
import random

def doctor_schedule():
    schedules = [
        "Dr. Andi is available on Monday from 08:00 AM to 11:00 AM at the outpatient clinic.",
        "Dr. Andi is available on Tuesday from 09:00 AM to 12:00 PM at the outpatient clinic.",
        "Dr. Andi is available on Wednesday from 10:00 AM to 01:00 PM at the outpatient clinic.",
        "Dr. Andi is available on Thursday from 01:00 PM to 04:00 PM at the outpatient clinic.",
        "Dr. Andi is available on Friday from 02:00 PM to 05:00 PM at the outpatient clinic.",
        "Dr. Andi is not available today due to a medical conference.",
        "Dr. Andi is not available today. Please check again tomorrow.",
        "Dr. Andi’s schedule is currently full. Please contact the registration counter for assistance."
    ]

    return random.choice(schedules)

doctor_schedule_tool = Tool(
    name="Doctor Schedule Information",
    func=lambda _: doctor_schedule(),
    description="Provides doctor schedule information"
)