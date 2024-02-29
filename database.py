from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
str_50 = Annotated[str, mapped_column(String(50))]


class Base(DeclarativeBase):
    pass
