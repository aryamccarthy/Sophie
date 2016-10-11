#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
import readline  # For backspace in prompt.

from analyze import analyze
from sendmail import Sendmail  # PyPI's version is not Python3 ready.
from termcolor import colored

# For Python 2 compatibility:
try:
    input = raw_input
except NameError:
    pass


NAME = "Sophie"
PROMPT = colored("You: ", color='red', attrs={"bold"})
PREFIX = colored("{}:".format(NAME), 'blue', attrs={"bold"})
conversation = []


def converse():
    """Maintains machinery of the conversation."""
    speak("Hi! I'm {}. What's on your mind?".format(NAME))
    while True:
        remark = listen()
        response = analyze_or_die(remark)
        speak(response)


def listen():
    """Let the user tell you what's up."""
    try:
        user_input = input(PROMPT)
        conversation.append(user_input)
        return user_input
    except (EOFError, KeyboardInterrupt):  # ctrl-D, ctrl-C
        print()
        speak("Hold on. Why don't we say a proper goodbye?")
        return listen()


def speak(response):
    """Sophie prints to the console."""
    print(PREFIX, response)
    conversation.append(response)


def analyze_or_die(remark):
    """Process the input, or go away if the user wants to quit."""
    try:
        return analyze(remark)
    except RuntimeError:
        wrap_up()


def email_conversation():
    """Let me see what else Sophie needs to learn."""
    Sendmail().sendmail(from_addr="",
                        to_addrs=["aryadevin@icloud.com"],
                        msg="\n".join(conversation))


def wrap_up():
    """Tear it all down."""
    speak("Alrighty then. Bye!")
    email_conversation()
    exit()


if __name__ == '__main__':
    converse()
