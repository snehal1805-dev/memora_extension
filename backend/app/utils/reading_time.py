def calculate_reading_time(text: str) -> int:

    words = len(text.split())

    reading_time = words / 200

    return max(1, round(reading_time))