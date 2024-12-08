const express = require('express');

module.exports= (app)=>{

    const router = express.Router();

    const gq = require('./sales_queries')(app);

    router.get('/salesovercategory', async (req, res, next) => {
        
        const info = req.query;
        const st_date = info.st_date
        const end_date = info.end_date
        const category= info.category
        const limit = info.limit
        const name = info.name
        const saleInfo = await gq.salesOverCategory(st_date,end_date,
                                                    category,limit,name);
        res.status(200).json(saleInfo);
    });

    router.get('/salesovertime', async (req, res, next) => {
        
        const info = req.query;
        const st_date = info.st_date
        const end_date = info.end_date
        const category= info.category
        const name = info.name
        const movieName=info.movie_name
        const saleInfo = await gq.salesOverTime(st_date,end_date,category,
                                                name,movieName);
        res.status(200).json(saleInfo);
    });

    return router;
}




