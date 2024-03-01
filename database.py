import datetime

from sqlalchemy import String, text
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]
str_50 = Annotated[str, mapped_column(String(50))]


class Base(DeclarativeBase):
    pass
