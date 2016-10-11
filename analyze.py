#!/usr/bin/python
# -*- coding: latin-1 -*-
from random import choice
import re

translations = {
    "are": "am",
    "am": "are",
    "were": "was",
    "was": "were",
    "you": "I",
    "i": "you",
    "your": "my",
    "my": "your",
    "i've": "you have",
    "you've": "I have",
    "i'm": "you are",
    "you're": "I am"
}

replies = {
    r"Can you ([^\?]*)\??": [
        "Don't you believe I can {}?",
        "Perhaps you would like to be able to {}.",
        "You want me to be able to {}?"
    ],
    r"Can I ([^\?]*)\??": [
        "Perhaps you don't want to {}",
        "Do you want to be able to {}"
    ],
    r"You are (.*)": [
        "What makes you think I am {}?",
        "Does it please you to believe that I am {}?",
        "Perhaps you would like to be {}?"
    ],
    r"You'?re (.*)": [
        "Do you sometimes wish you were {}?"
    ],
    r"I don'?t (.*)": [
        "Don't you really {}?",
        "Why don't you {}?",
        "Do you wish to be able to {}?",
        "Don't you wish to be able to {}?"
    ],
    r"I feel (.*)": [
        "Does that trouble you?",
        "Tell me more about such feelings.",
        "Do you often feel {}?",
        "Do you enjoy feeling {}?"
    ],
    r"Why don'?t you (.*)": [
        "Do you really believe I don't {}?",
        "Perhaps in good time I will {}",
        "Do you want me to {}?",
        "How did you know I can't {}?"
    ],
    r"Why can'?t I ([^\?]*)\??": [
        "Do you think you should be able to {}?",
        "Why can't you {}?"
    ],
    r"Are you ([^\?]*)\??": [
        "Why are you interested in whether or not I am {}?",
        "Would you prefer if I were not {}?",
        "Perhaps in your fantasies I am {}"
    ],
    r"I can'?t (.*)": [
        "Have you tried?",
        "Perhaps you can now {}",
    ],
    r"I am (.*)": [
        "Did you come to me because you are {}?",
        "How long have you been {}?",
        "Do you believe it is normal to be {}?",
        "Do you enjoy being {}?"
    ],
    r"I'm (.*)": [
        "Did you come to me because you are {}?",
        "How long have you been {}?",
        "Do you believe it is normal to be {}?",
        "Do you enjoy being {}?"
    ],
    r"You (.*)": [
        u"We were discussing you–not me.",
        "Oh, I {}",
        "You're not really talking about me, are you?"
    ],
    r"I want (.*)": [
        "What would it mean if you got {}?",
        "Why do you want {}?",
        "Suppose you soon got {}?",
        "What if you never got {}?",
        "I sometimes also want {}.",
    ],
    r"What ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"How ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"Who ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"Where ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"When ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"Why ([^\?]*)\??": [
        "Why do you ask?",
        "Does that question interest you?",
        "What answer would please you the most?",
        "What do you think?",
        "Are such questions on your mind often?",
        "What is it you really want to know?",
        "Have you asked anyone else?",
        "Have you asked such questions before?",
        "What else comes to mind when you ask that?",
    ],
    r"(.*) name(.*)": [
        "Names don't interest me.",
        "I don't care about names. Go on."
    ],
    r".*cause(.*)": [
        "Is that the real reason?",
        "Don't any other reasons come to mind?",
        "Does that reason explain anything else?",
        "What other reason might there be?"
    ],
    r"(.*)sorry(.*)": [
        "Please don't apologize.",
        "Apologies are not necessary.",
        "What feelings do you get when you apologize?",
        "Don't be so defensive!"
    ],
    r"(.*) dream(s|ed|t)?(.*)": [
        "What does that dream suggest to you?",
        "Do you dream often?",
        "What persons appear in your dreams?",
        "Are you disturbed by your dreams?",
    ],
    r"Hello(.*)": [
        "How do you do? Please state your problem.",
    ],
    r"Hi(.*)": [
        "How do you do? Please state your problem.",
    ],
    r"^Hey(.*)": [
        "How do you do? Please state your problem.",
    ],

    r".*\bmaybe\b(.*)": [
        "You don't seem quite certain.",
        "Why the uncertain tone?",
        "Can't you be more positive?",
        "You aren't sure?",
        "Don't you know?"
    ],
    r".*\bno\b.*": [
        "Are you saying that just to be negative?",
        "You are being a bit negative.",
        "Why not?",
        "Are you sure?",
        "Why no?",
    ],
    r".*\b[Yy]our\b(.*)": [
        "Are you concerned about my {}?",
        "What about your own {}?"
    ],
    r".*\balways\b.*": [
        "Can you think of a specific example?",
        "When?",
        "What are you thinking of?",
        "Really, always?"
    ],
    r".*\bthink (.*)": [
        "Do you really think so?",
        "But you are not sure you {}",
        "Do you doubt you {}?"
    ],
    r".*\balike\b.*": [
        "In what way?",
        "What resemblance do you see?",
        "What does the similarity suggest to you?",
        "What other connections do you see?",
        "Could there really be some connection?"
    ],
    r".*\byes\b.*": [
        "You seem quite positive.",
        "Are you sure?",
        "I see.",
        "I understand."
    ],
    r".*\bfriends?\b.*": [
        "Why do you bring up the topic of friends?",
        "Do your friends worry you?",
        "Do your friends pick on you?",
        "Are you sure you have any friends?",
        "Do you ipose on your friends?",
        "Perhaps your love for friends worries you?"
    ],
    r".*\bcomputers?\b.*": [
        "Do computers worry you?",
        "Are you talking about me in particular?",
        "Are you frightened by machines?",
        "Why do you mention computers?",
        "What do you think computers have to do with your problem?",
        "Don't you think computers can help people?",
        "What is it about machines that worries you?",
    ],
    r"(.*)": [
        "Say, do you have any psychological problems?",
        "What does that suggest to you?",
        "I see.",
        "I'm not sure I understand you fully.",
        "Come, come. Elucidate your thoughts.",
        "Can you elaborate on that?",
        "That is quite interesting.",
        "Please tell me more.",
        "Let's change focus a bit... Tell me about your family.",
        "Can you elaborate on that?",
        'Why do you say "{0}"?',
        "I see.",
        "Very interesting.",
        "So {0}. Huh.",
        "I see. And what does that tell you?",
        "How does that make you feel?",
        "How do you feel when you say that?",
        "What a silly thing to say!",
    ]
}

farewells = {"bye", "goodbye", "shut up", "fuck you", "fuck off", "go away", "exit", "quit"}

def translated(span):
    tokens = span.lower().split()
    modified = [translations.get(w, w) for w in tokens]
    return ' '.join(modified)


def analyze(remark):
    remark = remark.rstrip(".!")
    for statement in farewells:
        if remark.lower().startswith(statement):
            raise RuntimeError
    for pattern, answers in replies.items():
        match = re.match(pattern, remark.lower())
        if match:
            result = choice(answers)
            return result.format(*[translated(x) for x in match.groups()])
