# SQL - язык баз данных
# MySQL, PostgreSQL, SQLite - СУБД, система управления базой данных
# MongoDB, Redis

"""
База данных: Hospital
Таблицы: Patient, Doctor, Appointment

Patient: Name, Surname, Birthday, Phone, Email, Address
Doctor: Name, Surname, Work experience, Specialization
Appointment: Date, Time, Patient, Doctor

Patient data:
Ivan, Ivanovich, 1990-01-01, 89098765432, <EMAIL>, Moscow

SELECT (name, surname) FROM patient WHERE phone = '89098765432';

SQLAlchemy, ORM

{"name": "John"}

"""

from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine("sqlite+aiosqlite:///shop.db", echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    phone_number: Mapped[str] = mapped_column(String(15), nullable=True)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(1024))
    price: Mapped[int]
    category: Mapped[int] = mapped_column(ForeignKey("categories.id"))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
