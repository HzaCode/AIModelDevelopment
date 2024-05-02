import pandas as pd
import plotly.express as px


data = {
    
}


df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])


colors = {
    "Development": "rgb(30,144,255)",
    "Data Preparation": "rgb(95,158,160)",
    "Training": "rgb(255,140,0)",
    "Optimization": "rgb(255,69,0)"
}

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",
                  title="<b>Development and Optimization of AI Models</b>",
                  color_discrete_map=colors,
                  template='plotly_white', height=800)


fig.update_layout({
    'bargap': 0.2,
    'xaxis': {
        'tickformat': "%b %Y",
        'ticklabelmode': "period",
        'ticks': "outside",
        'ticklen': 10
    },
    'yaxis': {
        'title': "Tasks",
        'autorange': "reversed"
    },
    'legend': {
        'title': "Model Stages:",
        'orientation': "h",
        'yanchor': "bottom",
        'y': 1.02,
        'xanchor': "right",
        'x': 1
    }
})


fig.show()
