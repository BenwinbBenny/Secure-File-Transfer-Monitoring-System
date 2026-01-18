import hashlib
import os

class HashVerifier:
    @staticmethod
    def generate_sha256(path):
        if not os.path.exists(path):
            return None

        digest = hashlib.sha256()
        with open(path, "rb") as file:
            for chunk in iter(lambda: file.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()
