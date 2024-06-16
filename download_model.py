import bentoml
import pickle


log_model = pickle.load(open('log_model.pkl','rb'))

print(log_model)

saved_model = bentoml.sklearn.save_model("log_model", log_model)