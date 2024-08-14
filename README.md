# Big Mart Sales Prediction using Machine Learning

This repository contains a machine learning project aimed at predicting the sales of items at different outlets in the Big Mart dataset. The project is implemented using Python and Flask, allowing users to input item and outlet details through a web interface and receive sales predictions.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project is designed to predict the sales of items in different Big Mart outlets based on various factors like item type, MRP, outlet size, and more. The prediction model is built using machine learning algorithms, and the results are displayed on a web interface powered by Flask.

## Dataset
The dataset used in this project is a hypothetical dataset provided for academic purposes. It includes information about items and outlets, such as:
- Item Identifier
- Item Weight
- Item Fat Content
- Item Visibility
- Item Type
- Item MRP
- Outlet Identifier
- Outlet Establishment Year
- Outlet Size
- Outlet Location Type
- Outlet Type

## Model
The machine learning model used in this project is trained using regression techniques. The model is trained on the dataset to predict the sales of items based on the input features. The trained model is serialized using Pickle for deployment in the web application.

## Web Application
The web application is built using Flask. It provides a simple user interface where users can input the details of an item and an outlet, and the application will predict the sales for that item at the specified outlet.

### Features
- User-friendly interface to input data
- Real-time prediction of item sales
- Display of prediction results on the same page

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahinithi/Big-Mart-Sales-Prediction-using-Machine-Learning
   ```
2. Navigate to the project directory:
   ```bash
   cd Big-Mart-Sales-Prediction-using-Machine-Learning
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage
1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter the required details for the item and outlet in the form provided.
3. Click the "Predict" button to see the predicted sales for the item.

## File Structure
```
├── app.py                    # Flask application
├── big_mart_sales_model.pkl   # Trained machine learning model
├── index.html                # HTML template for the web interface
├── README.md                 # Project documentation
└── requirements.txt          # Python packages required
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


## Acknowledgments

This project was developed by **Nithilan**.
