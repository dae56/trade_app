from database import Base, intpk

from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = "users"


