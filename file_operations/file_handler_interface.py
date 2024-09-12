# file_handler_interface.py

from abc import ABC, abstractmethod

class FileHandlerInterface(ABC):

    @abstractmethod
    def get_image_files(self, directory: str) -> str:
        """Recursively search for images and return the path of the temp directory."""
        pass

    @abstractmethod
    def handle_errors(self, file_path: str) -> bool:
        """Handle errors (like corrupted image files)."""
        pass
