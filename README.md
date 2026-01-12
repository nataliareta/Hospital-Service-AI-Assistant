# Hospital-Service-AI-Assistant
This project will develop an AI-based chatbot that assists patients and hospital visitors in obtaining hospital service information quickly, accurately, and efficiently, without replacing the role of medical professionals. With this project, the hospital’s customer service workload can be reduced, responses can be provided quickly 24/7 without waiting for hospital staff to be online, information delivery becomes more consistent, and the system can be easily scaled and developed for production use.

## Use Case
**Target User:**
- New patients: Confused about the registration process
- Returning patients: Looking for doctor schedules
- Patient families: Seeking information about inpatient services
- General visitors: Visiting hours and clinic locations

**Here are some example questions:**
1. New Patients
- “How do I register as a new patient?”
- “What documents do I need for first-time registration?”
- “Where is the registration counter located?”
2. Returning Patients
- “What is the schedule for Dr. Andi today?”
- “How can I book an appointment online?”
- “Can I reschedule my doctor’s appointment?”
3. Patient Families
- “What are the visiting hours for inpatients?”
- “How can I get information about a patient’s room?”
- “What are the rules for inpatient visitors?
4. General Visitors
- “Where is the cardiology clinic located?”
- “What time does the outpatient clinic open?”
- “Is there a pharmacy inside the hospital?”

## Scope Project
**Scope Project Hospital Service AI Assistant And Supporting Technologies**
- AI Agent Architecture: This project uses an AI Agent architecture, where the chatbot does not function merely as a question-and-answer system, but is also capable of analyzing user intent, making decisions, and determining the most appropriate action. The agent acts as the main decision-maker that understands the context of the user’s question, selects the most relevant tool, and then composes a response based on the tool’s output.
- LangChain Framework: LangChain is used as the main framework for developing the chatbot because it provides a modular and well-structured way to build applications based on Large Language Models. Through LangChain, prompts, agents, tools, and memory can be managed separately while remaining fully integrated.
- Large Language Model (Gemini 2.0 Flash Lite): The chatbot uses Gemini 2.0 Flash Lite as its primary language model. This model is chosen for its low latency, meaning fast response times between user queries and system-generated answers. In addition, the model is lightweight and cost-efficient, making it suitable for public service applications such as hospitals that require fast and stable responses.
- Tool-Based System (Dummy Tools): The chatbot system is designed using a tool-based approach, where the agent can call specific functions to retrieve particular information, such as doctor schedules, registration flows, or hospital service details. The tools used in this project are dummy or simulated tools, meaning they are not directly connected to real hospital databases or APIs.
- Single Tool Selection Logic: In each interaction, the agent is restricted to selecting only one tool that is most relevant to the user’s question. This approach encourages more efficient intent analysis and prevents unnecessary tool calls.
- Conversation Memory: The chatbot is equipped with a memory feature that allows the system to remember previous messages within a single interaction session. With memory, the chatbot can provide more contextual and natural responses, as it understands the relationship between consecutive user questions. 
- Prompt Engineering: Prompt engineering is used to control the chatbot’s behavior so that it consistently operates within its defined role and limitations. Through carefully designed prompts, the chatbot is guided to focus on hospital service information and explicitly avoid providing medical diagnoses or medication recommendations.

## System Architecture
//gambarr//
The system is designed using an agent-based architecture where user input is first processed by a prompt-guided AI agent. The agent analyzes the user intent and selects exactly one appropriate tool to retrieve relevant information. The tool response is then transformed into a natural language answer and returned to the user.
**Technologies Used:** Python, LangChain, LLM (Gemini 2.0 Flash Lite), Dummy Tools.

## Workflow
1) The system workflow begins when a user submits a question to the chatbot. The question is received by the AI agent, which has been configured with prompts containing the system’s rules, roles, and limitations, particularly within the context of healthcare services.
2) The agent then analyzes the user’s intent to determine the category of information needed, such as doctor schedules, registration procedures, or general questions about hospital services. Based on this analysis, the agent selects the single most relevant tool to use.
3) The selected tool returns data or information that matches the user’s request. This data is then processed by the agent and structured into a clear and natural-language response that is easy to understand. The final answer is sent back to the user as the chatbot’s response.

## Setup & Run
To run this project locally, make sure that Python with a compatible version is installed. The execution steps are as follows:
Python installed → Clone the repository from GitHub to your local machine → Install all required dependencies using the provided requirements file → Run the main application file via the command line → The chatbot is ready to receive user input and execute the workflow based on the predefined agent and tools design.
