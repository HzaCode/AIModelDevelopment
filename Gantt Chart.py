from datetime import datetime, timedelta 
from IPython.display import display, HTML
import pandas as pd  
import calendar

file_path = "project_plan.xlsx"
def load_tasks_from_excel(file_path):
    df = pd.read_excel(file_path)
    tasks = []
    for _, row in df.iterrows():
        task = {
            "name": row["Task"],
            "start": row["Start"],
            "end": row["End"],
            "model": row["Model"],
            "progress": row["Progress"]
        }
        tasks.append(task)
    return tasks

start_date = datetime(2024, 5, 1)  
end_date = datetime(2024, 9, 30)
current_date = datetime(2024, 5, 13)

total_days = (end_date - start_date).days

model_colors = {
   
}

milestones = [
    {
        "name": "Milestone 1: ",
        "date": datetime(2024, 6, 23)
    },
    {
        "name": "Milestone 2: ", 
        "date": datetime(2024, 9, 1)  
    },
    {  
        "name": "Milestone 3: ",
        "date": datetime(2024, 9, 29)
    }
]

table_style = "width:100%; border: 1px solid black; border-collapse: collapse;"
header_row_style = "background-color: #f2f2f2;"  
task_header_style = "width: 10%;"
model_header_style = "width: 5%;"  
timeline_header_style = "width: 85%;"

time_scale_style = "width:100%; height: 80px; background-color: #f1f1f1; position: relative;"
month_mark_style = "position: absolute; left: {}%; width: 2px; height: 30px; background-color: #c00;" 
month_text_style = "position: absolute; left: {}%; top: 35px; transform: rotate(45deg); transform-origin: left top;" 
week_mark_style = "position: absolute; left: {}%; width: 1px; height: 15px; background-color: #333;"  
week_text_style = "position: absolute; left: {}%; top: 20px; font-size: 12px;"
milestone_style = "position: absolute; left: {}%; top: 60px; width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 12px solid {};"
milestone_text_style = "position: absolute; left: {}%; top: 80px; font-size: 12px; transform: rotate(45deg); transform-origin: left top; width: 150px;"

html = f"<table style='{table_style}'>"
html += f"<tr style='{header_row_style}'><th style='{task_header_style}'>Task</th><th style='{model_header_style}'>Model</th><th style='{timeline_header_style}'>Time Span</th></tr>"

time_scale_html = f"<div style='{time_scale_style}'>"

start_date_mark = start_date.strftime('%m/%d') 
time_scale_html += f"<div style='position: absolute; left: 0%; top: 0px;'>{start_date_mark}</div>"

end_date_mark = end_date.strftime('%m/%d')
time_scale_html += f"<div style='position: absolute; right: 0%; top: 0px;'>{end_date_mark}</div>" 

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 6:  
        left_percent = ((current_date - start_date).days / total_days) * 100
        time_scale_html += f"<div style='{week_mark_style.format(left_percent)}'></div>"
        time_scale_html += f"<div style='{week_text_style.format(left_percent)}'>{current_date.strftime('%m/%d')}</div>"
    current_date += timedelta(days=1)  
        
current_month_start = start_date
while current_month_start < end_date:
    days_in_month = calendar.monthrange(current_month_start.year, current_month_start.month)[1] 
    next_month_start = current_month_start + timedelta(days=days_in_month)
    
    while current_month_start.weekday() != 6:  
        current_month_start += timedelta(days=1)
    
    left_percent = ((current_month_start - start_date).days / total_days) * 100  
    time_scale_html += f"<div style='{month_mark_style.format(left_percent)}'></div>"
    time_scale_html += f"<div style='{month_text_style.format(left_percent)}'>{current_month_start.strftime('%Y-%m')}</div>" 
    
    current_month_start = next_month_start
for milestone in milestones:
    left_percent = ((milestone['date'] - start_date).days / total_days) * 100
    milestone_color = "#4a4a4a" 
    for model, color in model_colors.items():
        if model in milestone['name']:
            milestone_color = color
            break
    time_scale_html += f"<div style='{milestone_style.format(left_percent, milestone_color)}'></div>"
    time_scale_html += f"<div style='{milestone_text_style.format(left_percent)}'>{milestone['name']}</div>"

html += f"<tr><td></td><td></td><td>{time_scale_html}</td></tr>"

tasks = load_tasks_from_excel("project_plan.xlsx")  

task_row_height = 30  
light_gray = "#d3d3d3"
timeline_height = 65
task_bar_style = "width: 100%; background-color: #ddd; position: relative; height: 30px;"
task_duration_style = "position: absolute; left: {}%; width: {}%; background-color: {}; height: 80%; top: 10%; border-radius: 4px;"  
task_progress_style = "position: absolute; left: {}%; width: {}%; background-color: {}; height: 80%; top: 10%; border-radius: 4px;"
task_dependency_style = "position: absolute; left: {}%; bottom: 40%; width: 1px; border-right: 2px dashed {}; height: {}px;"
task_name_style = "position: absolute; left: 4px; top: 50%; transform: translateY(-50%); font-size: 14px; color: white; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);"

for task_index, task in enumerate(tasks): 
    start_percent = ((task["start"] - start_date).days / total_days) * 100
    end_percent = ((task["end"] - start_date).days / total_days) * 100  
    progress_percent = start_percent + (end_percent - start_percent) * task["progress"] / 100

    task_bar_html = f"<div style='{task_bar_style}'>"
    task_bar_html += f"<div style='{task_duration_style.format(start_percent, end_percent - start_percent, model_colors[task['model']])}'></div>" 
    task_bar_html += f"<div style='{task_progress_style.format(start_percent, progress_percent - start_percent, model_colors[task['model']])}'></div>"
    task_bar_html += f"<div style='{task_name_style}'>{task['name']}</div>"
    
    if task_index > 0:  
        line_height = timeline_height * (task_index + 1) - task_row_height  
        task_bar_html += f"<div style='{task_dependency_style.format(end_percent, light_gray, line_height)}'></div>"

    task_bar_html += "</div>"  
    html += f"<tr><td></td><td style='background-color: {model_colors[task['model']]}'>{task['model']}</td><td>{task_bar_html}</td></tr>"

legend_html = "<div style='margin-top: 20px;'>"
for model, color in model_colors.items(): 
    legend_html += f"<div style='margin-right: 20px; display: inline-block;'><div style='width: 20px; height: 20px; background-color: {color}; display: inline-block; margin-right: 5px;'></div>{model}</div>"
legend_html += "</div>"

html += "</table>"
html += legend_html
display(HTML(html))
