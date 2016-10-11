import readline  # For backspace in prompt.
from .termcolor import colored

PARTNER_NAME = "Sophie"


def analyze(user_input: str) -> str:
    return user_input


def get_input() -> str:
    prompt = colored("You: ", color='red', attrs={"bold"})
    return input(prompt)


def print_response(response: str) -> ():
    prefix = colored("{}:".format(PARTNER_NAME), 'blue', attrs={"bold"})
    print(prefix, response)


def main():
    while True:
        user_input = get_input()
        response = analyze(user_input)
        print_response(response)

if __name__ == '__main__':
    main()
