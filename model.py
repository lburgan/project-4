

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings("ignore")


csv = Path("titanic.csv")
titanic_df = pd.read_csv(csv)
titanic_df.head()


#drop unecessary columns
titanic_df = titanic_df.drop(["name","ticket","cabin","boat","body","home.dest"], axis = 1)


#get rid of missing values 
new_df = titanic_df.dropna()


dummy_df = pd.get_dummies(new_df)
dummy_df.head()

# Getting target, features and train/testing/splitting the data 
y_rf = dummy_df["survived"].values.reshape(-1, 1)
X_rf = dummy_df.drop("survived", axis = 1)
X_trainRF, X_testRF, y_trainRF, y_testRF = train_test_split(X_rf, y_rf, random_state=1912)


# Scaling the data 
scaler = StandardScaler()
X_scalerRF = scaler.fit(X_trainRF)
X_train_scaledRF = X_scalerRF.transform(X_trainRF)
X_test_scaledRF = X_scalerRF.transform(X_testRF)


# Creating the Random Forest mode
rf_model = RandomForestClassifier(n_estimators=1000, random_state=78)


# Fitting the model 
rf_model = rf_model.fit(X_train_scaledRF, y_trainRF.ravel())

# Making predictions 
predictionsRF = rf_model.predict(X_test_scaledRF)

# Getting the accuracy score 
accuracy_score(y_testRF,predictionsRF)


def predict_titanic(demo_list):
    male = 0
    female = 0
    embarked_C = 0
    embarked_Q = 0
    embarked_S = 0
    
    if demo_list[5] == "M":
        female = 0 
        male = 1
    elif demo_list[5] == "F":
        female = 1
        male == 0
    if demo_list[6] == "Cherbourg":
        embarked_C = 1
        embarked_Q = 0
        embarked_S = 0
    elif demo_list[6] == "Queenstown":
        embarked_C = 0
        embarked_Q = 1
        embarked_S = 0 
    elif demo_list[6] == "Southampton":
        embarked_C = 0
        embarked_Q = 0
        embarked_S = 1
    x_data = pd.DataFrame({"pclass": int(demo_list[0]),
                           "age":int(demo_list[1]), 
                           "sibsp":int(demo_list[2]),
                           "parch":int(demo_list[3]),
                           "fare":int(demo_list[4]),
                           "sex_female":female,
                           "sex_male":male,
                           "embarked_C":embarked_C,
                          "embarked_Q":embarked_Q,
                          "embarked_S":embarked_S},index=[0])
    X_scaler = X_scalerRF.transform(x_data)
    prediction = rf_model.predict(X_scaler)
    if prediction[0] > 0:
        return("survived")
    else:
        return("perished")
    



    
        
        


