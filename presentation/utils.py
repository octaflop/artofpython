# encoding: utf-8

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def render_code(pycode):
    return highlight(pycode, PythonLexer(), HtmlFormatter())
