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
            "description": "Senior project for Seneca Park Zoo Society. This is a tool that allows individuals and organizations to track the positive ecological impact made through their donations to the zoo. It also provides field researchers with a tool to help them store and track ecological data that they collect in the wild.",
            "tools": "Node.js, Express.js, Salesforce, Heroku",
            "github": "https://github.com/my-conservation-life/my-conservation-life",
            "link": ""
        },
        {
            "name": "Chicago Website",
            "imagePath": "images/chicago-website.png",
            "description": "Final project for my Web & Mobile II class. A tourism website about Chicago, Illinois. Features a responsive design and surveys that store visitor responses in a back-end database.",
            "tools": "HTML, CSS, JavaScript, PHP",
            "github": "https://github.com/exw4141/iste240-project",
            "link": "https://iste240-project.herokuapp.com/"
        },
        {
            "name": "Personal Website",
            "imagePath": "images/personal-website.png",
            "description": "Personal project to create my own website and to learn the Flask microframework",
            "tools": "Flask, HTML, CSS",
            "github": "https://github.com/exw4141/personal-website",
            "link": ""
        },
        {
            "name": "AR Duck Hunt",
            "imagePath": "images/duck-hunt.png",
            "description": "Project for Trends in Software Development Processes that ported 2-D Duck Hunt assets into an augmented reality environment. The main purpose of this project was to gain experience with the Agile methodology and its entailing ceremonies (daily standups, sprint retrospectives, planning poker, etc.). However, I was able to gain experience with AR development and the Unity game engine.",
            "tools": "C#, Unity, Vuforia",
            "github": "",
            "link": ""
        },
        {
            "name": "Currency Converter",
            "imagePath": "images/currency-converter.png",
            "description": "A currency converter that can convert USD to many other currencies in the world. Features a simple GUI to select currencies for conversion and input amounts to convert from.",
            "tools": "Java, JavaFX",
            "github": "https://github.com/exw4141/currency-converter",
            "link": ""
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/resume')
def resume():
    return render_template('resume.html')
