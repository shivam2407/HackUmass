from fatsecret import Fatsecret
from flask import Flask, render_template, request
from google.cloud import vision
from google.cloud.vision import types
import json
import requests
import random

app = Flask(__name__)
fs = Fatsecret("e0f89e5553d34ffd972e75f869bd551f","35db6d8a8b98446b817c1c7d54ef1351")

@app.route('/product',methods=["POST"])
def response():
    value = request.files['Upload']
    #encodedImage = base64.b64encode(value.read())
    encodedImage = value.read()
    result = get_vision(encodedImage)
    return render_template("Product.html", result = result)
    

def get_vision(content):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=content)
    response = client.web_detection(image=image).web_detection
    food_item = response.web_entities[0].description
    foods = fs.foods_search(food_item,1,10)
    options = {}
    for food in foods:
          options[food['food_id']] = food['food_name']
    return options

def get_food_details(food):
    units = food['serving_description']
    details = {}
    details['unit'] = units 
    if "calories" in food.keys():
      details['Calories'] = food['calories']
    if "iron" in food.keys():
      details['Iron'] = food['iron']
    if "sodium" in food.keys():
      details['Sodium'] = str(float(food['sodium'])/1000) 
    if "protein" in food.keys():
      details['Protein'] = food['protein']
    if "vitamin_c" in food.keys():
      details['Vitmain C'] = food['vitamin_c']
    if "saturated_fat" in food.keys():
      details['Saturated Fat'] = food['saturated_fat']
    if "carbohydrate" in food.keys():
      details['Carbohydrate'] = food['carbohydrate']
    if "fat" in food.keys():
      details['Fat'] = food['fat']
    if "fiber" in food.keys():
      details['Fiber'] = food['fiber']
    if "potassium" in food.keys():
      details['Potassium'] = food['potassium']
    if "sugar" in food.keys():
      details['Sugar'] = food['sugar']
    if "calcium" in food.keys():
      details['Calcium'] = food['calcium']
    if "vitamin_a" in food.keys():
      details['Vitamin A'] = food['vitamin_a']
    return details


@app.route('/properties',methods=["POST"])
def calorie():
    value = request.form['food_id']
    food = fs.food_get(value)['servings']['serving']
    if type(food) == list:
      food = food[0]
    #return json.dumps(food,ensure_ascii=False)
    result = get_food_details(food)
    return render_template("Properties.html", result = result) 

@app.route('/exercise',methods=["POST"])
def get_exercise():
    value = '';
    url = 'https://wger.de/api/v2/'
    page_number = random.randint(1,14)
    url = "https://wger.de/api/v2/exercise?language=2&page="+str(page_number)
    header = {'Accept': 'application/json','Authorization':''}
    r = requests.post(url=url, data={}, headers=header)
    r = json.loads(r.content.decode('UTF-8'))
    return str(r)
    url_image = "https://wger.de/api/v2/exerciseimage"
    r_image = requests.post(url=url_image, data={}, headers=header)
    bmr = ((10*85)+(6.25*173)+(5*21)+5)/2
    exer={}
    calorie={}
    r = r['results']
    for exercise in r:
         exer[exercise['name']] = exercise['description']
         calorie[exercise['name']] = random.randint(30,100)
    return render_template("excersie.html", result = exer)
    return str(exer)


@app.route('/<string:page_name>/')
def show_food(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
    app.run()
