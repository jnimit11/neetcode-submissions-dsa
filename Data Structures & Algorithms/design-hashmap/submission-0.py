
class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for pair in self.data:
            if pair[0] == key:
                pair[1] = value
                return

        self.data.append([key, value])

    def get(self, key: int) -> int:
        for pair in self.data:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        for pair in self.data:
            if pair[0] == key:
                self.data.remove(pair)
                return
