from .util import monkeypatch

class FlakeConfigToml:
    def __init__(self, tree):
        pass

    def __iter__(self):
        raise StopIteration()

    def run(self, *args) -> List[Any]:
        return []

    def add_options(self, *args):
        monkeypatch()
