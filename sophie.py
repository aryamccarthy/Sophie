from __future__ import print_function  # Python 2 compatibility
from builtins import input  # Python 2 compatibility
import readline  # For backspace in prompt.

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
            try:
                response = self.analyze(remark)
            except RuntimeError:
                print("Alrighty then. Bye!")
                break
            self.speak(response)
        
    def listen(self):
        return input(self._prompt)

    def speak(self, response):
        print(self._prefix, response)

    def analyze(self, remark):
        return analyze(remark)
        

if __name__ == '__main__':
    Sophie().converse()
