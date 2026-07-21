"""AWS Lambda entry point for the UniMate Alexa Skill."""

import json
import logging

from intents import handle_intent
from responses import build_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Route an Alexa request to the appropriate UniMate handler."""
    logger.info("Incoming request: %s", json.dumps(event))

    try:
        request = event["request"]
        request_type = request["type"]

        if request_type == "LaunchRequest":
            return build_response(
                "Welcome to UniMate. You can ask for a topic explanation or a quiz. "
                "For example, say: explain cloud computing.",
                reprompt="Try saying: explain cloud computing.",
            )

        if request_type == "IntentRequest":
            return handle_intent(request["intent"])

        if request_type == "SessionEndedRequest":
            logger.info("Alexa session ended: %s", request.get("reason", "Unknown"))
            return {}

        return build_response("Sorry, UniMate could not process that request.")

    except (KeyError, TypeError) as error:
        logger.exception("Invalid Alexa request: %s", error)
        return build_response(
            "Sorry, something went wrong. Please try again later.",
            should_end_session=True,
        )
