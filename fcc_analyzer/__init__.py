"""
fcc_analyzer
GUI to analyze TI spectra from FCclasses code
"""

# Add imports here
from .fcc_analyzer import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
