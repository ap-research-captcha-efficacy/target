"""
the only requirement of a CAPTCHA module is that it returns a tuple of (challenge, solution) strings
the challenge string should be a data URI
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs
"""

def generate():
    return ("data:,lol", "swej")