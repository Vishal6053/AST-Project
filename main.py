from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://vishal6503:vishal6503@cluster0.fqn525t.mongodb.net/?retryWrites=true&w=majority") 
db = client['test']
collection = db['test']

@app.route('/')
def display_jobs():
    jobs_data = collection.find()
    print(jobs_data)
    return render_template('index.html', jobs_data=jobs_data)

if __name__ == '__main__':
    app.run(debug=True)
