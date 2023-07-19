from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from service import tokenize, gen_world_cloud, gen_general_world_cloud

url = "data/reportcanais.xlsx"
data = pd.ExcelFile(url)


app = Dash(__name__)

server = app.server

general_world_cloud = gen_general_world_cloud(data)

app.layout = html.Div([
    html.H1(children='Nuvem de Palavras dos Títulos de Vídeos(Todos os canais)', style={'textAlign':'center'}),
    dcc.Graph(figure=px.imshow(general_world_cloud), id=''),
    html.P(''),   
    html.H1(children='Nuvem de Palavras dos Títulos de Vídeos(Por canal)', style={'textAlign':'center'}),
    dcc.Dropdown(data.sheet_names[0:len(data.sheet_names)-1],data.sheet_names[0] ,id='dropdown-selection'),
    dcc.Graph(figure={}, id='graph-content')
])


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    df = pd.read_excel(data, sheet_name=value)
    column = df.columns[0]
    res= df[column]
    comment_words = tokenize(res)
    wordcloud = gen_world_cloud(comment_words)
    fig = px.imshow(wordcloud)
    return fig
    
if __name__ == '__main__':
    app.run(debug=True)

