const path = require("path");
const express = require('express');
const cors = require('cors');
const https = require('https');
require('dotenv').config();
fs = require('fs');
const {Pool} = require('pg');
const db = require('./queries');

const pool = new Pool(db.db_info);

const app = express();

app.pool=pool

app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET, PUT, POST');
    next();
});


app.use(cors({
    origin: true,
    credentials: true,
}));


app.use(express.urlencoded({extended: true}));
app.use(express.json());


const usersRouter = require('./users_routes')(app);

app.use('/', usersRouter);


const options = {
    key: fs.readFileSync('./certs/localhost-key.pem'),
    cert: fs.readFileSync('./certs/localhost.pem')
};

const server = https.createServer(options, app);

const PORT =  process.env.PORT || 4324;
server.listen(PORT, () => {console.log('Server is listening on port ' + PORT)})

