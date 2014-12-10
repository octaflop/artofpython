from utils import render_code

db = {
    'slides': [
        {
          'id': 'title',
          'animation': 'slide',
          'x': '0',
          'y': '0',
          'z': '0',
          'rotate': '0',
          'rotate_x': '0',
          'rotate_y': '0',
          'scale': 0,
          'content': """
          <h1>The Art of Python</h1>
          <h2>Faris Chebib</h2>
          <h3>2014-12-10</h3>
          """
        },
        {
          'id': 'art',
          'animation': 'slide',
          'x': '0',
          'y': '1000',
          'z': '-500',
          'rotate': '0',
          'rotate_x': '180',
          'rotate_y': '180',
          'scale': 0,
          'content': """
            <q>Aren’t you just <b>bored</b> with all those slides-based presentations?</q>
            {code}
          """.format(code=render_code('[x.first_name, x.last_name for x in people]'))
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
            <q>Don’t you think that presentations given <strong>in modern browsers</strong> 
            shouldn’t <strong>copy the limits</strong> of ‘classic’ slide decks?</q>
        """
        },
        {
          'id': 'resources',
          'animation': 'slide',
          'x': '0',
          'y': '1500',
          'z': '1500',
          'rotate': '45',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Resources</h2>
            <ul>
              <li>
                <a href='http://www.fractalcurves.com/'>Brain-Filling Curves</a>
              </li>
              <li>
                <a href='http://algorithmicbotany.org/papers/#abop'>The Algorithmic Beauty of Plants</a>
              </li>
            </ul>
          """
        },
        {
          'id': 'overview',
          'animation': 'slide',
          'x': '0',
          'y': '0',
          'z': '0',
          'rotate': '0',
          'rotate_x': '0',
          'rotate_y': '0',
          'scale': 0
        }
    ]
}
