#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
from subprocess import Popen
import readline  # For backspace in prompt.
from sys import exit

from analyze import analyze
from sendmail import Sendmail
try:
    from termcolor import colored
except ImportError:
    print("Please install `termcolor`.", 
        "This can be done with `pip install termcolor`.")
    def colored(text, *args, **kwargs):
        return text

# For Python 2 compatibility:
try:
    input = raw_input
except NameError:
    pass


class Sophie(object):
    """A self-contained conversationalist."""

    def __init__(self):
        super(Sophie, self).__init__()
        self.NAME = "Sophie"
        self._prompt = colored("You: ", color='red', attrs={"bold"})
        self._prefix = colored("{}:".format(self.NAME), 'blue', attrs={"bold"})
        self.conversation = []

    def converse(self):
        self.speak("Hi! I'm {}. What's on your mind?".format(self.NAME))
        while True:
            remark = self.listen()
            response = self.analyze_or_die(remark)
            self.speak(response)
        
    def listen(self):
        try:
            user_input = input(self._prompt)
            self.conversation.append(user_input)
            return user_input
        except (EOFError, KeyboardInterrupt):  # ctrl-D, ctrl-C
            print()
            self.speak("Hold on. Why don't we say a proper goodbye?")
            return self.listen()

    def speak(self, response):
        print(self._prefix, response)
        self.conversation.append(response)

    def analyze_or_die(self, remark):
        try:
            return analyze(remark)
        except RuntimeError:
            self.speak("Alrighty then. Bye!")
            self.wrap_up()
            exit()

    def wrap_up(self):
        Sendmail().sendmail(from_addr="",
            to_addrs=["aryadevin@icloud.com"],
            msg = "\n".join(self.conversation))

        

if __name__ == '__main__':
    Sophie().converse()
