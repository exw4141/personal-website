from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def project():
    projects = [
        {
            "name": "Seneca Park Zoo Conservation Impact Project",
            "imagePath": "images/mcl.png",
            "description": "Senior project for Seneca Park Zoo Society",
            "tools": "Node.js, Salesforce, Heroku, JavaScript",
            "github": "https://github.com/my-conservation-life/my-conservation-life",
            "link": ""
        },
        {
            "name": "Chicago Website",
            "imagePath": "images/chicago-website.png",
            "description": "Final project for my Web & Mobile II class.",
            "tools": "HTML, CSS, JavaScript, PHP",
            "github": "https://github.com/exw4141/iste240-project",
            "link": "https://iste240-project.herokuapp.com/"
        },
        {
            "name": "Personal Website",
            "imagePath": "images/personal-website.png",
            "description": "Personal project to create my own website and to learn the Flask microframework",
            "tools": "Flask, Python, HTML, CSS",
            "github": "https://github.com/exw4141/personal-website",
            "link": ""
        },
        {
            "name": "AR Duck Hunt",
            "imagePath": "images/duck-hunt.png",
            "description": "Project for Trends in Software Development Processes.",
            "tools": "C#, Unity, Vuforia",
            "github": "",
            "link": ""
        },
        {
            "name": "Currency Converter",
            "imagePath": "images/currency-converter.png",
            "description": "Simple currency converter that can convert USD to many other currencies in the world",
            "tools": "Java",
            "github": "https://github.com/exw4141/currency-converter",
            "link": ""
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')
