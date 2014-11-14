# encoding: utf-8

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

db = {
    'slides': [
        {
        'id': 'prestitle',
        'animation': 'slide',
        'x': '-1000',
        'y': '-1500',
        'scale': 1,
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
        'scale': 1,
        'content': """
            <q>Don't you think that presentations given <strong>in modern browsers</strong> shouldn't <strong>copy the limits</strong> of 'classic' slide decks?</q>
        """
        },
    ]
}