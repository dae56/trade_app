from database import Base, intpk, str_50

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str_50]
    last_name: Mapped[str_50]
    middle_name: Mapped[str_50]
    created_at


metadata = User.metadata
