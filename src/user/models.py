from database import Base, intpk

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(50), nullable=False)


metadata = User.metadata
