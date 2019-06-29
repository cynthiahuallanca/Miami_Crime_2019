#from machineLearning import two_plots, stationarity_test, chart_by_weekday
from flask import Flask, jsonify, render_template, redirect

# Create an instance of Flask

app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    
      
    return render_template("index.html")


@app.route("/crime_rate")
def crime_rate():

       
    return render_template("crime_rate.html")


@app.route("/crime_rate_by_city")
def crime_rate_by_city():

       
    return render_template("crime_rate_by_city.html")


@app.route("/crime_type_by_city")
def crime_type_by_city():

       
    return render_template("crime_type_by_city.html")


@app.route("/homeless")
def homeless():

       
    return render_template("homeless.html")


@app.route("/machinelng")
def machinelng():
    
    return render_template("machinelng.html")

@app.route("/conclusion")
def conclusion():

       
    return render_template("conclusion.html")

@app.route("/about")
def about():
    
    return render_template("about.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
#    app.run()
    