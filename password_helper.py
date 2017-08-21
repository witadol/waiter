import hashlib
import os
import base64


class PasswordHelper:

    def get_hash(self, plain):
        plain = plain.encode('UTF-8')
        digest = hashlib.sha512(plain).hexdigest()
        return digest

    def get_salt(self):
        return str(base64.b64encode(os.urandom(20)))

    def validate_password(self, plain, salt, expected):
        result_sequence = plain + salt
        digest = self.get_hash(result_sequence)
        return digest == expected


if __name__ == '__main__':
    PH = PasswordHelper()
    print(PH.get_hash('aaaaa'+PH.get_salt()))