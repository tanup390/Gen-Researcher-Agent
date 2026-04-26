from app.agents.basic_agent import BasicAgent

agent = BasicAgent()

while True:
    query = input("\nAsk something (or type 'exit'): ")

    if query.lower() == "exit":
        break

    result = agent.run(query)
    print("\nAgent:\n", result)