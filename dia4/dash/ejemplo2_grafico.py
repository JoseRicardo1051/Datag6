import dash
from dash import dcc,html
import pandas as pandas
import plotly.express as px
import seaborn as sns

app = dash.Dash(__name__)

#creamos grafico estadistico
df = sns.load_dataset('penguins')

app.layout = html.Div([
    html.H1("MI primer grafico con Ploty Dash"),
    dcc.Graph(
        figure=px.scatter(df,x='bill_length_mm',y='bill_depth_mm',
                          color='species',
                          title='Relación entre bill length y bill depth')
    )
])


if __name__ == '__main__':
    app.run(debug=True)