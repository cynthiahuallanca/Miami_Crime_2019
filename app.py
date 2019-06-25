from machineLearning import two_plots, stationarity_test, chart_by_weekday
from flask import Flask, jsonify, render_template, redirect

# Create an instance of Flask

app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    
#    two_plots()
    stationarity = open("Resources/stationarity.txt", "r")    
    results = stationarity.read()
    i=0
    results_list = {}
    results_array =[]
    results_array = results.split('\n')
    for element in results_array: 
        print('element', element)
        results_list.update({element:str(i)})
        i += 1                     
        
    res = {element for element in results_array} 
#    print('res', results_list)
    
    stationarity.close()
    
    return render_template("index.html",  results=results_list)


@app.route("/comp_profiles")
def comp_profiles():

       
    # Return template and data
    return render_template("comp_profiles.html")




if __name__ == "__main__":
#    app.run(host='0.0.0.0',port=5000)
    app.run()
    