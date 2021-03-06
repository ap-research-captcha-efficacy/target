from flask import (
    Blueprint, g, redirect, request, session, url_for, make_response
)
from markupsafe import escape

from .model import target_model

t = target_model()
bp = Blueprint("routes", __name__)

@bp.route("/")
def root():
    return "YOU" if t.verify_passport(request.args.get("passport")) else "HAZE"

@bp.route("/captchas")
def captchas():
    res = []
    for type in t.types_loaded.keys():
        res.append(type)
        try:
            mods = getattr(t.types_loaded[type], "valid_mods")
            for mod in mods:
                res.append(type+"?modifiers="+mod)
        except Exception as e:
            print(e)
    return {"captchas": res}

@bp.route("/captcha/<type>")
def captcha(type):
    chal = t.fetch_challenge(type, mod = request.args.get("modifiers"))
    if not chal:
        return make_response("oops~ (fetch_challenge failed, probably the fault of the module)", 500)
    return {"challenge": chal[0], "token": chal[1]}

@bp.route("/solution")
def solution():
    ans = t.verify_solution(request.args.get("proposal"), request.args.get("token"))
    if not ans[0]:
        return make_response(ans[1], 401)
    return {"passport_token": ans[1][0], "passport_issued": ans[1][1]}