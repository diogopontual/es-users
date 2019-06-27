from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json


class Negotiator:
    questions = [
        {
            'type': 'input',
            'name': 'host',
            'message': 'What is the elasticsearch url?',
        },
    {
            'type': 'input',
            'name': 'username',
            'message': 'What is the elasticsearch username?',
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'What is the elasticsearch password?',
        },
        {
            'type': 'input',
            'name': 'proxy',
            'message': 'And what about the proxy?',
        }
    ]

    def get_es_data(self):
        answers = prompt(self.questions)
        return answers;

