from typing import List

from core.model import AIResponse


def render_response(response: AIResponse) -> None:
    if response.has_error:
        print("+-- correction " + "-" * 40)
        print(f"| {response.corrected_text}")
        print(f"| ({response.explanation})")
        print("+" + "-" * 54)
        print(response.reply)
    else:
        print(response.reply)


def render_summary(weak_areas: List[str]) -> None:
    print("\n--- while you were away ---")
    if not weak_areas:
        print("No recurring grammar mistakes noticed. Nice work!")
    else:
        print("Areas to work on: " + ", ".join(weak_areas))
    print("---------------------------\n")