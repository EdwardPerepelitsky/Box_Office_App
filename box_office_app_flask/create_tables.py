import queries
import asyncio

async def createMovies (cur):
    text = "".join(['CREATE TABLE movies (id serial primary key, title varchar(128) unique, ',
                 'release_date date not null, end_date date default null)'])
    await cur.execute(text, [])


async def createTheaters(cur):
    text = "".join(['CREATE TABLE theaters (id serial primary key, name varchar(128) unique, ',
                 'city varchar(128))'])
    await cur.execute(text, [])

async def createSales(cur):
    text = "".join(['CREATE TABLE sales (id serial primary key,', 
                 'movie_id int REFERENCES movies(id) on delete cascade, ',
                 'theater_id int REFERENCES theaters(id) on delete cascade, ',
                 'sale_date date not null, ',
                 'total_sales numeric default 0); ',
                 'Create index idx_sales_moid_sadate_totsa on ', 
                 'sales(movie_id,sale_date,total_sales); ', 
                 'Create index idx_sales_thid_sadate_totsa on ', 
                 'sales(theater_id,sale_date,total_sales); ',
                 'Create unique index idx_sales_moid_thid_sadate on ',
                 'sales(movie_id,theater_id,sale_date); ',
                 'Create index idx_sales_sadate on sales(sale_date);'])
                 
    await cur.execute(text, [])


async def createTables():
    async with queries.AsyncConnectionPool(queries.connection_str, open=False) as pool:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await createMovies(cur)
                await createTheaters(cur)
                await createSales(cur)


try:
    asyncio.run(createTables())
except Exception as e: 
    print(e)