
from queries import query
from flask import current_app

def format_result(row,return_columns):
    row_obj={}
    for column,value in zip(return_columns,row):
        row_obj[column]=value
    return row_obj

async def salesOverCategory(st_date,end_date,category,limit,name):

    if category=='theater':

        if name:

            text = "".join(['select name,city,total from (select theater_id,total from ', 
            '(select theater_id,sum(total_sales) as total from ',
            '(sales inner join (select id from movies where title=%s) as mov_id_tab ',
            'on sales.movie_id=mov_id_tab.id) as sales_movie where ',
            'sale_date >=%s and sale_date<=%s ',
            'group by theater_id) as day_sales order by total desc limit %s) ',
            'as max_day_sales ',
            'inner join theaters on theaters.id=max_day_sales.theater_id;'])

            return_columns=['name','city','total']
            params = (name,st_date,end_date,limit)
        
        else:
            text = "".join(['select name,city,total from (select theater_id,total from ', 
            '(select theater_id,sum(total_sales) as total from sales where ', 
            'sale_date >=%s and sale_date<=%s ',
            'group by theater_id) as day_sales order by total desc limit %s) ',
            'as max_day_sales ',
            'inner join theaters on theaters.id=max_day_sales.theater_id;'])

            return_columns=['name','city','total']
            params = (st_date,end_date,limit)
        
    else:

        if name:

            text = "".join(["select title,to_char(release_date,'mm-dd-yyyy') as ", 
            '"releaseDate",',
            'total from (select movie_id,total from ', 
            '(select movie_id,sum(total_sales) as total from ',
            '(sales inner join (select id from theaters where name=%s) as ', 
            'theater_id_tab on sales.theater_id=theater_id_tab.id) ',
            'as sales_theater where ',
            'sale_date >=%s and sale_date<=%s ',  
            'group by movie_id) as day_sales order by total desc limit %s) ',
            'as max_day_sales ',
            'inner join movies on movies.id=max_day_sales.movie_id;'])
            return_columns=['title','releaseDate','total']
            params = (st_date,end_date,limit,name)

        

        else:
            text = "".join(["select title,to_char(release_date,'mm-dd-yyyy') as ",
            '"releaseDate",',
            'total from (select movie_id,total from ', 
            '(select movie_id,sum(total_sales) as total from sales where ',
            'sale_date >=%s and sale_date<=%s ',
            'group by movie_id) as day_sales order by total desc limit %s) ', 
            'as max_day_sales ', 
            'inner join movies on movies.id=max_day_sales.movie_id;'])
            return_columns=['title','releaseDate','total']
            params = (st_date,end_date,limit)

    res = await query(text, params,current_app.pool)
    res = list(map(lambda row:format_result(row,return_columns),res))
    return res


async def salesOverTime(st_date,end_date,category,name,movie_name):
    
    if category=='theater':

        text = "".join(["select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from ", 
        'sales inner join (select id from theaters where name=%s) as theater_id_tab ', 
        'on sales.theater_id=theater_id_tab.id where sale_date>=%s and ', 
        'sale_date<=%s group by sale_date order by sale_date;'])
        return_columns=['date','total']
        params = (name,st_date,end_date)
    
    elif category=='movie':

        text = "".join(["select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from ", 
        'sales inner join (select id from movies where title=%s) as movie_id_tab ', 
        'on sales.movie_id=movie_id_tab.id where sale_date>=%s and ', 
        'sale_date<=%s group by sale_date order by sale_date;'])
        return_columns=['date','total']
        params = (name,st_date,end_date)
    

    elif category=='both':
        text = "".join(["select to_char(sale_date,'mm-dd-yyyy') as date,total_sales as total from ", 
        'sales inner join (select id from theaters where name=%s) as theater_id_tab ',
        'on sales.theater_id=theater_id_tab.id ',
        'inner join (select id from movies where title=%s) as movie_id_tab ', 
        'on sales.movie_id=movie_id_tab.id ',
        'where sale_date>=%s and ',
        'sale_date<=%s order by sale_date;'])
        return_columns=['date','total']
        params=(name,movie_name,st_date,end_date)

    else:
        text = "".join(["select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from ",
        'sales where sale_date>=%s and sale_date<=%s group by sale_date order by sale_date;'])
        return_columns=['date','total']
        params = (st_date,end_date)
     
    res = await query(text, params,current_app.pool)
    res = list(map(lambda row:format_result(row,return_columns),res))
    return res

























