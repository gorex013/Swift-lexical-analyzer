class FunctionDefinition:
    def __init__(self, name, params, rparams, fbody):
        self.name = name
        self.params = params
        self.return_params = rparams
        self.fbody = fbody # TODO: IT SHOULD BE AN EXPRESSION OBJECT

    def dict_representation(self):
        return {
            'name': self.name,
            'parameters': self.params,
            'return_types': self.return_params,
            'function_body': self.fbody
        }


class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def dict_representation(self):
        return {
            'callee': self.name,
            'args': self.args
        }


class FunctionParseException(Exception):
    def __init__(self, message):
        super().__init__(message)


def parse():
    pass