from langchain.tools import Tool
import random

def registration_info():
    infos = [
        "New patients must bring a valid ID card, insurance card (if any), and fill out the registration form at the registration counter.",
        "First-time patients are required to present a valid identification card and complete the registration form at the front desk.",
        "New patient registration can be completed at the registration counter by submitting a valid ID and insurance information if available.",
        "Patients registering for the first time should bring a valid ID card and arrive early to complete the registration process.",
        "New patients are advised to prepare their identification documents before registering at the hospital registration counter.",
        "Registration for new patients is handled at the main registration desk during hospital operating hours.",
        "To register as a new patient, please visit the registration counter and follow the instructions provided by hospital staff.",
        "New patient registration requires completing a registration form and presenting valid personal identification."
    ]

    return random.choice(infos)

registration_info_tool = Tool(
    name="Patient Registration Information",
    func=lambda _: registration_info(),
    description="Provides information about new patient registration procedures"
)