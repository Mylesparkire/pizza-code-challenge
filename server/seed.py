from server.app import create_app, db

from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_database():
    app = create_app()
    with app.app_context():
        # Clear existing data
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()

        # Create restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Slice of Heaven", address="456 Oak Ave"),
            Restaurant(name="Pizza Paradise", address="789 Pine Rd"),
            Restaurant(name="Pizza Planet", address="101 Pine Rd"),
            Restaurant(name="Pizza Place", address="105 New York Rd"),
        ]
        db.session.add_all(restaurants)

        # Create pizzas
        pizzas = [
            Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni"),
            Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Mushrooms, Onions"),
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Mozzarella, Cheese"),
           
        ]
        db.session.add_all(pizzas)

        # Commit to get IDs
        db.session.commit()

        # Create restaurant pizzas
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=11, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=13, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=12, restaurant_id=3, pizza_id=2),
            RestaurantPizza(price=14, restaurant_id=3, pizza_id=3)
        ]
        db.session.add_all(restaurant_pizzas)

        # Final commit
        db.session.commit()

if __name__ == '__main__':
    seed_database()
    print("Database seeded successfully!") 