import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Create a Plotly figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    #app.run_server(debug=True)
    # Make the app accessible from other devices on the local network; 10.60.57.78 is my Local IP address
    # Open a web browser on another device on the same local network and go to http://<your-local-ip>:8050/. 
    # Replace <your-local-ip> with the IP address you found in the previous step.
    app.run_server(host='0.0.0.0', port=8050, debug=True)
