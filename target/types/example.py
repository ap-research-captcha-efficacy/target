"""
the only requirements of a CAPTCHA module is that it's generate function returns a tuple of (challenge, solution) strings
and that it takes one argument -- the modifiers (if there are any)
the challenge string should be a data URI
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs
prototypical implementation below:
"""

def generate(mod):
    return ("data:,lol", "swej")