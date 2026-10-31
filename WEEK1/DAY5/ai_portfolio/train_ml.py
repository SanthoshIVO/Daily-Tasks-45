import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def train_and_save():
    print("Training Insurance Model...")
    df = pd.read_csv('D:/pysp1/Notes/FastAPI/projects/ML Project/insurance.csv')
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    obj_cols = ['sex', 'smoker', 'region']
    num_cols = ['age', 'bmi', 'children']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), obj_cols)
        ]
    )
    
    # Fit preprocessor and model
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)
    updated_xtrain = preprocessor.fit_transform(xtrain)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(updated_xtrain, ytrain)
    
    # Save both to the models folder
    joblib.dump(model, 'D:/pysp1/Notes/FastAPI/projects/ai_portfolio/models/insurance_model.joblib')
    joblib.dump(preprocessor, 'D:/pysp1/Notes/FastAPI/projects/ai_portfolio/models/preprocessor.joblib')
    print("Model and Preprocessor saved successfully!")

if __name__ == "__main__":
    train_and_save()
