# Import necessary modules
from flask import Flask, request, render_template
import pickle
import numpy as np

# Create a Flask application instance
app = Flask(__name__, template_folder='.')

# Load the trained model
with open("big_mart_sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html") # Render the index.html template

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the form
    item_identifier = int(request.form["item_identifier"])
    item_weight = float(request.form["item_weight"])
    item_fat_content = int(request.form["item_fat_content"])
    item_visibility = float(request.form["item_visibility"])
    item_type = int(request.form["item_type"])
    item_mrp = float(request.form["item_mrp"])
    outlet_identifier = int(request.form["outlet_identifier"])
    outlet_establishment_year = int(request.form["outlet_establishment_year"])
    outlet_size = int(request.form["outlet_size"])
    outlet_location_type = int(request.form["outlet_location_type"])
    outlet_type = int(request.form["outlet_type"])

    # Combine inputs into a single list
    input_data = np.asarray([[item_identifier, item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                              outlet_identifier, outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    # Make a prediction using the model
    prediction = model.predict(input_data)

    # Format the prediction
    prediction_text = f'Predicted Item Outlet Sales: ${prediction[0]:,.2f}'

    # Pass the prediction value to the template
    return render_template("index.html", prediction=prediction_text)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug mode for development
