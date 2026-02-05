from flask import Flask
from google import genai
from google.genai import types
from flask import render_template
from flask import request

client = genai.Client(api_key="AIzaSyDut6Tg-Ky-xhHPKRWu8GmkHahiPacIlxw")

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
    return "helloworld"
@app.route('/chat',methods=['GET','POST'])
def chat():
    user_message = request.json.get('message')
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Part.from_text(text= user_message),
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)
    return response.text

if __name__ =='__main__':
    app.run(debug=True)