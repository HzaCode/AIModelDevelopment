import pandas as pd
import plotly.express as px


df = pd.read_csv(r'gantt_chart_new.csv', encoding='latin1')
df['Start'] = df['Start'].astype('datetime64')
df['Finish'] = df['Finish'].astype('datetime64')

#set label colors
colors = {
    '': 'rgb(30,144,255)', '': 'rgb(211,211,211)',
    '': 'rgb(95,158,160)', '': 'rgb(0,0,128)', '': 'rgb(211,211,210)'
}


fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", hover_name="Task",
                  color_discrete_sequence=px.colors.qualitative.Prism, opacity=.7, color='Dimension',
                  title="<b>IE 3.0 Gantt Chart 2021</b>", height=1200)


fig.update_layout(
    bargap=0.5, bargroupgap=0.1,
    xaxis=dict(
        showgrid=True, rangeslider_visible=True, side="top", tickmode='array', dtick="M1",
        tickformat="Q%q %Y \n", ticklabelmode="period", ticks="outside", tickson="boundaries",
        tickwidth=.1, layer='below traces', ticklen=20,
        tickfont=dict(family='Old Standard TT, serif', size=24, color='gray'),
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]), x=.37, y=-.05, font=dict(family="Arial", size=14, color="darkgray")
        )
    ),
    yaxis=dict(
        title="", autorange="reversed", automargin=True,
        ticklen=10, showgrid=True, showticklabels=True,
        tickfont=dict(family='Old Standard TT, serif', size=16, color='gray')
    ),
    legend=dict(
        orientation="h", yanchor="bottom", y=1.1, title="", xanchor="right", x=1,
        font=dict(family="Arial", size=14, color="darkgray")
    )
)

fig.update_traces(marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.95)

fig.write_html("gantt_chart.html")

fig.show()
