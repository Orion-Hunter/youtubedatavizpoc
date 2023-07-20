import os
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from service import tokenize, gen_world_cloud, gen_general_world_cloud, gen_total_world_cloud

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True


url_esquerda = "./data/CanaisEsquerda.xlsx"
url_direita = "./data/CanaisDireita.xlsx"

data_esquerda = pd.ExcelFile(url_esquerda)
data_direita = pd.ExcelFile(url_direita)

app = Dash(__name__)

server = app.server

general_world_cloud = gen_total_world_cloud(data_esquerda, data_direita)
general_world_cloud_esquerda = gen_general_world_cloud(data_esquerda)
general_world_cloud_direita = gen_general_world_cloud(data_direita)

app.layout = html.Div([
    html.Div([
            html.H2(children='Nuvem de Palavras dos Títulos de Vídeos(Todos os canais)', style={'textAlign':'center'}),
            dcc.Graph(figure=px.imshow(general_world_cloud), id=''),
  
        ], style={'width': '100%'}
    ),
    html.P(),
    html.Div([    
    html.Div([
            html.H2(children='Nuvem de Palavras dos Títulos de Vídeos(Todos os canais Esquerda)', style={'textAlign':'center'}),
            dcc.Graph(figure=px.imshow(general_world_cloud_esquerda), id=''),
  
        ], style={'width': '49%', 'display': 'inline-block'}
    ),    
    html.Div([
            html.H2(children='Nuvem de Palavras dos Títulos de Vídeos(Todos os canais Direita)', style={'textAlign':'center'}),
            dcc.Graph(figure=px.imshow(general_world_cloud_direita), id=''),
        ], style={'width': '49%', 'display': 'inline-block'}
    ),
    ], style={"display": "flex", "width": "100%"}),
    html.P(''),
     html.Div([
    html.Div([
            html.H2(children='Nuvem de Palavras(Por canal - Esquerda)', style={'textAlign':'center'}),
            dcc.Dropdown(data_esquerda.sheet_names[0:len(data_esquerda.sheet_names)-1],data_esquerda.sheet_names[0] ,id='dropdown-selection-esquerda'),
            dcc.Graph(figure={}, id='graph-content-esquerda')            
        ], style={'width': '49%', 'display': 'inline-block'}
    ),    
    html.Div([
          html.H2(children='Nuvem de Palavras(Por canal - Direita)', style={'textAlign':'center'}),
          dcc.Dropdown(data_direita.sheet_names[0:len(data_direita.sheet_names)-1],data_direita.sheet_names[0] ,id='dropdown-selection-direita'),
          dcc.Graph(figure={}, id='graph-content-direita'),     
        ], style={'width': '49%', 'display': 'inline-block'}
    ),
    ], style={"display": "flex", "width": "100%"}),
    
    
    
], style={"display": "inline-block", "width": "100%"})

@callback(
    Output('graph-content-esquerda', 'figure'),
    Input('dropdown-selection-esquerda', 'value')
)
def update_graph_esquerda(value):
    df = pd.read_excel(data_esquerda, sheet_name=value)
    column = df.columns[0]
    res= df[column]
    comment_words = tokenize(res)
    wordcloud = gen_world_cloud(comment_words)
    fig = px.imshow(wordcloud)
    return fig

@callback(
    Output('graph-content-direita', 'figure'),
    Input('dropdown-selection-direita', 'value')
)
def update_graph_direita(value):
    df = pd.read_excel(data_direita, sheet_name=value)
    column = df.columns[0]
    res= df[column]
    comment_words = tokenize(res)
    wordcloud = gen_world_cloud(comment_words)
    fig = px.imshow(wordcloud)
    return fig

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=debug, use_reloader=False)

