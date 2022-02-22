import os
from distutils.core import setup

scritps = ["hello_you"] if not os.environ.get("SCRIPT_WITH_PY") else ["hello_you.py"]


setup(name='fortytwo',
      version='1.0',
      packages=["fortytwo"],
      scripts=scripts
)
