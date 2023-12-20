import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Function to add weeks to a date
def add_weeks(start_date, weeks):
    return start_date + timedelta(weeks=weeks)

# Setting up the start date and exam period dates
start_date = datetime(2024, 1, 1)
if start_date.weekday() != 0:
    start_date += timedelta(days=(7 - start_date.weekday()))

exam_start = datetime(2024, 5, 1)
exam_end = datetime(2024, 6, 15)

# Correcting the code to handle the IndexError and allowing overlap between phases and exam periods

# Setting up the start date and exam period dates
start_date = datetime(2024, 1, 1)
exam_start_1 = datetime(2024, 5, 1)
exam_end_1 = datetime(2024, 6, 15)
exam_start_2 = datetime(2024, 11, 15)
exam_end_2 = datetime(2024, 12, 22)

# Defining the phases and their durations in weeks
phases = {
    "Planning and Research": 5, 
    "Prototype Development": 12,
    "Exam Break 1": (exam_end_1 - exam_start_1).days // 7,
    "Iterative Development and Testing": 20,
    "Exam Break 2": (exam_end_2 - exam_start_2).days // 7,
    "User Testing and Feedback": 6,
    "Final Review and Deployment": 4,
    "Maintenance and Improvement": 12  # ongoing, plotted as 12 weeks for visualization
}

# Calculating the start and end dates for each phase
dates = []
end_dates = []
current_date = start_date

for phase, duration in phases.items():
    if phase.startswith("Exam Break"):
        # Handling for exam break periods
        if phase == "Exam Break 1":
            current_date = exam_start_1
            end_date = exam_end_1
        elif phase == "Exam Break 2":
            current_date = exam_start_2
            end_date = exam_end_2
    else:
        # Regular phases start after the end of the last phase or exam break
        current_date = end_dates[-1] if end_dates else start_date
        end_date = add_weeks(current_date, duration)
    
    dates.append(current_date)
    end_dates.append(end_date)

# Creating the Gantt chart with overlap allowed
fig, ax = plt.subplots(figsize=(12, 7))
for i, (phase, duration) in enumerate(phases.items()):
    color = "red" if "Exam Break" in phase else "skyblue"
    ax.barh(phase, end_dates[i] - dates[i], left=dates[i], color=color, edgecolor='grey')

# Formatting the chart
ax.set_xlabel("Date")
ax.set_title("Adjusted Project Timeline Gantt Chart")
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)

# Set the x-axis to display real dates
ax.set_xlim(start_date, end_dates[-1])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)  # Tilt date labels to avoid overlap

# Keep y-axis labels horizontal
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()


