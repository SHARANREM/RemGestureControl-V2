import os
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
from utils.logger import logger
import subprocess
import sys


class PythonFileExecutor:
    def __init__(self, keyboard: KeyboardController, mouse: MouseController):
        self.keyboard = keyboard
        self.mouse = mouse

    # def execute(self, file_path: str) -> None:
    #     if not file_path:
    #         logger.error("No Python file path provided.")
    #         return

    #     if not os.path.exists(file_path):
    #         logger.error(f"Python file not found: {file_path}")
    #         return

    #     local_scope = {
    #         "keyboard": self.keyboard,
    #         "mouse": self.mouse,
    #         "Key": Key,
    #         "Button": Button,
    #         "logger": logger
    #     }

    #     safe_builtins = {
    #         "print": print,
    #         "range": range,
    #         "len": len,
    #         "int": int,
    #         "str": str,
    #         "list": list,
    #         "dict": dict,
    #         "bool": bool,
    #         "float": float
    #     }

    #     try:
    #         with open(file_path, "r", encoding="utf-8") as f:
    #             code = f.read()

    #         exec(code, {"__builtins__": safe_builtins}, local_scope)
    #         logger.info(f"Executed Python file: {file_path}")

    #     except Exception as e:
    #         logger.error(f"Error executing file {file_path}: {e}")

    def execute(self, file_path: str):
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return

        logger.info(f"Running Python file via subprocess: {file_path}")
        subprocess.Popen([sys.executable, file_path])