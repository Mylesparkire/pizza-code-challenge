import sys
import os

# Add the root folder to sys.path to import models from the root folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify
from models import db, RestaurantPizza  # adjust imports to your actual models

app = Flask(__name__)

# Config for your database URI (adjust if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), '../app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Pizza API!"

@app.route('/restaurant_pizzas')
def restaurant_pizzas():
    # Query all restaurant pizzas (adjust based on your actual model fields)
    pizzas = RestaurantPizza.query.all()

    # Serialize the data as a list of dicts
    pizzas_list = []
    for pizza in pizzas:
        pizzas_list.append({
            'id': pizza.id,
            'restaurant_id': pizza.restaurant_id,
            'pizza_id': pizza.pizza_id,
            # add other fields you have in your model
        })

    return jsonify(pizzas_list)

if __name__ == '__main__':
    app.run(debug=True)
