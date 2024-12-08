const db = require('./queries');

module.exports= (app)=> {
    const pool = app.pool

    async function salesOverCategory(st_date,end_date,category,limit,name){
        let text
        let params
        
        if (category==='theater'){

            if (name){

                text = 'select name,city,total from (select theater_id,total from ' + 
                '(select theater_id,sum(total_sales) as total from '+
                '(sales inner join (select id from movies where title=$4) as mov_id_tab '+
                'on sales.movie_id=mov_id_tab.id) as sales_movie where ' + 
                'sale_date >=$1 and sale_date<=$2 ' +  
                'group by theater_id) as day_sales order by total desc limit $3) '+
                'as max_day_sales ' + 
                'inner join theaters on theaters.id=max_day_sales.theater_id;';
                    
                params = [st_date,end_date,limit,name];
            }
            
            else{
                text = 'select name,city,total from (select theater_id,total from ' + 
                '(select theater_id,sum(total_sales) as total from sales where ' + 
                'sale_date >=$1 and sale_date<=$2 ' +  
                'group by theater_id) as day_sales order by total desc limit $3) '+
                'as max_day_sales ' + 
                'inner join theaters on theaters.id=max_day_sales.theater_id;';
                params = [st_date,end_date,limit];
            }

        }
        else{

            if (name){

                text = `select title,to_char(release_date,'mm-dd-yyyy') as ` + 
                `"releaseDate",` + 
                'total from (select movie_id,total from ' + 
                '(select movie_id,sum(total_sales) as total from ' + 
                '(sales inner join (select id from theaters where name=$4) as ' + 
                'theater_id_tab on sales.theater_id=theater_id_tab.id) ' + 
                'as sales_theater where ' + 
                'sale_date >=$1 and sale_date<=$2 ' +  
                'group by movie_id) as day_sales order by total desc limit $3) ' + 
                'as max_day_sales ' + 
                'inner join movies on movies.id=max_day_sales.movie_id;';
                params = [st_date,end_date,limit,name];

            }

            else{
                text = `select title,to_char(release_date,'mm-dd-yyyy') as ` + 
                `"releaseDate",` + 
                'total from (select movie_id,total from ' + 
                '(select movie_id,sum(total_sales) as total from sales where ' + 
                'sale_date >=$1 and sale_date<=$2 ' +  
                'group by movie_id) as day_sales order by total desc limit $3) ' + 
                'as max_day_sales ' + 
                'inner join movies on movies.id=max_day_sales.movie_id;';
                params = [st_date,end_date,limit];
            }

        }
        
        const res = await db.query(text, params,pool);
        return res.rows;
    };

    async function salesOverTime(st_date,end_date,category,name,movie_name){
        let text
        let params
        if (category==='theater'){

            text = "select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from " + 
            'sales inner join (select id from theaters where name=$3) as theater_id_tab ' + 
            'on sales.theater_id=theater_id_tab.id where sale_date>=$1 and ' + 
            'sale_date<=$2 group by sale_date order by sale_date;'
            params = [st_date,end_date,name];
        }
        else if (category==='movie'){

            text = "select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from " + 
            'sales inner join (select id from movies where title=$3) as movie_id_tab ' + 
            'on sales.movie_id=movie_id_tab.id where sale_date>=$1 and ' + 
            'sale_date<=$2 group by sale_date order by sale_date;'
            params = [st_date,end_date,name];
        }

        else if (category==='both'){
            text = "select to_char(sale_date,'mm-dd-yyyy') as date,total_sales as total from " + 
            'sales inner join (select id from theaters where name=$3) as theater_id_tab ' + 
            'on sales.theater_id=theater_id_tab.id ' + 
            'inner join (select id from movies where title=$4) as movie_id_tab ' + 
            'on sales.movie_id=movie_id_tab.id ' + 
            'where sale_date>=$1 and ' + 
            'sale_date<=$2 order by sale_date;'
            params=[st_date,end_date,name,movie_name]
        }

        else {
            text = "select to_char(sale_date,'mm-dd-yyyy') as date,sum(total_sales) as total from " +
            'sales where sale_date>=$1 and sale_date<=$2 group by sale_date order by sale_date;'
            params = [st_date,end_date];
        }
        
        const res = await db.query(text, params,pool);
        return res.rows;
    };

    return {salesOverCategory,salesOverTime}
}

    























