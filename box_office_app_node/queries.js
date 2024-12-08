

const db_info= {
    // user: 'postgres',
    user: 'edward',
    // host: 'db',
    host: 'localhost',
    database: 'postgres',
    password: 'mysecretpassword',
    port: '5432'
}

async function query(text, params,pool){
    return await pool.query(text, params);
}




module.exports = {query,db_info};