from database.models import async_session, User, Category, Product
from sqlalchemy import select, update, delete


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def get_product_by_category(category_id: int):
    async with async_session() as session:
        return await session.scalars(select(Product).where(Product.category == category_id))


async def get_item_by_id(item_id):
    async with async_session() as session:
        return await session.scalar(select(Product).where(Product.id == item_id))
