from flask import Flask,request,current_app
import asyncio
from queries import create_pool
from sales_queries import salesOverCategory,salesOverTime

async def create_app():
    app = Flask(__name__)
    with app.app_context():
        current_app.pool= await create_pool()
    return app

app = asyncio.run(create_app())

@app.route('/salesovercategory', methods = [ 'GET'])
async def get_sales_category():
    
    st_date=request.args.get('st_date')
    end_date=request.args.get('end_date')
    category=request.args.get('category')
    limit=request.args.get('limit')
    name=request.args.get('name')

    return await salesOverCategory(st_date,end_date,category,limit,name)

@app.route('/salesovertime', methods = [ 'GET'])
async def get_sales_time():
    
    st_date=request.args.get('st_date')
    end_date=request.args.get('end_date')
    category=request.args.get('category')
    name=request.args.get('name')
    movieName=request.args.get('movie_name')

    return await salesOverTime(st_date,end_date,category,name,movieName)

  
if __name__=='__main__': 
   app.run()


