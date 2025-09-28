from settings import settings
from src.assistants import supervisor
from src.aux_methods import pretty_print_messages, get_user_input
from src.strings import WELCOME_MESSAGE


def do() -> None:
    """Main function to run the supervisor assistant."""
    last_chunk = None

    # Get user input and create an initial message
    initial_messages = [
        {
            "role": "user",
            "content": get_user_input(WELCOME_MESSAGE.format(language=settings.LANGUAGE)),
        }
    ]

    # Stream responses from supervisor
    for response_chunk in supervisor.stream({"messages": initial_messages}):
        pretty_print_messages(response_chunk, show_last_message_only=True)
        last_chunk = response_chunk

    # Print final message history
    if last_chunk and "supervisor" in last_chunk:
        final_messages = last_chunk["supervisor"]["messages"]
        for message in final_messages:
            message.pretty_print()

def check_settings() -> bool:
    """Check if all required settings are set."""
    if not settings.OPENAI_BASE_URL:
        print("OpenAI base URL not set.")
        return False

    if not settings.TAVILY_API_KEY:
        print("TAVILY API key not set.")
        return False

    return True


def main() -> None:
    if check_settings():
        do()


if __name__ == "__main__":
    main()
