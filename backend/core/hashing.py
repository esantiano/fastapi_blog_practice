from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password,hashed_password)
    
    @staticmethod
    def get_password_hash(password):
        # print(len(password.encode('utf-8')))
        return pwd_context.hash(password.encode('utf-8'))