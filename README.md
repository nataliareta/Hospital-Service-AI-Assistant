# Hospital-Service-AI-Assistant
This project will develop an AI-based chatbot that assists patients and hospital visitors in obtaining hospital service information quickly, accurately, and efficiently, without replacing the role of medical professionals. With this project, the hospital’s customer service workload can be reduced, responses can be provided quickly 24/7 without waiting for hospital staff to be online, information delivery becomes more consistent, and the system can be easily scaled and developed for production use.

## Use Case
**Target User: **
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
- AI Agent Architecture
This project uses an AI Agent architecture, where the chatbot does not function merely as a question-and-answer system, but is also capable of analyzing user intent, making decisions, and determining the most appropriate action. The agent acts as the main decision-maker that understands the context of the user’s question, selects the most relevant tool, and then composes a response based on the tool’s output. This approach makes the chatbot closer to real-world AI systems rather than a static chatbot.
- LangChain Framework
LangChain is used as the main framework for developing the chatbot because it provides a modular and well-structured way to build applications based on Large Language Models. Through LangChain, prompts, agents, tools, and memory can be managed separately while remaining fully integrated. This framework helps ensure that the AI system is easier to maintain, extend, and understand, especially in the context of healthcare service applications.
- Large Language Model (Gemini 2.0 Flash Lite)
The chatbot uses Gemini 2.0 Flash Lite as its primary language model. This model is chosen for its low latency, meaning fast response times between user queries and system-generated answers. In addition, the model is lightweight and cost-efficient, making it suitable for public service applications such as hospitals that require fast and stable responses. Its capabilities are sufficient to handle administrative and general informational questions without compromising system performance.
- Tool-Based System (Dummy Tools)
The chatbot system is designed using a tool-based approach, where the agent can call specific functions to retrieve particular information, such as doctor schedules, registration flows, or hospital service details. The tools used in this project are dummy or simulated tools, meaning they are not directly connected to real hospital databases or APIs. This approach allows the development to focus on agent logic and system architecture, and makes it easier for reviewers to run the project without external dependencies.
- Single Tool Selection Logic
In each interaction, the agent is restricted to selecting only one tool that is most relevant to the user’s question. This approach encourages more efficient intent analysis and prevents unnecessary tool calls. The single-tool selection logic reflects best practices in production AI systems, where efficiency, performance, and resource management are key considerations.
- Conversation Memory
The chatbot is equipped with a memory feature that allows the system to remember previous messages within a single interaction session. With memory, the chatbot can provide more contextual and natural responses, as it understands the relationship between consecutive user questions. This feature improves the overall user experience and makes the interaction feel more like a conversation with a human assistant.
- Prompt Engineering
Prompt engineering is used to control the chatbot’s behavior so that it consistently operates within its defined role and limitations. Through carefully designed prompts, the chatbot is guided to focus on hospital service information and explicitly avoid providing medical diagnoses or medication recommendations. This approach is critical in healthcare contexts to ensure safety, ethical use, and clarity of the AI system’s role.
