from __future__ import print_function, unicode_literals
from PyInquirer import prompt


def prompts():
    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Link: '
        },
        {
            'type': 'list',
            'name': 'site',
            'message': 'Website',
            'choices': [
                {
                    'value': 'manga4life',
                    'name': 'Manga4Life'
                },
                {
                    'value': 'mangakakalot',
                    'name': 'MangaKakalot'
                },
            ],
            'default': 'manga4life'
        },
        {
            'type': 'input',
            'name': 'start_chapter',
            'message': 'Starting Chapter: '
        },
        {
            'type': 'input',
            'name': 'end_chapter',
            'message': 'End Chapter: '
        },
        {
            'type': 'input',
            'name': 'manga_name',
            'message': 'Name of the Manga: '
        },
        {
            'type': 'list',
            'name': 'point_five',
            'message': 'Point Fives exist? ',
            'choices': [
                {
                    'value': '1',
                    'name': 'Yes'
                },
                {
                    'value': '0',
                    'name': 'No'
                },
            ],
            'default': 'manga4life'
        },
    ]

    answers = prompt(questions)
    return answers
