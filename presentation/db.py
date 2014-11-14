# encoding: utf-8

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

db = {
    'slides': [
        {
        'id': 'home',
        'animation': 'slide',
        'x': '-1000',
        'y': '-1500',
        'z': '0',
        'rotate_x': '-10',
        'rotate_y': '-40',
        'scale': 10,
        'content': """
            <q>Aren't you just <b>bored</b> with all those slides-based presentations?</q>
            {code}
        """.format(code=highlight('print("Hello World")', PythonLexer(), HtmlFormatter()))
        },
        {
        'id': '',
        'animation': 'slide',
        'x': '0',
        'y': '-1500',
        'rotate_x': '-100',
        'rotate_y': '-40',
        'scale': 2,
        'content': """
            <q>Don't you think that presentations given <strong>in modern browsers</strong> shouldn't <strong>copy the limits</strong> of 'classic' slide decks?</q>
        """
        },
    ]
}