from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the models
gb_pipeline = joblib.load('models/gradient_boosting_model.pkl')
kmeans = joblib.load('models/kmeans_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Load risk mapping
import json
with open('models/risk_mapping.json', 'r') as f:
    risk_mapping = json.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract features
    age = data['age']
    sex = data['sex']
    bmi = data['bmi']
    children = data['children']
    smoker = data['smoker']
    region = data['region']
    
    # Calculate derived features
    smoker_bmi = bmi if smoker == 'yes' else 0
    smoker_age = age if smoker == 'yes' else 0
    
    # Create a DataFrame for the customer
    customer_df = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region],
        'smoker_bmi': [smoker_bmi],
        'smoker_age': [smoker_age]
    })
    
    # Predict cost
    predicted_cost = float(gb_pipeline.predict(customer_df)[0])
    
    # Create clustering features
    cluster_features = [[age, bmi, children, predicted_cost, smoker_bmi, smoker_age]]
    scaled_features = scaler.transform(cluster_features)
    
    # Predict cluster
    cluster = int(kmeans.predict(scaled_features)[0])
    risk_level = risk_mapping[str(cluster)]  # Json keys are strings
    
    return jsonify({
        'predictedCost': predicted_cost,
        'riskCluster': cluster,
        'riskLevel': risk_level
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)