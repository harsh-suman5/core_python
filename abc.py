from abc import ABC, abstractmethod
class harsh(ABC):
    @abstractmethod
    def body(self):
        print("abstraction method learning started")
        return
    def harsh(self):
        print("concrete method started learning by harsh")
harsh.body(self= harsh)

