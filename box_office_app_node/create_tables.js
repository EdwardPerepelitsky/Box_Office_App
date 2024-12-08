const db = require('./queries.js');
const {Pool} = require('pg');
const pool = new Pool(db.db_info);

async function createMovies(){
    const text = 'CREATE TABLE movies (id serial primary key, title varchar(128) unique, '+
                 'release_date date not null, end_date date default null)';
    await db.query(text, [],pool);
} 

async function createTheaters(){
    const text = 'CREATE TABLE theaters (id serial primary key, name varchar(128) unique, '+
                 'city varchar(128))';
    await db.query(text, [],pool);
} 

async function createSales(){
    const text = 'CREATE TABLE sales (id serial primary key,' + 
                 'movie_id int REFERENCES movies(id) on delete cascade, ' +
                 'theater_id int REFERENCES theaters(id) on delete cascade, ' +
                 'sale_date date not null, ' + 
                 'total_sales numeric default 0); ' +
                 'Create index idx_sales_moid_sadate_totsa on ' + 
                 'sales(movie_id,sale_date,total_sales); ' + 
                 'Create index idx_sales_thid_sadate_totsa on ' + 
                 'sales(theater_id,sale_date,total_sales); ' +
                 'Create unique index idx_sales_moid_thid_sadate on ' + 
                 'sales(movie_id,theater_id,sale_date); ' + 
                 'Create index idx_sales_sadate on sales(sale_date);'
                 
    await db.query(text, [],pool);
}


async function createTables(){
    await createMovies();
    await createTheaters();
    await createSales();
}

createTables().catch(error => {console.log(error);});