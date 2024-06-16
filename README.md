# Password_Strength_Predictor(NLP)

## Overview
The NLP Password Strength Predictor is a machine learning project aimed at evaluating and predicting the strength of passwords using Natural Language Processing (NLP) techniques. The project leverages advanced NLP methods to analyze passwords and classify their strength into predefined categories such as weak, medium, and strong.

## Features

Data Preprocessing: Clean and preprocess password data, including handling missing values and normalizing text.
Feature Extraction: Utilize techniques like TF-IDF to transform password text data into meaningful features.
Model Training: Train machine learning models, including RandomForestClassifier, to predict password strength.
Evaluation: Assess model performance using metrics like accuracy, precision, recall, and F1-score, as well as confusion matrices.
Technologies Used
Python: Primary programming language used for development.
Pandas: Data manipulation and analysis.
NumPy: Numerical computing.
Scikit-learn: Machine learning library for model building and evaluation.
Matplotlib & Seaborn: Data visualization.

 Source: Custom-made in sql.

## How to run:
markdown
Copy code
# Password Strength Predictor API

This project is a Password Strength Predictor API built using BentoML and a pre-trained Logistic Regression model. The API takes a password as input and classifies its strength as either "weak", "medium strength", or "strong".

## Project Structure

- **service.py**: Contains the BentoML service definition and the classify function.
- **log_model.pkl**: Pickle file containing the pre-trained Logistic Regression model.
- **vectorizor.pkl**: Pickle file containing the pre-trained vectorizer (CountVectorizer).
- **requirements.txt**: Lists the dependencies required for the project.

## Setup and Installation

### Clone the Repository

git clone https://github.com/yourusername/Password_Strength_Predictor-NLP-.git
cd Password_Strength_Predictor-NLP-

Create and Activate a Virtual Environment


conda create --name password_strength_predictor python=3.12
conda activate password_strength_predictor
Install Dependencies
Ensure you have all the necessary dependencies installed. Create a requirements.txt file if you haven't already and add the required packages.

bentoml
numpy
scikit-learn

pip install -r requirements.txt
Download the Pre-trained Models
Ensure that log_model.pkl and vectorizor.pkl are placed in the root directory of your project.

Running the API

bentoml serve service.py:svc --reload --port 3001
Note: You can change the port if 3001 is already in use.

Make API Requests

curl -X POST "http://127.0.0.1:3001/classify" -H "Content-Type: application/json" -d '{"password": "your_password_here"}'

Using Postman
- Open Postman and create a new POST request.
- Set the URL to http://127.0.0.1:3001/classify.
- Go to the Headers tab and set Content-Type to application/json.
- Go to the Body tab, select raw and choose JSON from the dropdown.
- Enter the following JSON payload:


{
    "password": "your_password_here"
}

Click Send.
Using Python requests


import requests

url = "http://127.0.0.1:3001/classify"
payload = {
    "password": "your_password_here"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())


The API will return a JSON response indicating the strength of the password:

{
    "strength": "weak password"
}
or

{
    "strength": "medium strength password"
}
or


{
    "strength": "strong password"
}

## Troubleshooting
Port Issues: If the specified port is already in use, you can change the port by modifying the bentoml serve command with a different port number using the --port flag.
Model Loading Errors: Ensure that the log_model.pkl and vectorizor.pkl files are present in the root directory and are correctly saved.

## Conclusion
This Password Strength Predictor API allows you to evaluate the strength of passwords using a pre-trained machine learning model. By following the setup instructions and running the API, you can easily integrate this functionality into your applications. If you encounter any issues or have questions, please refer to the logs for detailed error messages and troubleshooting information.
