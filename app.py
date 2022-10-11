#!/usr/bin/python3
"""Project Orbit"""

import os
# go to the correct path (this file's folder)
# os.chdir(os.path.dirname(__file__)) # this is really important and should be done first
# os.chdir('..')

from orbit import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=1667)
