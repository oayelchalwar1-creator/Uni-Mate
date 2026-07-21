"""Small reusable functions used by the Lambda backend."""


def get_slot_value(intent, slot_name):
    """Return a slot's recognised value, or an empty string when it is missing."""
    return intent.get("slots", {}).get(slot_name, {}).get("value", "")


def normalise_topic(topic):
    """Make user input safe and consistent for dictionary lookups."""
    return topic.strip().lower() if topic else ""
