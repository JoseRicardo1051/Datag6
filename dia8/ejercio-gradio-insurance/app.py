import joblib
import numpy as np
import pandas as pd
import gradio as gr

# Cargar el modelo y los scalers
loaded_model = joblib.load('model.pkl')
loaded_scaler_X = joblib.load('scaler_X.pkl')
loaded_scaler_y = joblib.load('scaler_y.pkl')

def predict_price(
    sex: float,
    smoker: float,
    region: str,
    age: float,
    bmi: float,
    children: float
) -> float:
    # Crear un array con los valores de entrada en el orden correcto
    input_list = []
    if region == 'northeast':
      input_list = [sex,smoker,1.0,0.0,0.0,0.0,age,bmi,children]
    elif region == 'northwest':
      input_list = [sex,smoker,0.0,1.0,0.0,0.0,age,bmi,children]
    elif region == 'southeast':
      input_list = [sex,smoker,0.0,0.0,1.0,0.0,age,bmi,children]
    elif region == 'southwest':
      input_list = [sex,smoker,0.0,0.0,0.0,1.0,age,bmi,children]
    
    print(input_list)
            
    input_data = np.array(input_list).reshape(1, -1)

    # Escalar las características de entrada usando el scaler_X cargado
    input_scaled = loaded_scaler_X.transform(input_data)

    # Realizar la predicción con el modelo cargado
    predicted_charge_scaled = loaded_model.predict(input_scaled)

    # Invertir la escala de la predicción usando el scaler_y cargado
    predicted_charge = loaded_scaler_y.inverse_transform(predicted_charge_scaled.reshape(-1, 1))

    return round(predicted_charge[0][0],2)

# Definir los componentes de entrada para Gradio
sex_input = gr.Radio([("Female", 0.0), ("Male", 1.0)], label="Sex", value=0.0)
smoker_input = gr.Radio([("No", 0.0), ("Yes", 1.0)], label="Smoker", value=0.0)
region_input = gr.Radio(["northeast", "northwest", "southeast", "southwest"], label="Region", value="southwest")
age_input = gr.Slider(minimum=18, maximum=100, step=1, label="Age", value=30)
bmi_input = gr.Slider(minimum=15.0, maximum=55.0, step=0.1, label="BMI", value=25.0)
children_input = gr.Slider(minimum=0, maximum=10, step=1, label="Children", value=1)

# Definir el componente de salida
output = gr.Number(label="Predicted Insurance Cost ($)")

# Crear la interfaz Gradio
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        sex_input,
        smoker_input,
        region_input,
        age_input,
        bmi_input,
        children_input
    ],
    outputs=output,
    title="Insurance Cost Prediction",
    description="Enter the client's details to predict their insurance cost."
)

# Lanzar la interfaz
iface.launch()
