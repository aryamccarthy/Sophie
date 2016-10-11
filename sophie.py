from __future__ import print_function  # Python 2 compatibility
from builtins import input  # Python 2 compatibility
import readline  # For backspace in prompt.

from termcolor import colored


class Sophie(object):
    """A self-contained conversationalist."""

    def __init__(self):
        super(Sophie, self).__init__()
        self.NAME = "Sophie"
        self._prompt = colored("You: ", color='red', attrs={"bold"})
        self._prefix = colored("{}:".format(self.NAME), 'blue', attrs={"bold"})


    def converse(self):
        while True:
            remark = self.listen()
            response = self.analyze(remark)
            self.speak(response)
        
    def listen(self):
        return input(self._prompt)

    def speak(self, response):
        print(self._prefix, response)

    def analyze(self, remark):
        return 'You said "{}"!'.format(remark)


def main():
    Sophie().converse()

if __name__ == '__main__':
    main()
