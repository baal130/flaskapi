from app import app,db
from .models import ProductDB
import json,os
from flask_restful import Api, Resource , reqparse, abort, fields, marshal_with
api=Api(app)





product_post_args= reqparse.RequestParser()
# product_post_args.add_argument("Product code", type=int,help="Product code is required", required=True)
product_post_args.add_argument("name", type=str,help="Product name is required", required=True)
product_post_args.add_argument("price", type=str ,help="Product price is required", required=True)

product_put_args= reqparse.RequestParser()
# product_post_args.add_argument("Product code", type=int,help="Product code is required", required=True)
product_put_args.add_argument("name", type=str,help="Product name ", )
product_put_args.add_argument("price", type=str ,help="Product price ", )


resource_field={
	
	'name' :fields.String,
	'price':fields.String,
	'id'   :fields.Integer,

}

class Product (Resource):
	@marshal_with(resource_field)
	def get(self,product_id):
		# return( {"data":"hi"})
		product=ProductDB.query.filter_by(id=product_id).first()
		if not product:
			abort(404,message="product don't exist use post to create")
		return product



	@marshal_with(resource_field)
	def put (self,product_id):
		args=product_put_args.parse_args()
		product=ProductDB.query.filter_by(id=product_id).first()

		if not product:
			abort(404,message="product don't exist use post to create")

		if "name" in args and args['name'] is not None :
			product.name=args['name']
			print(args)
			print(product)
		if "price" in args and args['price'] is not None:
			product.price=args['price']
		db.session.commit()		
		return product
	@marshal_with(resource_field)	
	def delete (self,product_id):
		product=ProductDB.query.filter_by(id=product_id).first()
		if not product:
			abort(404,message="product don't exist use post to create")
		
		db.session.delete(product)
		db.session.commit()
		return product
class ProductCreate (Resource):
	@marshal_with(resource_field)
	def post(self):
		product=ProductDB.query.all()
	
		if product:
			id= ProductDB.query.count()+1
		else:
			id=1
		args=product_post_args.parse_args()
		
		args["id"]=id
		print(args)
		#products[product_id]=args
		obj=ProductDB(name=args['name'],price=args['price'] , id=args['id'])
		db.session.add(obj)
		db.session.commit()
		# return{product_id:args}	
		return product, 200
api.add_resource(ProductCreate,"/v1/product") 
api.add_resource(Product,"/v1/product/<int:product_id>") #routing for one or more HTTP methods for a given URL

@marshal_with(resource_field)
def serialize_product(self):
	return self
@app.route("/v1/products")

def get_products():
	products=ProductDB.query.all()
	l=[]
	for product in products:
		l.append(serialize_product(product))
	print(l)
	dump=json.dumps(l) #list to json
	print(dump)
	return dump
	
	#expected json array [{},{}] type str