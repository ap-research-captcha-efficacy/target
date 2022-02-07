import sys, os
from datetime import datetime
from secrets import token_hex

class target_model():
    def __init__(self):
        self.queue = {}
        self.types_loaded = {}
        self.invite_list = {}
        
        self.__load_types()

    def fetch_challenge(self, type, mod = None):
        try:
            (challenge, solution) = getattr(self.types_loaded[type], "generate")(mod)
            token = token_hex(64)
            self.queue[token] = (solution, datetime.now().timestamp())
            return (challenge, token)
        except Exception as e:
            print(e)
            return False

    def verify_solution(self, proposed, token):
        if not(proposed) or not(token):
            return (False, "missing proposal or token")
        if not self.queue.get(token):
            return (False, "invalid token")
        if (datetime.now().timestamp() - self.queue[token][1]) > 60:
            self.queue.pop(token)
            return (False, "token timed out")
        if not(self.queue[token][0] == proposed):
            self.queue.pop(token)
            return (False, "incorrect")
        passport = (token_hex(64), datetime.now().timestamp())
        self.invite_list[passport[0]] = passport[1]
        return (True, passport)

    def verify_passport(self, proffered):
        return (proffered and 
        bool(self.invite_list.get(proffered)) and 
        (datetime.now().timestamp() - self.invite_list.get(proffered)) < 60**2)

    def __load_types(self):
        sys.path.append("./target/types")
        types = [name.split(".py")[0] for name in os.listdir("./target/types") if name.endswith(".py")]
        for type in types:
            try:
                module = __import__(type)
            except: 
                print(f"error loading type {type}")
                continue
            if not(hasattr(module, "generate")):
                print(f"type {type} is invalid: crucial attribute missing!")
                continue
            else:
                self.types_loaded[module.__name__] = module
                print(f"loaded type {module.__name__}")