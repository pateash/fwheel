# ashish_libs/__init__.py
import sys
import os

# Add vendor directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "vendor"))

# Now you can import the vendored packages
import faker
import click
