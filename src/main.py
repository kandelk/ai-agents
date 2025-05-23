from swarm import Swarm

from agents import supervisor_agent

client = Swarm()


def run(query: str) -> str:
    try:
        print("Supervisor agent running query.")
        response = client.run(
            agent=supervisor_agent,
            messages=[{"role": "user", "content": query}],
            debug=False
        )
        return response.messages[-1]['content']
    except Exception as e:
        print(f"An error occurred while processing the query: {e}")
        return str(e)


def interactive_mode():
    print("Welcome to the Financial Assistant!")
    print("You can ask questions about stocks, companies, and financial data.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Your question: ").strip()
        if query.lower() in ['exit', 'quit']:
            print("Thank you for using the Financial Assistant. Goodbye!")
            break

        print("\nProcessing your request...\n")
        response = run(query)
        print(f"Response: {response}\n")


if __name__ == "__main__":
    interactive_mode()
