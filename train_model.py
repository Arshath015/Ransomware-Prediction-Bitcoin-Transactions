import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("D:/project/data/Data.csv")

# Drop any columns that are not required
X = data.drop(columns=['label', 'address'])  # Drop 'address' and 'label'
y = data['label']

# Identify numeric and categorical columns
numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = []  # No categorical columns remaining

# Preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        # No categorical columns
    ])

# Create and train model pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))])

pipeline.fit(X, y)

# Save the trained model
joblib.dump(pipeline, 'model.pkl')

print("Model training complete and saved as 'model.pkl'")
