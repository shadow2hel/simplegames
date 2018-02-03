import sys
import random

answers = [
        ["Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"],
        ["Reply hazy try again",
                "Ask again later", "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again"
                ],
        ["It is certain",
             "It is decidedly so",
             "Without a doubt",
             "Yes definitely",
             "You may rely on it"]
]

while True:
    print("Ask me a question, any question:")
    question = input()

    list_length = random.randrange(0, len(answers))
    random_column = answers[list_length]
    elements_length = random.randrange(0, len(random_column))
    answer = answers[list_length][elements_length]

    print(answer)
    print("\r\n")
