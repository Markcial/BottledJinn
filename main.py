#!/usr/bin/env python

import sys, os
package_dir = "packages"
package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)
sys.path.insert(0, package_dir_path)

from BottledJinn import Jinn
from bottle import debug

jinn = Jinn()
debug( True )
jinn.run(reloader=True,host='localhost', port=8080)
