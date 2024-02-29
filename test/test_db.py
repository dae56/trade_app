import asyncio

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine
from database import Base


class TestTable(Base):
    __tablename__ = 'test_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    year_old: Mapped[int]


async def async_main() -> None:
    engine = create_async_engine("postgresql+asyncpg://postgres:qwerty@localhost:5432/trade_app")

    async with engine.begin() as connection:
        await connection.run_sync(TestTable.metadata.create_all)

asyncio.run(async_main())
