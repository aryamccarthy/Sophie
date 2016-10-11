from __future__ import print_function  # Python 2 compatibility
from builtins import input  # Python 2 compatibility
import readline  # For backspace in prompt.
from sys import exit

from analyze import analyze

try:
    from termcolor import colored
except ImportError:
    print("Please install `termcolor`.", 
        "This can be done with `pip install termcolor`.")
    def colored(text, *args, **kwargs):
        return text


class Sophie(object):
    """A self-contained conversationalist."""

    def __init__(self):
        super(Sophie, self).__init__()
        self.NAME = "Sophie"
        self._prompt = colored("You: ", color='red', attrs={"bold"})
        self._prefix = colored("{}:".format(self.NAME), 'blue', attrs={"bold"})


    def converse(self):
        self.speak("Hi! I'm {}. What's on your mind?".format(self.NAME))
        while True:
            remark = self.listen()
            response = self.analyze_or_die(remark)
            self.speak(response)
        
    def listen(self):
        try:
            return input(self._prompt)
        except (EOFError, KeyboardInterrupt):  # ctrl-D, ctrl-C
            print()
            self.speak("Harsh! Can't you wish me a proper goodbye?")
            return self.listen()

    def speak(self, response):
        print(self._prefix, response)

    def analyze_or_die(self, remark):
        try:
            return analyze(remark)
        except RuntimeError:
            self.speak("Alrighty then. Bye!")
            exit()

        

if __name__ == '__main__':
    Sophie().converse()
