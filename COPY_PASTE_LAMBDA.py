"""Paste this entire file into the AWS Lambda lambda_function.py editor."""

import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def response(speech, reprompt=None, end_session=False):
    result = {
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": speech},
            "shouldEndSession": end_session,
        },
    }
    if reprompt and not end_session:
        result["response"]["reprompt"] = {
            "outputSpeech": {"type": "PlainText", "text": reprompt}
        }
    return result


def topic_from(intent):
    return intent.get("slots", {}).get("topic", {}).get("value", "").strip().lower()


def lambda_handler(event, context):
    logger.info("Request: %s", json.dumps(event))

    try:
        request = event["request"]
        request_type = request["type"]

        if request_type == "LaunchRequest":
            return response(
                "Welcome to UniMate. Ask me to explain a topic or give you a quiz. "
                "For example, say: explain cloud computing.",
                "Try saying: explain cloud computing.",
            )

        if request_type == "SessionEndedRequest":
            return {}

        intent = request["intent"]
        name = intent["name"]

        if name == "AMAZON.HelpIntent":
            return response(
                "You can say: explain machine learning, or: quiz me on cloud computing.",
                "What would you like to study?",
            )

        if name in ("AMAZON.StopIntent", "AMAZON.CancelIntent"):
            return response("Goodbye. Good luck with your studies.", end_session=True)

        if name == "AMAZON.FallbackIntent":
            return response(
                "I did not understand that. Try saying: explain cloud computing.",
                "What topic would you like help with?",
            )

        topic = topic_from(intent)

        if name == "ExplainTopicIntent":
            explanations = {
                "cloud computing": "Cloud computing means using computing services such as storage, servers, and databases over the internet instead of owning all the hardware yourself.",
                "machine learning": "Machine learning is a branch of artificial intelligence where a system learns patterns from data to make predictions or decisions.",
                "cyber security": "Cyber security is the protection of computers, networks, and information from unauthorised access, attacks, and damage.",
            }
            if topic in explanations:
                return response(explanations[topic])
            return response(
                "I do not yet have a reliable explanation for that topic. Please try cloud computing, machine learning, or cyber security.",
                "Try asking about cloud computing.",
            )

        if name == "QuizIntent":
            quizzes = {
                "cloud computing": "Here is your cloud computing quiz. Question one: name one cloud service model. Question two: what is one benefit of cloud computing?",
                "machine learning": "Here is your machine learning quiz. Question one: what is training data? Question two: what is the purpose of a model?",
            }
            if topic in quizzes:
                return response(quizzes[topic])
            return response(
                "I do not yet have a quiz for that topic. Please try cloud computing or machine learning.",
                "Which topic would you like a quiz on?",
            )

        return response("Sorry, that feature is not available yet.")

    except Exception as error:
        logger.exception("Unexpected error: %s", error)
        return response("Sorry, something went wrong. Please try again later.", end_session=True)
