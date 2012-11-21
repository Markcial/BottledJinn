#!/usr/bin/env python

import sys
import os
package_dir = "packages"
package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)
sys.path.insert(0, package_dir_path)

from bottle import Bottle
from BottledJinn import Jinn, paths

if __name__ == '__main__':
    jinn = Jinn()
    bottle = Bottle()
    bottle.mount(paths.auth_prefix, jinn)
    bottle.run(
        reloader=True,
        host='localhost',
        port=8080,
        debug=True
    )
