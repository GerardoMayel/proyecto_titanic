from src.prepare_data import prepare_data
from src.train_model import train_model
from src.predict import load_model, predict
from sklearn.metrics import accuracy_score, classification_report

def main():
    # Preparar datos
    X_train, X_test, y_train, y_test = prepare_data()
    
    # Entrenar modelo
    model = train_model(X_train, y_train)
    
    # Evaluar modelo
    y_pred = predict(model, X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy:.2f}")
    
    # Imprimir reporte de clasificación
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))
    
    # Ejemplo de predicción
    print("\nEjemplo de predicción:")
    ejemplo = X_test[:1]  # Usar el primer ejemplo del conjunto de prueba
    prediccion = predict(model, ejemplo)
    print(f"Características del pasajero: {ejemplo}")
    print(f"Predicción de supervivencia: {'Sobrevivió' if prediccion[0] == 1 else 'No sobrevivió'}")

if __name__ == "__main__":
    main()
