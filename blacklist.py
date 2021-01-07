"""
blacklist.py
This file contains the blacklist of the JWT tokens. It will be imported by
app.py and the logout resource so that tokens are added to the blacklist when the
user logs out.
"""

BLACKLIST = set()
