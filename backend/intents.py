"""Intent routing and feature logic for UniMate."""

from responses import build_response
from utils import get_slot_value, normalise_topic

TOPIC_EXPLANATIONS = {
    "cloud computing": (
        "Cloud computing means using computing services such as servers, storage, "
        "and databases over the internet, rather than owning all hardware yourself."
    ),
    "machine learning": (
        "Machine learning is a branch of artificial intelligence in which systems "
        "learn patterns from data to make predictions or decisions."
    ),
    "cyber security": (
        "Cyber security is the protection of computers, networks, and data from "
        "unauthorised access, attacks, or damage."
    ),
}

QUIZZES = {
    "cloud computing": (
        "Here is your cloud computing quiz. Question one: name one cloud service model. "
        "Question two: what is one benefit of cloud computing?"
    ),
    "machine learning": (
        "Here is your machine learning quiz. Question one: what is training data? "
        "Question two: what is the purpose of a model?"
    ),
}


def handle_intent(intent):
    """Return an Alexa response for the supplied intent object."""
    intent_name = intent.get("name", "")

    if intent_name == "AMAZON.HelpIntent":
        return build_response(
            "You can ask me to explain a computing topic or create a quiz. "
            "For example, say: explain machine learning.",
            reprompt="What would you like help with?",
        )

    if intent_name in {"AMAZON.StopIntent", "AMAZON.CancelIntent"}:
        return build_response("Goodbye. Good luck with your studies.", should_end_session=True)

    if intent_name == "AMAZON.FallbackIntent":
        return build_response(
            "I did not understand that. You can say: explain cloud computing.",
            reprompt="Try asking for a topic explanation or a quiz.",
        )

    if intent_name == "ExplainTopicIntent":
        return explain_topic(intent)

    if intent_name == "QuizIntent":
        return create_quiz(intent)

    return build_response("Sorry, that feature is not available yet.")


def explain_topic(intent):
    """Provide a concise explanation for a supported topic."""
    topic = normalise_topic(get_slot_value(intent, "topic"))
    explanation = TOPIC_EXPLANATIONS.get(topic)
    if explanation:
        return build_response(explanation)

    return build_response(
        "I do not yet have a reliable explanation for " + (topic or "that topic") +
        ". Please try cloud computing, machine learning, or cyber security.",
        reprompt="Try asking about cloud computing.",
    )


def create_quiz(intent):
    """Provide a short quiz for a supported topic."""
    topic = normalise_topic(get_slot_value(intent, "topic"))
    quiz = QUIZZES.get(topic)
    if quiz:
        return build_response(quiz)

    return build_response(
        "I do not yet have a quiz for " + (topic or "that topic") +
        ". Please try cloud computing or machine learning.",
        reprompt="Which topic would you like a quiz on?",
    )
