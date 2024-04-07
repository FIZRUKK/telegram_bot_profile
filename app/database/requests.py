from app.database.models import User, async_session
from sqlalchemy import select, func 

async def input_user(user_id, user_name, first_name, last_name, phone_number):
    async with async_session() as session:
        new_user = User(user_id=user_id, user_name=user_name, first_name=first_name, last_name=last_name, phone_number=phone_number)
        user = await session.scalar(select(User).where(User.user_id == user_id))
        if not user:
            session.add(new_user)
            await session.commit()
        
async def get_users():
    async with async_session() as session:
        users = await session.scalars(select(User))
        return users
    
async def get_id_users():
    async with async_session() as session:
        pass

async def get_user_info_by_id(user_id: int):
    async with async_session() as session:
        user = (await session.execute(select(User).where(User.user_id == user_id))).scalars().first()
        if user:
            return user.__dict__
        else:
            return None

async def get_count_users():
    async with async_session() as session:
        count = await session.scalar(func.count(User.id))
        return count