from flask import Blueprint
from markupsafe import escape

from .model import target_model

t = target_model()
bp = Blueprint("routes", __name__)

@bp.route("/")
def root():
    return "hello, world!"

@bp.route("/captchas")
def captchas():
    return {"captchas": list(t.types_loaded.keys())}
@bp.route("/captcha/<type>")
def captcha(type):
    chal = t.fetch_challenge(type)
    return {"challenge": chal[0], "token": chal[1]}

@bp.route("/solution")
def solution():
    return "asdasD"