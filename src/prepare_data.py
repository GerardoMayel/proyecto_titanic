import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def prepare_data():
    # Cargar datos
    data = pd.read_csv('data/raw/titanic.csv')
    
    # Seleccionar características relevantes
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = data[features]
    y = data['Survived']
    
    # Preprocesamiento
    # Convertir características categóricas
    X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})
    X['Embarked'] = X['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Imputar valores faltantes
    imputer = SimpleImputer(strategy='mean')
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    
    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Guardar datos procesados
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv('data/processed/titanic_processed.csv', index=False)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
