from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlflowProject.pipeline.prediction import PredictionPipiline


app = Flask(__name__)

@app.route('/',methods =['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return 'Training Sucessfull..!!'


# @app.route('/predict', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         try:
#             # Retrieve inputs
#             data = {
#                 'Weight': float(request.form['Weight']),
#                 'FatContent': request.form['FatContent'],
#                 'ProductVisibility': float(request.form['ProductVisibility']),
#                 'ProductType': request.form['ProductType'],
#                 'MRP': float(request.form['MRP']),
#                 'EstablishmentYear': int(request.form['EstablishmentYear']),
#                 'OutletSize': request.form['OutletSize'],
#                 'LocationType': request.form['LocationType'],
#                 'OutletType': request.form['OutletType'],
#             }
#             # Convert to DataFrame
#             data_df = pd.DataFrame([data])
#             data_df = pd.get_dummies(data_df)
#             print(data_df)

#             # Predict
#             obj = PredictionPipiline()
#             prediction = obj.predict(data_df)

#             return render_template('results.html', prediction=str(prediction))
#         except Exception as e:
#             print("This Exception message is:", e)
#             return f"Error: {e}"
#     else:
#         return render_template('index.html')
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=8080,debug=True)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()

        # Map input data to match trained model's feature names
        input_data = {
            'Weight': float(form_data['Weight']),
            'FatContent': form_data['FatContent'],  # Store the value directly for later encoding
            'ProductVisibility': float(form_data['ProductVisibility']),
            'ProductType': form_data['ProductType'],
            'ProductID': form_data['ProductID'],
            'OutletID': int(form_data['OutletID']),
            'MRP': float(form_data['MRP']),
            'EstablishmentYear': int(form_data['EstablishmentYear']),
            'OutletSize': form_data['OutletSize'],  # Store the value directly for later encoding
            'LocationType': form_data['LocationType'],  # Store the value directly for later encoding
            'OutletType': form_data['OutletType'],  # Store the value directly for later encoding
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        trained_columns = [
    "Weight", "ProductVisibility", "MRP", "OutletID", "EstablishmentYear", "ProductID_DR", 
    "ProductID_FD", "ProductID_NC", "FatContent_lf", "FatContent_reg", "ProductType_Baking Goods", 
    "ProductType_Breads", "ProductType_Breakfast", "ProductType_Canned", "ProductType_Dairy", 
    "ProductType_Frozen Foods", "ProductType_Fruits and Vegetables", "ProductType_Hard Drinks", 
    "ProductType_Health and Hygiene", "ProductType_Household", "ProductType_Meat", "ProductType_Others", 
    "ProductType_Seafood", "ProductType_Snack Foods", "ProductType_Soft Drinks", "ProductType_Starchy Foods", 
    "OutletSize_High", "OutletSize_Medium", "OutletSize_Small", "LocationType_Tier 1", "LocationType_Tier 2", 
    "LocationType_Tier 3", "OutletType_Grocery Store", "OutletType_Supermarket Type1", 
    "OutletType_Supermarket Type2", "OutletType_Supermarket Type3"
]

        # # Reindex the input data to match the training columns
        input_df = input_df.reindex(columns=trained_columns, fill_value=0)
        input_df = pd.get_dummies(input_df)
        print("----------------",input_df)

        # Predict
        obj = PredictionPipiline()
        prediction = obj.predict(input_df)
        prediction = prediction*100
        # print(type(prediction))
        # Render the result
        return render_template('results.html', prediction=str(prediction))

    except Exception as e:
        print("This Exception message is:", e)
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)