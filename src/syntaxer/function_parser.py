class Function:
    def __init__(self, name, params, rparams, fbody):
        self.name = name
        self.params = params
        self.return_params = rparams
        self.fbody = fbody


class FunctionParseException(Exception):
    def __init__(self, message):
        super().__init__(message)


def parse():
    pass