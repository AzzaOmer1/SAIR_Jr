import pandas as pd
import numpy as np
from datetime import datetime  # 📅 استيراد مكتبة التاريخ
from sklearn.base import BaseEstimator, TransformerMixin

class AdvancedFeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.feature_names = []
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        
        if not isinstance(X, pd.DataFrame):
            X_df = pd.DataFrame(X)
        else:
            X_df = X.copy()
            
        numeric_cols_to_check = ['Year', 'Engine Size', 'Mileage']
        for col in numeric_cols_to_check:
            if col in X_df.columns:
                X_df[col] = pd.to_numeric(X_df[col], errors='coerce').fillna(0)
                
        if 'Year' in X_df.columns:
            
            current_year = datetime.now().year
            X_df['Car_Age'] = current_year - X_df['Year']
            
        self.feature_names = list(X_df.columns)
        return X_df
    
    def get_feature_names_out(self, input_features=None):
        return np.array(self.feature_names)