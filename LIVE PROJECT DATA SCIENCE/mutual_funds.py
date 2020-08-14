import requests
import datetime
import plotly.express as px
import plotly.graph_objs as go

ct = datetime.datetime.now() - datetime.timedelta(days=1)
x = str(ct.strftime('%d-%m-%Y'))


def date_5y():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=(366 * 5) - 2)
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def date_2y():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=(366 * 2))
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def date_y():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=(367))
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def date_6m():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=((92 * 2) - 1))
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def date_3m():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=(93))
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def date_m():
    ct = datetime.datetime.now() - datetime.timedelta(days=1)
    x = str(ct.strftime('%d-%m-%Y'))
    ct = datetime.datetime.now() - datetime.timedelta(days=(32))
    y = str(ct.strftime('%d-%m-%Y'))
    return y


def nav_cal(m1, x, y):
    x = (((float(list(filter(lambda person: person['date'] == x, m1))[0]["nav"]) - float(
        list(filter(lambda person: person['date'] == y, m1))[0]["nav"])) / float(
        list(filter(lambda person: person['date'] == y, m1))[0]["nav"])) * 100)
    return x


def nav_per(list):
    x = []
    for i in range(200):
        x.append(((float(list[i]) - float(list[i + 1])) / float(list[i + 1])) * 100)
    return x


def plot(df, mf,tit):
    from datetime import datetime
    dates = df
    DATE = [datetime.strptime(x, '%d-%m-%Y') for x in dates]

    fig = px.line(x=DATE, y=mf, title=tit, template="plotly_dark")

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all"),
            ])
        )
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=" NAV Growth(%)",

    )

    fig.show()


def plotbar(sa1,sa2,sa3,sa4,sa5,sa6):
    final = [sa1, sa2, sa3, sa4, sa5, sa6]
    rez = [[final[j][i] for j in range(len(final))] for i in range(len(final[0]))]

    branches = ['1 Month', '3 Month', '6 Month', '1 Year', '3 Year', '5 Year']
    trace1 = go.Bar(
        x=branches,
        y=rez[0],
        name=m2
    )
    trace2 = go.Bar(
        x=branches,
        y=rez[1],
        name=c2
    )
    trace3 = go.Bar(
        x=branches,
        y=rez[2],
        name=i2
    )

    trace4 = go.Bar(
        x=branches,
        y=rez[3],
        name=k2
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(barmode='group')
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(template="plotly_dark", title="Return Comparison(Based On Time)")
    fig.show()



ct = datetime.datetime.now() - datetime.timedelta(days=2)
x = str(ct.strftime('%d-%m-%Y'))
response = requests.get("https://api.mfapi.in/mf/107578")
mirae = response.json()
m1 = mirae["data"]
m2 = mirae["meta"]["scheme_name"]

ml = []
for i in range(201):
    ml.append(mirae["data"][i]["nav"])

mf = []
mf = nav_per(ml)

response = requests.get("https://api.mfapi.in/mf/113221")
canara = response.json()
c1 = canara["data"]
c2 = canara["meta"]["scheme_name"]
cl = []
for i in range(201):
    cl.append(canara["data"][i]["nav"])
cf = []
cf = nav_per(cl)

response = requests.get("https://api.mfapi.in/mf/108799")
idfc = response.json()
i1 = idfc["data"]
i2 = idfc["meta"]["scheme_name"]
il = []
for i in range(201):
    il.append(idfc["data"][i]["nav"])

if1 = []
if1 = nav_per(il)

response = requests.get("https://api.mfapi.in/mf/114458")
kotak = response.json()
k1 = kotak["data"]
k2 = kotak["meta"]["scheme_name"]
kl = []
df = []
for i in range(201):
    kl.append(kotak["data"][i]["nav"])
for i in range(200):
    df.append(kotak["data"][i]["date"])
kf = []
kf = nav_per(kl)

# dict for one month return
y = date_m()
sa1 = [ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

# dict for three month return
y = date_3m()
sa2 = [ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

# dict for 6 month
y = date_6m()
sa3 = [ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

# dict for 1 year
y = date_y()
sa4 =[ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

# dict for 2 year
y = date_2y()
sa5 = [ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

# dict for 5 year
y = date_5y()
sa6 = [ nav_cal(m1, x, y), nav_cal(c1, x, y), nav_cal(i1, x, y), nav_cal(k1, x, y)]

plotbar(sa1,sa2,sa3,sa4,sa5,sa6)
plot(df,mf,m2)
plot(df,cf,c2)
plot(df,if1,i2)
plot(df,kf,k2)
