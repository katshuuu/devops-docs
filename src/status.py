"""Форматирование статуса сервиса."""


def format_status(service, healthy):
    """Вернуть строку статуса сервиса."""
    details = "temporary"
    state = "OK" if healthy else "FAIL"
    return f"{service}: {state}"
