from sqlalchemy.orm import Session
from schemas.user import UserCreate, DuplicateUserError
from db.models.user import User
from core.hashing import Hasher

def create_new_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        # Raise our custom exception
        raise DuplicateUserError(f"A user with email '{user.email}' already exists.")
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user