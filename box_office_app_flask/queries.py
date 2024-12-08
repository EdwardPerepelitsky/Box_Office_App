from psycopg_pool import AsyncConnectionPool
import asyncio

connection_str = ''.join(['user=edward host=localhost dbname=postgres ',
'password=mysecretpassword port=5432'])


async def create_pool():
    pool = AsyncConnectionPool(connection_str,open=False)
    await pool.open(wait=True)
    return  pool
    
async def query(text,params,pool):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(text, params)
            return await cur.fetchall()



