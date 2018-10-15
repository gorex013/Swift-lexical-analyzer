class Expression:
    def dict_representation(self):
        pass


class VariableDefinition(Expression):
    def __init__(self, name, value, vtype, is_const):
        self.name = name
        self.value = value
        self.vtype = vtype
        self.is_const = is_const

    def dict_representation(self):
        return {
            'type': self.__class__,
            'name': self.name,
            'value': self.value,
            'variable_type': self.vtype,
            'const_type': self.is_const,
        }


class VariableUpdate(Expression):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def dict_representation(self):
        return {
            'type': self.__class__,
            'name': self.name,
            'value': self.value
        }


class FunctionDefinition(Expression):
    def __init__(self, name, params, rparams, fbody):
        self.name = name
        self.params = params
        self.return_params = rparams
        self.fbody = fbody

    def dict_representation(self):
        return {
            'type': self.__class__,
            'name': self.name,
            'parameters': self.params,
            'return_types': self.return_params,
            'function_body': self.fbody
        }


class FunctionCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def dict_representation(self):
        return {
            'type': self.__class__,
            'callee': self.name,
            'args': self.args
        }


class FunctionParseException(Exception):
    def __init__(self, message):
        super().__init__(message)
