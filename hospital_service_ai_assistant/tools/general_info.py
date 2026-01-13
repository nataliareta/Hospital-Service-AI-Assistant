from langchain.tools import Tool
import random

def general_info():
    infos = [
        "The cardiology clinic is located on the 2nd floor. The pharmacy is open 24 hours.",
        "The outpatient clinics are located on the 1st and 2nd floors. The pharmacy operates 24/7.",
        "The emergency department is located on the ground floor and is open 24 hours.",
        "The pharmacy is located next to the main lobby and is open 24 hours a day.",
        "The cardiology clinic is on the 2nd floor, while the radiology department is on the 1st floor.",
        "The hospital information desk is located near the main entrance on the ground floor.",
        "Public restrooms are available on every floor near the elevator area.",
        "The hospital cafeteria is located on the 3rd floor and is open from 7:00 AM to 7:00 PM."
    ]

    return random.choice(infos)

general_info_tool = Tool(
    name="General Hospital Information",
    func=lambda _: general_info(),
    description="Provides general hospital information such as clinic locations and services"
)