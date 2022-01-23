import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go # or plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

emotionele_stabiliteit_lijst = []
openheid_lijst = []
veilgheidsbewust_lijst = []
loyaliteit_lijst = []
onafhankelijkheid_lijst = []

'''
Vragenlijst antwoorden client

Per onderwerp staan hier de antwoorden die de cliënt heeft gegeven.
'''
# Vraag ?
emotionele_stabiliteit_lijst.append('b') 
# Vraag ?
emotionele_stabiliteit_lijst.append('b') 
# Vraag ?
emotionele_stabiliteit_lijst.append('b')
# Vraag ?
openheid_lijst.append('b')
# Vraag ?
openheid_lijst.append('b') 
# Vraag ?
openheid_lijst.append('b') 
# Vraag ?
veilgheidsbewust_lijst.append('b') 
# Vraag ?
veilgheidsbewust_lijst.append('b') 
# Vraag ?
veilgheidsbewust_lijst.append('a')
# Vraag ?
loyaliteit_lijst.append('b') 
# Vraag ?
loyaliteit_lijst.append('b') 
# Vraag ?
loyaliteit_lijst.append('a') 
# Vraag ?
onafhankelijkheid_lijst.append('b') 
# Vraag ?
onafhankelijkheid_lijst.append('b') 
# Vraag ?
onafhankelijkheid_lijst.append('a')

'''
Scores client berekenen
'''
# Emotionele stabiliteit berekenen
emotionele_stabiliteit_points = 0
if emotionele_stabiliteit_lijst[0].lower() == 'a':
    emotionele_stabiliteit_points += 1
if emotionele_stabiliteit_lijst[1].lower() == 'b':
    emotionele_stabiliteit_points += 1 
if emotionele_stabiliteit_lijst[2].lower() == 'b':
    emotionele_stabiliteit_points += 1 
emotionele_stabiliteit_percentage = round(emotionele_stabiliteit_points/len(emotionele_stabiliteit_lijst)*100)

# Openheid berekenen
openheid_points = 0
if openheid_lijst[0].lower() == 'a':
    openheid_points += 1
if openheid_lijst[1].lower() == 'b':
    openheid_points += 1
if openheid_lijst[2].lower() == 'b':
    openheid_points += 1
openheid_percentage = round(openheid_points/len(openheid_lijst)*100)

# Veiligheidsbewust berekenen
veiligheidsbewust_points = 0
if veilgheidsbewust_lijst[0].lower() == 'a':
    veiligheidsbewust_points += 1
if veilgheidsbewust_lijst[1].lower() == 'b':
    veiligheidsbewust_points += 1
if veilgheidsbewust_lijst[2].lower() == 'a':
    veiligheidsbewust_points += 1  
veiligheidsbewust_percentage = round(veiligheidsbewust_points/len(veilgheidsbewust_lijst)*100)

# Loyaliteit berekenen
loyaliteit_points = 0
if loyaliteit_lijst[0].lower() == 'a':
    loyaliteit_points += 1
if loyaliteit_lijst[1].lower() == 'b':
    loyaliteit_points += 1
if loyaliteit_lijst[2].lower() == 'a':
    loyaliteit_points += 1  
loyaliteit_percentage = round(loyaliteit_points/len(loyaliteit_lijst)*100)

# Onafhankelijkheid berekenen
onafhankelijkheid_points = 0
if onafhankelijkheid_lijst[0].lower() == 'a':
    onafhankelijkheid_points += 1
if onafhankelijkheid_lijst[1].lower() == 'b':
    onafhankelijkheid_points += 1
if onafhankelijkheid_lijst[2].lower() == 'a':
    onafhankelijkheid_points += 1  
onafhankelijkheid_percentage = round(onafhankelijkheid_points/len(onafhankelijkheid_lijst)*100)

'''
Figures
'''
fig_emotionele_stabiliteit = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig_emotionele_stabiliteit = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = emotionele_stabiliteit_percentage,
    mode = "gauge+number+delta",
    title = {'text': ""},
    delta = {'reference': 100},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 3, 'tickcolor': "black"},
        'bar': {'color': "darkgrey"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 25], 'color': "green"},
            {'range': [26, 50], 'color': "yellow"},
            {'range': [51, 74], 'color': "orange"},
            {'range': [75, 100], 'color': "red"}],
        }))

fig_openheid = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig_openheid = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = openheid_percentage,
    mode = "gauge+number+delta",
    title = {'text': ""},
    delta = {'reference': 100},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 3, 'tickcolor': "black"},
        'bar': {'color': "darkgrey"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 25], 'color': "green"},
            {'range': [26, 50], 'color': "yellow"},
            {'range': [51, 74], 'color': "orange"},
            {'range': [75, 100], 'color': "red"}],
        }))

fig_veiligheidsbewust = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig_veiligheidsbewust = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = veiligheidsbewust_percentage,
    mode = "gauge+number+delta",
    title = {'text': ""},
    delta = {'reference': 100},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 3, 'tickcolor': "black"},
        'bar': {'color': "darkgrey"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 25], 'color': "green"},
            {'range': [26, 50], 'color': "yellow"},
            {'range': [51, 74], 'color': "orange"},
            {'range': [75, 100], 'color': "red"}],
        }))

fig_loyaliteit = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig_loyaliteit = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = loyaliteit_percentage,
    mode = "gauge+number+delta",
    title = {'text': ""},
    delta = {'reference': 100},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 3, 'tickcolor': "black"},
        'bar': {'color': "darkgrey"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 25], 'color': "green"},
            {'range': [26, 50], 'color': "yellow"},
            {'range': [51, 74], 'color': "orange"},
            {'range': [75, 100], 'color': "red"}],
        }))

fig_onafhankelijkheid = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig_onafhankelijkheid = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = onafhankelijkheid_percentage,
    mode = "gauge+number+delta",
    title = {'text': ""},
    delta = {'reference': 100},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 3, 'tickcolor': "black"},
        'bar': {'color': "darkgrey"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 25], 'color': "green"},
            {'range': [26, 50], 'color': "yellow"},
            {'range': [51, 74], 'color': "orange"},
            {'range': [75, 100], 'color': "red"}],
        }))

'''
Layout
'''
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Uitslag'),

        html.Div(children='''
            Hier is de uitkomst van de test
        '''),  
    ]),
    # All elements from the top of the page
    html.Div([
        html.H4(children='Emotionele stabiliteit'),

        dcc.Graph(
            id='graph1',
            figure=fig_emotionele_stabiliteit
        ),  
    ]),
    html.Div([
        html.H4(children='Openheid'),

        dcc.Graph(
            id='graph2',
            figure=fig_openheid
        ),  
    ]),
    html.Div([
        html.H4(children='Veiligheidsbewust'),

        dcc.Graph(
            id='graph3',
            figure=fig_veiligheidsbewust
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H4(children='Loyaliteit'),

        dcc.Graph(
            id='graph4',
            figure=fig_loyaliteit
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H4(children='Onafhankelijkheid'),

        dcc.Graph(
            id='graph5',
            figure=fig_onafhankelijkheid
        ),  
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)