class ProgrammingLanguage:
    """
    Estimated Time: 30 minutes
    Current Time: 50 minutes
    """

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        if self.reflection is True:
            reflection_str = f", Reflection={self.reflection}"
        else:
            reflection_str = ""
        return f"{self.name}, {self.typing} Typing{reflection_str}, First appeared in {self.year}"
