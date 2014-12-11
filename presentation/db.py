from utils import render_code

branching = """
def branch(length=100):
    …
    branch(length * 0.6)
    …
"""

nodereplacement = """
def left_hilbert(length, width):
    …
    right_hilbert(length - 1, width)
    …
    left_hilbert(length - 1, width)
    …
    left_hilbert(length - 1, width)
    …
    right_hilbert(length - 1, width)
"""

lsystems = """
def X(n): 
  if n > 0:
      xn = X(n-1)
      fn = F(n-1)
      return ''.join([xn,'+',xn,'+',fn])
  else:
      return 'X'
"""

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
          'id': 'paintbrush',
          'animation': 'slide',
          'x': '1000',
          'y': '1500',
          'z': '1500',
          'rotate': '145',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Our Paintbrush</h2>
            <h2><code>{code}</code></h2>
            <small>(available in python 2.7 &amp; 3.4)</small>
          """.format(code=render_code('import turtle as t'))
        },
        {
          'id': 'fractals',
          'animation': 'slide',
          'x': '1500',
          'y': '-1500',
          'z': '1500',
          'rotate': '145',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Fractals</h2>
            <img src='/static/img/broccoli.jpg' />
          """
        },
        {
          'id': 'morefractals',
          'animation': 'slide',
          'x': '2500',
          'y': '-2500',
          'z': '2500',
          'rotate': '145',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Fractal Curves</h2>
            <img src='/static/img/coral.png' />
            <!-- <img src='/static/img/DragonCurve_animation.gif' />-->
          """
        },
        {
          'id': 'fractaldimensions',
          'animation': 'slide',
          'x': '3500',
          'y': '-3500',
          'z': '3500',
          'rotate': '145',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Fractal Dimensions</h2>
            <img src='/static/img/dimensions.png' />
          """
        },
        {
          'id': 'drawsome',
          'animation': 'slide',
          'x': '4500',
          'y': '-4500',
          'z': '4500',
          'rotate': '145',
          'rotate_x': '0',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Let’s draw some fractals!</h2>
          """
        },
        {
          'id': 'basicbranching',
          'animation': 'slide',
          'x': '5500',
          'y': '-5500',
          'z': '5500',
          'rotate': '245',
          'rotate_x': '24',
          'rotate_y': '145',
          'scale': 0,
          'content': """
            <h2>Basic Branching</h2>
            <img src='/static/img/branching.png' />
            {code}
          """.format(code=render_code(branching))
        },
        {
          'id': 'nodereplacement',
          'animation': 'slide',
          'x': '7500',
          'y': '-7500',
          'z': '7500',
          'rotate': '45',
          'rotate_x': '4',
          'rotate_y': '45',
          'scale': 0,
          'content': """
            <h2>Node Replacement</h2>
            <img src='/static/img/nodereplacement.png' />
            <small>{code}</small>
          """.format(code=render_code(nodereplacement))
        },
        {
          'id': 'lsystems',
          'animation': 'slide',
          'x': '8500',
          'y': '-8500',
          'z': '8500',
          'rotate': '145',
          'rotate_x': '40',
          'rotate_y': '145',
          'scale': 0,
          'content': """
            <h2>L-Systems</h2>
            <img src='/static/img/lsystems.png' />
            <small>{code}</small>
          """.format(code=render_code(lsystems))
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
