
import bentoml
from bentoml.io import JSON
import numpy as np
import logging
import pickle


# Load your vectorizer and model
vectorizor = pickle.load(open('vectorizor.pkl', 'rb'))


# Define the BentoML service
log_model_runner = bentoml.sklearn.get("log_model:xlgdggrmasw2pqsw").to_runner()
svc = bentoml.Service("password_strength_classifier", runners=[log_model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(input_data: dict) -> dict:
    try:
        password = input_data['password']
        sample = np.array([password])
        
        # Transform the input password into a vector
        sample_matrix = vectorizor.transform(sample)
        
        # Calculate length features
        length = len(password)
        length_normpass = len([char for char in password if char.islower() or char.isupper()]) / len(password)
        
        # Append length features to the vectorized input
        new_matrix = np.append(sample_matrix.toarray(), [length_normpass, length]).reshape(1, -1)
        
        # Predict password strength using the runner
        result = log_model_runner.predict.run(new_matrix)
        
        # Return the strength of the password based on the prediction
        if result[0] == 0:
            return {'strength': 'weak password'}
        elif result[0] == 1:
            return {'strength': 'medium strength password'}
        else:
            return {'strength': 'strong password'}
    except Exception as e:
        logging.error(f"Error in classify function: {e}")
        return {'error': str(e)}
