class Hello:
    def __init__(self, str):
        pass
        self.str = str

class B (Hello):
    def __init__(self, str):
        pass
        super().__init__(str)