from joblib import load
import numpy as np

class Model:
    def __init__(self, model_name) -> None:
        self.model_path = "/Users/duartemiranda/Desktop/side_projects/house_pricing/backend/housepricing/rest_api/LRegression/models/"
        self.mode_name = model_name
    def load_model(self):
        model = load(self.model_path+self.mode_name)
        return model


def make_predict(data):

    #reshape data
    if type(data) != type(list):
        data = [data]
    data = np.array(data).reshape(1, 12)

    model_name = "Linear_Regression_housing.joblib"
    model_loader = Model(model_name=model_name)
    model = model_loader.load_model()
    y = model.predict(data)
    return y
