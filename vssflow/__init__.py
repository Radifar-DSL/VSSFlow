"""
VSSFlow
Virtual Screening workflow based on SoS workflow (Script fo Scripts)
"""

# Add imports here
from .vssflow import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
