"""Helpers for creating valid Alexa speech responses."""


def build_response(speech, reprompt=None, should_end_session=False):
    """Create the JSON response format expected by Alexa."""
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": speech},
            "shouldEndSession": should_end_session,
        },
    }

    if reprompt and not should_end_session:
        response["response"]["reprompt"] = {
            "outputSpeech": {"type": "PlainText", "text": reprompt}
        }
    return response
