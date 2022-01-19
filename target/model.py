import sys, os
from secrets import token_hex

class target_model():
    def __init__(self):
        self.queue = {}
        self.types_loaded = {}

        self.__load_types()

    def fetch_challenge(self, type):
        try:
            (challenge, solution) = getattr(self.types_loaded[type], "generate")()
            token = token_hex(64)
            self.queue[token] = solution
            return (challenge, token)
        except Exception as e:
            print(e)
            return False

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