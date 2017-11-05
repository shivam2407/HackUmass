Dependencies: 
1.  pyfatsecret0.2.3
2. Flask0.12.2
3. Google.Cloud
4. Google.Cloud.vision
5. Json
6. Random

API used:
1. Google Vision API
2. Fatsecret API
3. Workout Manager API
And last but not the least Python3.X(X>0)

Flow of Program:

1. First we ask user to upload the photo of their food on the website.
Code Executed: Here when the website opens the function show_food(page_name) is executed where it fetches the page name from url which needs to be rendered. In this case it is index.html file in templates folder.  

2. Second when user uploads the photo we fetch the photo and then send the photo to Google vision API and fetch the name of dish.
Code Executed: Here the function response is called which reads the image’s byte array and with this value it calls get_vision(content) function. This functions uses the Google vision api to fetch the name of the dish.

3. After fetching the name of the dishes we fetch the various variant of that dishes and show them to user so that they can select which variant of that dish they are eating. We are using pyfatsecret for fetching this data.
Code Executed: Here the function calorie() is executed which gets all the information for the dish you are eating like calories per serving, fats(saturated fats, unsaturated fats), protein, and many more. After fetching this information it renders the web page named Properties.html with the information it just received.

4. Now we are calculating the B.M.R (Basal Metabolic Rate) of the user based on his/her age, weight and height. For this POC this information is hard coded and not been asked by user. Once B.M.R is calculated we deduct that calorie from the calorie consumed by user. After this if user wants he/she can see the list of excersie he/she can do for burning those calories. We give name of the exercise, description of how to do that exercise and for how long one exercise should be done to lose the extra calories.
Code Executed: Here the function get_exercise() is executed. It fetches all different exercise a person can do to lose calories. Once we have the information we render the exercise.html with the information we just received.
