"""
    A list of responses that is used by main.py for ANNA to use

    Date: 2/21/2024
"""
import re
import random

CONST_RESPONSE: dict = {
    # Elaborate User Inputs
    "(.*)i want to (.*)": [
        "Is it really that important that you {1}?",
        "Why do you want to {1}?",
        "Can you tell me why you want to {1}?",
        "Why is it important that you {1}?",
    ],
    "(.*)reminds(.*)": [
        "What do you think is the resemblance?",
        "Do you think you know why it reminds you of that?",
        "What are the similarities?",
        "What is the connection between the two?",
        "Why does it remind you of that?"
    ],
    "(.*)but now(.*)": [
        "Do you know what caused this change?",
        "What happened to cause this change?",
    ],
    # Emotions
    "(.*)(i feel |im feeling )?(anxious|sad|sadness|bad|terrible|horrible|terrified|tired)": [
        "Do you want to talk about why you feel {2}?",
        "What makes you feel {2}?",
        "It's okay. Do you know what makes you feel {2}?"
    ],
    "(.*)(i feel |im feeling )?(happy|glad|excited)": [
        "That's good to hear! Do you know why that makes you feel {2}?",
        "Do you know what makes you feel {2}?"
    ],
    # "I ___" Responses
    "(.*)(i feel|im feeling) (.*)": [
        "What makes you feel {2}?",
        "What else do you feel besides that?",
    ],
    "(.*)i dont (.*)": [
        "Why do you not {1}?",
    ],
    "(.*)i am (.*)": [
        "What makes you so sure that you're {1}?",
        "You seem quite sure that you're {1}.",
        "Why do you think that you're {1}?",
        "What makes you think that you're {1}?",
    ],
    "(.*)i cant (.*)": [
        "Is it important for you that you {1}?",
        "Do you really want to {1}?",
        "How would you feel if you could {1}?",
    ],
    "(.*)i want (.*)": [
        "Why do you want {1}?",
        "Can you tell me why you want {1}?",
    ],
    "(.*)i could (.*)": [
        "How would you feel if you could {1}?",
        "Why is it important that you could {1}?",
    ],
    "(.*)i would (.*)": [
        "How would you feel if you could {1}?",
        "Why is it important that you could {1}?",
    ],
    "(.*)i dont know": [
        "How does it feel to not know?",
        "What is it that you don't know?",
    ],
    # Greetings
    "(hello|hi|howdy|greetings|hey)(.*)": [
        "Hello. Please tell me how you are feeling today.",
        "Hello. How are you feeling right now?",
        "Hi there. Please tell me how you are feeling today.",
        "Hi there. How are you feeling right now?",
        "Hey. Please tell me how you are feeling today.",
        "Hey. How are you feeling right now?",
    ],
    # Generic Responses
    "(yes|no)": [
        "Why is that?",
        "You seem certain of that.",
        "I see. Tell me a little more about that then.",
    ],
    "(.*) ": [
        "Tell me more about that.",
        "Go on...",
        "Please continue.",
    ],
}

CONST_RESPONSE_UNKNOWN: list = [
    "I'm sorry. I don't quite understand what you mean by that.",
    "Could you rephrase that?",
    "I don't understand what you're saying. Could you say that again?"
]


def end_chat(user_input: str) -> bool:
    """Check if the user wants to finish chatting"""
    if re.match(r"(good)?( )?bye", user_input.lower()):
        return True
    return False


def match_response(user_input: str) -> str:
    """Returns the proper response depending on the RegEx of the user_input"""
    i = clean_response(user_input)

    # Find the right list of responses to use
    # - pattern is the key
    # - response_list is the values
    for pattern, response_list in CONST_RESPONSE.items():
        matches = re.match(pattern, i)

        if matches:
            chosen_response: str = random.choice(response_list)
            return chosen_response.format(*matches.groups())

    # NO PATTERN MATCH (ANNA doesn't understand the message)
    chosen_response: str = random.choice(CONST_RESPONSE_UNKNOWN)
    return chosen_response


def clean_response(user_input: str) -> str:
    """Clean up user input before HANNAH reads (remove apostrophe, lower capitalization, etc.)"""
    user_input = user_input.replace("'", "")
    return user_input.lower()
