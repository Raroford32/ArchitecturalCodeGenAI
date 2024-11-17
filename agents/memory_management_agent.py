from utils.memory_store import MemoryStore

class MemoryManagementAgent:
    def __init__(self):
        self.memory_store = MemoryStore()

    def get_data(self, key):
        return self.memory_store.retrieve(key)

    def set_data(self, key, value):
        self.memory_store.save(key, value)

    def delete_data(self, key):
        self.memory_store.delete(key)

    def clear_all_data(self):
        self.memory_store.clear_all()
