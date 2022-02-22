import os
from distutils.core import setup

scripts = ["./entry-script"] if os.environ.get("SCRIPT_WITH_PY") == "noext" else ["./entry-script.py"]


setup(name='fortytwo',
      version='1.0',
      packages=["fortytwo"],
      entry_points={"console_scripts": ["fortytwo-ep = fortytwo.__init__:entry"]},
      scripts=scripts
)
