import queries
import asyncio

def makeString(str_expr):
    if str_expr:
        return f"'{str_expr}'"
    return "NULL"


async def insertMovies(titles,st_dates,end_dates,cur):
    value_string= ''
    
    for i in range(len(titles)):
        value_string += "".join([f"({makeString(titles[i])},{makeString(st_dates[i])},",
        f"{makeString(end_dates[i])}), "])

    value_string= value_string[0:-2] + ';'
    text = 'insert into movies (title,release_date, end_date) '+ 'values ' + value_string
    await cur.execute(text, [])

async def insertTheaters(names,cities,cur):
    value_string= ''
    
    for i in range(len(names)): 
        value_string += f'({makeString(names[i])},{makeString(cities[i])}), '
    value_string=value_string[0:-2] + ';'
    text = 'insert into theaters (name,city) ' + 'values ' + value_string
    await cur.execute(text, [])

async def insertSales(movie_names,theater_names,sales_dates,sale_amounts,cur):

    value_string= ''
    
    for i in range(len(movie_names)):
        value_string += "".join([f'({makeString(movie_names[i])},', 
        f'{makeString(theater_names[i])},{makeString(sales_dates[i])},',
        f'{sale_amounts[i]}), '])
    value_string=value_string[0:-2] + '; '
    text = "".join(['drop table if exists sales_temp; ',
    'CREATE temp TABLE sales_temp (movie_title varchar(128), ',
    'theater_name varchar(128), ',
    'sale_date date,total_sales numeric default 0); ', 
    'insert into sales_temp (movie_title,theater_name, sale_date,total_sales) ',
    'values ' + value_string,
    'insert into sales(movie_id,theater_id,sale_date,total_sales) ', 
    'select movies.id,theaters.id, ',
    'sale_date,total_sales from sales_temp inner join movies on ',
    'movies.title=sales_temp.movie_title inner join theaters on ',
    'theaters.name=sales_temp.theater_name; ',
    'drop table if exists sales_temp;']) 
    await cur.execute(text, [])

titles = ['Moana 2','Wicked','Red One']
st_dates=['2024-11-27','2024-11-22','2024-11-15']
end_dates=[None,None,None]
names = ['AMC Saratoga 14','Regal LA Live','THE LOT Libert Station']
cities=['San Jose','Los Angeles','San Diego']
sales_dates=['11-28-2024','11-28-2024','11-28-2024',
'11-28-2024','11-28-2024','11-28-2024','11-28-2024','11-28-2024','11-28-2024',
'11-29-2024','11-29-2024','11-29-2024','11-29-2024','11-29-2024','11-29-2024',
'11-29-2024','11-29-2024','11-29-2024','11-30-2024','11-30-2024','11-30-2024',
'11-30-2024','11-30-2024','11-30-2024','11-30-2024','11-30-2024','11-30-2024']
theater_names=['AMC Saratoga 14','AMC Saratoga 14','AMC Saratoga 14',
'Regal LA Live','Regal LA Live','Regal LA Live',
'THE LOT Libert Station','THE LOT Libert Station','THE LOT Libert Station',
'AMC Saratoga 14','AMC Saratoga 14','AMC Saratoga 14',
'Regal LA Live','Regal LA Live','Regal LA Live',
'THE LOT Libert Station','THE LOT Libert Station','THE LOT Libert Station',
'AMC Saratoga 14','AMC Saratoga 14','AMC Saratoga 14',
'Regal LA Live','Regal LA Live','Regal LA Live',
'THE LOT Libert Station','THE LOT Libert Station','THE LOT Libert Station']
movie_names=['Moana 2','Wicked','Red One','Moana 2','Wicked','Red One',
'Moana 2','Wicked','Red One','Moana 2','Wicked','Red One',
'Moana 2','Wicked','Red One','Moana 2','Wicked','Red One',
'Moana 2','Wicked','Red One','Moana 2','Wicked','Red One',
'Moana 2','Wicked','Red One']
sale_amounts=[7600,5300,2000,6600,4300,1000,5600,3300,100,
14000,9200,2400,13000,8200,1400,12000,7200,400,
13000,8500,2420,12000,7500,1420,11000,6500,420]


async def insertData():
    async with queries.AsyncConnectionPool(queries.connection_str, open=False) as pool:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await insertMovies(titles,st_dates,end_dates,cur)
                await insertTheaters(names,cities,cur)
                await insertSales(movie_names,theater_names,sales_dates,
                sale_amounts,cur)


try:
    asyncio.run(insertData())
except Exception as e: 
    print(e)
