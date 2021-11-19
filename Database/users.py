import asyncpg
from asyncpg.pool import Pool
from typing import Union
from load_env import db_name, db_host, db_user, db_password


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        result = None
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """CREATE TABLE IF NOT EXISTS Users(
        id BIGSERIAL PRIMARY KEY,
        user_id BIGINT NOT NULL UNIQUE,
        username VARCHAR (255),
        first_name VARCHAR (255),
        last_name VARCHAR (255),
        level VARCHAR (20)
        );"""
        await self.execute(sql, execute=True)

    async def add_user(self, user_id, username, first_name, last_name):
        sql = """INSERT INTO Users (user_id, username, first_name, last_name) VALUES($1, $2, $3, $4) returning *"""
        return await self.execute(sql, user_id, username, first_name, last_name, execute=True)

    async def update_user(self, user_id, level):
        sql = """UPDATE Users SET level=$2 WHERE user_id=$1;"""
        await self.execute(sql, user_id, level, execute=True)

    async def select_user(self, user_id):
        sql = f"""SELECT * FROM Users WHERE user_id={user_id}"""
        return await self.execute(sql, fetchrow=True)

    async def select_users(self):
        sql = """SELECT * FROM users"""
        return await self.execute(sql, fetchrow=True)

    async def drop_user(self, user_id):
        sql = f"""DELETE FROM Users WHERE user_id={user_id}"""
        return await self.execute(sql, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)
