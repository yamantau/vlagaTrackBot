import plotly
import plotly.graph_objs as go
import pymongo

client = pymongo.MongoClient("mongodb+srv://vlaga:3lPDBLWuAM1u6lbH@cluster0.jztcayu.mongodb.net/?retryWrites=true&w=majority")

def make_graph(min, INFO):

    fig = go.Figure()
    fig.update_layout(title=INFO)

    def get_x_y(db):
        x = []
        y = []
        count = 0
        summ = 0
        candle = 12

        if min > 180:
            candle = 60
        elif min > 900:
            candle = 120

        for item in db.find().skip(db.count_documents({}) - min * 12):
            count += 1
            summ += item['rate']
            if count % candle == 0:
                avg = summ / count
                y.append(avg)
                x.append(item['date'])
                count = 0
                summ = 0
        fig.add_trace(go.Scatter(x=x, y=y, line_shape='spline'))

    get_x_y(client.binance[INFO + '_buy'])
    get_x_y(client.binance[INFO + '_sell'])

    plotly.io.write_image(fig, file='my_figure_file.png', format='png')