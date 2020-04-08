from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Restaurant, MenuItem

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def showHome():
    return render_template('index.html')

@app.route('/projects/')
def allProjects():
    return render_template('works.html')




@app.route('/restaurants/<int:restaurant_id>/delete/',
           methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    if request.method == 'POST':
        print "post request came"
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant)

@app.route('/restaurants/<int:restaurant_id>/edit/',
           methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        print "post request came"
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant = restaurant)

@app.route('/restaurants/new',
           methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def showRestaurantMenu(restaurant_id):
    return render_template('menu.html',restaurant =  restaurant,items =  items)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/',
           methods=['GET', 'POST'])
def deleteRestaurantMenu(restaurant_id,menu_id):
    if request.method == 'POST':
        return redirect(url_for('showRestaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item = item)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/',
           methods=['GET', 'POST'])
def editRestaurantMenu(restaurant_id,menu_id):
    if request.method == 'POST':
        return redirect(url_for('showRestaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('editMenuItem.html',item =  item)

@app.route('/restaurants/<int:restaurant_id>/menu/new/',
           methods=['GET', 'POST'])
def newRestaurantMenu(restaurant_id):
    if request.method == 'POST':
        return redirect(url_for('showRestaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant =  restaurant)









if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
