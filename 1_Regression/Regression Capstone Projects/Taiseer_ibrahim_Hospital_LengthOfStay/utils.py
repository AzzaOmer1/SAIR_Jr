# utils.py snippet
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class AdvancedFeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, Y=None):
            return self  # No fitting needed for this transformer
        
    def transform(self, X):
        #X_eng = X.copy()
        X_eng = np.asarray(X, dtype=float).copy()
        # comorb_count: comorbidity count (the sum of other dises)
        X_eng = np.column_stack([
            X_eng,
        # comord_count
            np.sum(X_eng[:, 1:12], axis=1)
                
            
        ])
            
     
            
            
            
        return X_eng


class OutlierHandler(BaseEstimator, TransformerMixin):
    def __init__(self, factor=1.5): self.factor = factor
    def fit(self, X, y=None):
        X_arr = X.values if isinstance(X, pd.DataFrame) else X
        self.lower_bounds_ = [np.percentile(X_arr[:,i],25) - self.factor*(np.percentile(X_arr[:,i],75)-np.percentile(X_arr[:,i],25)) for i in range(X_arr.shape[1])]
        self.upper_bounds_ = [np.percentile(X_arr[:,i],75) + self.factor*(np.percentile(X_arr[:,i],75)-np.percentile(X_arr[:,i],25)) for i in range(X_arr.shape[1])]
        return self
    def transform(self, X):
        X_arr = X.values if isinstance(X, pd.DataFrame) else X.copy()
        for i in range(X_arr.shape[1]):
            X_arr[:,i] = np.clip(X_arr[:,i], self.lower_bounds_[i], self.upper_bounds_[i])
        return X_arr