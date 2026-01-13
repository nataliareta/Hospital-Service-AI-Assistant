#Author: Natalia Reta Budiarti

from agent.hospital import create_agent

import os
print(os.getenv("GOOGLE_API_KEY"))

def main():
    agent = create_agent()
    print("Still running, please wait.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)
        print(f"Assistant: {response}\n")

if __name__ == "__main__":
    main()