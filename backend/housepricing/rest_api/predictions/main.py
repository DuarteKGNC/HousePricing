import os
from django.conf import settings
import pandas as pd


def start():
    subfilepath = 'rest_api/predictions/'
    filename = "Housing.csv"
    filepath = os.path.join(settings.BASE_DIR, subfilepath+filename)
    
    df = pd.read_csv(filepath)
    print(df.head())