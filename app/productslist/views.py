from app import app

import json,os
from flask_restful import Api, Resource , reqparse, abort
api=Api(app)

product_post_args= reqparse.RequestParser()
# product_post_args.add_argument("Product code", type=int,help="Product code is required", required=True)
product_post_args.add_argument("name", type=str,help="Product name is required", required=True)
product_post_args.add_argument("price", type=str ,help="Product price is required", required=True)

product_put_args= reqparse.RequestParser()
# product_post_args.add_argument("Product code", type=int,help="Product code is required", required=True)
product_put_args.add_argument("name", type=str,help="Product name ", )
product_put_args.add_argument("price", type=str ,help="Product price ", )

products =[ 
			 {"name":"Lavender heart", "price":"9.25" , "id":1},
			 {"name":"Personalised cufflinks", "price":"45.00", "id":2},
			 {"name":"Kids T-shirt", "price":"19.95", "id":3},		
		  ]

def if_product_dont_exist(product_id):
	# if product_id not in products:
	product=[p for p in products if p["id"] == product_id]
	if not product:	
		abort(404,message="product not found ")
def if_product_already_exist(product_id):
	for product in products:
		if product["id"]==product_id:
			abort(404,message="product exist use put to update")

class Product (Resource):
	def get(self,product_id):
		# return( {"data":"hi"})
		

		if_product_dont_exist(product_id)
		#return products[product_id]#{1: {'name': 'First', 'price': 10.0}}
		product = next((product for product in products if product['id'] == product_id), None)
		return product
		
	def post(self,product_id):
		args=product_post_args.parse_args()
		if_product_already_exist(product_id)
		args["id"]=product_id
		print(args)
		
		products.append(args)
		# return{product_id:args}	
		return products, 200	
	def put (self,product_id):
		args=product_put_args.parse_args()
		if_product_dont_exist(product_id)
		for product in products:
				if product["id"]==product_id:
					# product.update(args)
					if "name" in args and args['name'] is not None :
						product['name']=args['name']
						print(args)
						print(product)
					if "price" in args and args['price'] is not None:
						product['price']=args['price']
				
		return products	
	def delete (self,product_id):
		if_product_dont_exist(product_id)
		for i,product in enumerate(products):
				if product["id"]==product_id:
					del products[i]
		return products
class ProductCreate (Resource):
	def post(self):
		if products:
			id=len(products)+1
		else:
			id=1
		args=product_post_args.parse_args()
		
		args["id"]=id
		print(args)
		#products[product_id]=args
		products.append(args)
		# return{product_id:args}	
		return products, 200
api.add_resource(ProductCreate,"/v1/product") 
api.add_resource(Product,"/v1/product/<int:product_id>") #routing for one or more HTTP methods for a given URL


@app.route("/v1/products")
def get_products():
	


	dump=json.dumps(products) #list to json
	return dump
	#expected json array [{},{}] type str