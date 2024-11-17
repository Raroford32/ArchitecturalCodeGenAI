import os
import shutil
from utils.memory_store import MemoryStore

class IntegrationAgent:
    def __init__(self):
        self.memory_store = MemoryStore()
        self.src_dir = 'output/src'
        self.build_dir = 'output/build'

    def integrate_code(self):
        os.makedirs(self.build_dir, exist_ok=True)
        code_files = [f for f in os.listdir(self.src_dir) if f.endswith('.py')]
        modules = {}
        for file_name in code_files:
            src_file_path = os.path.join(self.src_dir, file_name)
            with open(src_file_path, 'r') as src_file:
                code = src_file.read()
                modules[file_name] = code
        # Simple integration logic: Copy files to build directory
        for file_name, code in modules.items():
            build_file_path = os.path.join(self.build_dir, file_name)
            with open(build_file_path, 'w') as build_file:
                build_file.write(code)
        print(f"Integrated code is available in '{self.build_dir}' directory.")
