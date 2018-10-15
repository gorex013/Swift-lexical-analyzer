class Condition:
    def __init__(self, value):
        self.value = value

    def dict(self):
        return '"condition":{' + self.value + '}'


class ConditionList:
    def __init__(self):
        self.condition_list = []

    def add_condition(self, condition: Condition):
        self.condition_list.append(condition)

    def add_condition_list(self, condition_list: list):
        for e in condition_list:
            self.add_condition(e)

    def dict(self):
        result = '"condition-list":{'
        for e in self.condition_list:
            result += e.dict() + ','
        result += '}'
        return result
