from flask import Flask
from flask_restful import Api, Resource , reqparse, abort
app=Flask(__name__)
api=Api(app)

product_post_args= reqparse.RequestParser()
# product_post_args.add_argument("Product code", type=int,help="Product code is required", required=True)
product_post_args.add_argument("Name", type=str,help="Product name is required", required=True)
product_post_args.add_argument("Price", type=int,help="Product price is required", required=True)
products ={}

def if_product_dont_exist(product_id):
	if product_id not in products:
		abort(404,message="product not found ")
class Product (Resource):
	def get(self,product_id):
		# return( {"data":"hi"})
		if_product_dont_exist(product_id)
		return products[product_id]
	def post(self,product_id):
		args=product_post_args.parse_args()
		products[product_id]=args
		# return{product_id:args}	
		return products[product_id], 201	


api.add_resource(Product,"/product/<int:product_id>")
@app.route("/")
def home_view():
	return "<h1>Hi</h1>"