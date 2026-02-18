import gradio as gr
import joblib
import numpy as np

model = joblib.load('model.pkl')
scaler_x = joblib.load('scaler_x.pkl')
scaler_y = joblib.load('scaler_y.pkl')

def predict_price(rooms):

  x = np.array([rooms])
  x_scaled = scaler_x.transform(x.reshape(-1,1))
  y_scaled = model.predict(x_scaled)
  y = scaler_y.inverse_transform(y_scaled)
  price = round(y[0][0],2)
  return price

    
import gradio as gr

inputs = [
    gr.Number(label='Número de habitaciones')
]

outputs = [
    gr.Textbox(label='Precio estimado')
]

gr.Interface(
    fn=predict_price,
    inputs=inputs,
    outputs=outputs,
    title='Predicción de precios de casas'
).launch(debug=False)