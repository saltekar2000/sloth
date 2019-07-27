"""
sloth
-----

sloth is a tool for labeling image and video data for computer vision research.

The documentation can be found at http://sloth.readthedocs.org/ .

"""
import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import sloth


# the following installation setup is based on django's setup.py
def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
PACKAGES, DATA_FILES = [], []
ROOT_DIR = os.path.dirname(__file__)
if ROOT_DIR != '':
    os.chdir(ROOT_DIR)
SLOTH_DIR = 'sloth'

for dirpath, dirnames, filenames in os.walk(SLOTH_DIR):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        PACKAGES.append('.'.join(fullsplit(dirpath)))
        if 'labeltool.ui' in filenames:
            DATA_FILES.append([dirpath, [os.path.join(dirpath, 'labeltool.ui')]])
    elif filenames:
        DATA_FILES.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(name='sloth',
      version=sloth.VERSION,
      description='The Sloth Labeling Tool',
      author='CV:HCI Research Group',
      url='http://sloth.readthedocs.org/',
      requires=['importlib', 'PyQt5', 'numpy'],
      packages=PACKAGES,
      data_files=DATA_FILES,
      scripts=['sloth/bin/sloth']
     )
