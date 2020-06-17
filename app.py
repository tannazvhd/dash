import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



def generate_Dropdown():
    return dcc.Dropdown(
        id='',
        options=[{'label': i, 'value': i} for i in {1,2,3}],
        value=''
    )


app.layout = html.Div(children=[
    html.Div(className=' container row', children=[
        html.Div(className='row', children=[
            html.Div(className='six columns',
                children=[
                    html.H1('Dash Assignment', style={'color': 'black','float':'left'})
                ])
        ]),
        html.Div(className='row', children=[
            html.Div(className='four columns',
                children=[
                    html.H1('Select Students', style={'color': 'black','float': 'left','font-size':'16pt'})
                ]),
            html.Div(className='four columns',
                children=[
                    html.H1('Last clicked course information', style={'color': 'black', 'float': 'left','font-size':'16pt'})
                ]),
        ]),
        html.Div(className='row', children=[
            html.Div(className='four columns',
                children=[
                    generate_Dropdown(),
                ]),
            html.Div(className='four columns',
                children=[
                    html.H1('No course clicked ingrades graph', style={'color': 'darkgrey', 'float': 'left','font-size':'12pt'}),
                    html.H1('No course clicked ingrades graph', style={'color': 'darkgrey', 'float': 'left','font-size':'12pt'})

                ]),
        ]),
        html.Div(className='row', children=[
            html.Div(className='six columns',
                children=[
                    html.H1('Students average grades', style={'color': 'black','font-size':'13pt','text-align':'center' })
                ]),
            html.Div(className='six columns',
                children=[
                    html.H1('Average weekly hours spend by students', style={'color': 'black','font-size':'13pt','text-align':'center'})
                ]),
        ]),
        html.Div(className='row', children=[
            html.Div(className='six columns',
                children=[
                    html.H1('here comes the first graph', style={'color': 'blue','font-size':'13pt','text-align':'center' })
                ]),
            html.Div(className='six columns',
                children=[
                    html.H1('here comes the second graph', style={'color': 'blue','font-size':'13pt','text-align':'center'})
                ]),
        ]),

    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)