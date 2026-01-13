from langchain.tools import Tool
import random

def inpatient_info():
    infos = [
        "Inpatient visiting hours are from 11:00 AM to 01:00 PM and 05:00 PM to 07:00 PM.",
        "Visitors are allowed to visit inpatients between 10:00 AM and 12:00 PM, and again from 04:00 PM to 06:00 PM.",
        "Inpatient visiting hours are divided into two sessions: late morning and early evening.",
        "Each inpatient is allowed a maximum of two visitors during visiting hours.",
        "Children under 12 years old are not permitted to visit inpatient rooms.",
        "Visiting hours for inpatients are subject to hospital policies and may change during special conditions.",
        "All inpatient visitors are required to register at the nurse station before entering patient rooms.",
        "For patient safety, visiting hours may be restricted depending on the patient’s medical condition."
    ]

    return random.choice(infos)

inpatient_info_tool = Tool(
    name="Inpatient Service Information",
    func=lambda _: inpatient_info(),
    description="Provides inpatient service and visiting hour information"
)