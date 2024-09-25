# Toolhouse code generator project

This repo contains the frontend and backend code for my Toolhouse code generator project. In this project, you can send a "Generate FizzBuzz code. Execute it to show me the results up to 10" or "Give me a description of how FizzBuzz works and then show me some code"

## Steps to run the app

1. run `git clone https://github.com/JamieDawson/toolhouse-take-home.git` to clone the repo.
2. cd into the backend folder and run `pip install flask flask-cors python-dotenv toolhouse together` to install all the dependancies.
3. Create a `.env` file inside the backend folder and copy and paste the code below.

```
TOOLHOUSE_API_KEY= (paste Toolhouse API key here)
TOGETHER_API_KEY=  (paste Togehter API key here)
```

Make sure to add the appropriate API keys.

4. cd into the frontend folder
5. run `npm i axios` to install the axios package.
6. Inside the backend folder, run `py .\app.py` to run the backend server
7. Inside the frontend folder, run `npm run start` to run the frontend server
8. Test the app by pasting `Give me a description of how FizzBuzz works and then show me some code` into the text area and clicking the submit button. If everything is set up correctly, you should see a response below.

## The app being used:

https://github.com/user-attachments/assets/ee7eedc8-06ec-424d-a220-8f9932d66c7f
