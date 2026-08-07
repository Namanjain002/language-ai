from ai.engine import get_validated_response
from ai.openai_client import OpenAIClient
from ai.validator import InvalidAIResponse
from cli.render import render_response, render_summary
from session.inactivity import should_show_summary
from session.state import ChatSession
from session.summary import generate_summary


def run() -> None:
    client = OpenAIClient()
    session = ChatSession()

    print("Hey,What's up? \nI am your AI language assistant.\n")
    while True:
        user_message = input("> ").strip()
        if user_message.lower() in ("exit", "quit"):
            break
        if not user_message:
            continue

        if should_show_summary(session):
            render_summary(generate_summary(session))
            session.error_tally.clear()

        try:
            response = get_validated_response(client, user_message)
        except InvalidAIResponse:
            print("Sorry, having trouble right now -- try again?")
            continue

        session.record(user_message, response)
        render_response(response)


if __name__ == "__main__":
    run()