import bokeh.charts
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure

def plot_interactive_timeseries(df, col):

    hover = HoverTool(tooltips=[
        ("y (%s)" % col, "$y{1.11}"),
        ("Date", "@DateStr"),
        ("LastPrice", "@LastPrice{1.11}"),
        ("LowPrice", "@LowPrice{1.11}"),
        ("HighPrice", "@HighPrice{1.11}"),
        ("AvgPrice", "@AvgPrice{1.11}"),
        ("Units", "@Units{int}"),
        ("Volume", "@Volume{1.11}")
    ])

    p = figure(
        plot_width=bokeh.charts.defaults.width, 
        plot_height=bokeh.charts.defaults.height, 
        x_axis_type="datetime",
        title="PRES16_WTA: Date vs %s" % col)

    for contract, group in df.groupby('Contract'):
        source = ColumnDataSource(group)
        source.add(group.Date.map(lambda x: x.strftime('%x')), 'DateStr')
        color = "blue" if contract == "DEM16_WTA" else ("red" if contract == "REP16_WTA" else "black")
        p.line(x='Date', y=col, color=color, legend=contract,
               line_width=2, 
               source=source)
    p.add_tools(hover)

    p.xaxis.axis_label = "Date"
    p.yaxis.axis_label = col
    p.legend.location = "top_left"
    p.logo = None

    return p

def simple_plot_interactive_timeseries(df, col):

    p = TimeSeries(
        df.pivot(index='Date', columns='Contract', values=col).sort_index(axis=1).reset_index(),
        x='Date', y=['DEM16_WTA', 'REP16_WTA'], 
        ylabel=col, legend=True, color=['blue', 'red'])

    return p