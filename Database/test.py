from users import Database
import asyncio


async def test():
    db = Database()
    await db.create_pool()
    await db.create_table_users()
    await db.update_user(123456, "beginner")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(test())
