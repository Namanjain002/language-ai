from session.state import ChatSession

DEFAULT_INACTIVITY_THRESHOLD_SECONDS = 90 * 60  # 1.5 hours


def should_show_summary(
    session: ChatSession,
    threshold_seconds: float = DEFAULT_INACTIVITY_THRESHOLD_SECONDS,
) -> bool:
    if not session.history:
        return False
    return session.seconds_since_last_activity() >= threshold_seconds