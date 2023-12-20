import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import networkx as nx

from datetime import datetime, timedelta

def add_weeks(start_date, weeks):
    return start_date + timedelta(weeks=weeks)

start_date = datetime(2024, 1, 1)
if start_date.weekday() != 0:
    start_date += timedelta(days=(7 - start_date.weekday()))

exam_start = datetime(2024, 5, 1)
exam_end = datetime(2024, 6, 15)

adjusted_phases = {
    'Planning and Research': 4,
    'Prototype Development': 8,
    'Exam Break': (exam_end - exam_start).days // 7,
    'Iterative Development and Testing': 16,
    'User Testing and Feedback': 6,
    'Final Review and Deployment': 4,
    'Maintenance and Improvement': 12
}

dates = [start_date]
for phase, duration in adjusted_phases.items():
    if phase == 'Exam Break':
        end_date = exam_end
    else:
        end_date = add_weeks(dates[-1], duration)
    dates.append(end_date)

fig, ax = plt.subplots(figsize=(12, 7))
for i, (phase, duration) in enumerate(adjusted_phases.items()):
    ax.barh(phase, duration * 7, left=(dates[i] - start_date).days, color='skyblue', edgecolor='grey')

ax.set_xlabel('Weeks since project start')
ax.set_title('Adjusted Project Timeline Gantt Chart')
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)

locator = mdates.AutoDateLocator(minticks=5, maxticks=15)
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

plt.tight_layout()

# Adjusting the flowchart to better represent the iterative development process

# Creating a directed graph for the flowchart
G = nx.DiGraph()

# Adding nodes for algorithm options
G.add_node("Start", pos=(0, 4), color='lightblue')
G.add_node("Linear Programming", pos=(0, 3), color='skyblue')
G.add_node("Mixed-Integer Programming", pos=(1, 3), color='skyblue')
G.add_node("Local Search Algorithms", pos=(2, 3), color='skyblue')

# Adding nodes for iterative development stages
G.add_node("Prototype Development", pos=(0, 2), color='lightgreen')
G.add_node("Feature Expansion", pos=(1, 2), color='lightgreen')
G.add_node("Refinement & Testing", pos=(2, 2), color='lightgreen')

# Adding node for final deployment
G.add_node("Final Deployment", pos=(1, 1), color='salmon')

# Connecting start to algorithm options
G.add_edge("Start", "Linear Programming")
G.add_edge("Start", "Mixed-Integer Programming")
G.add_edge("Start", "Local Search Algorithms")

# Connecting algorithm options to iterative stages
G.add_edge("Linear Programming", "Prototype Development")
G.add_edge("Mixed-Integer Programming", "Prototype Development")
G.add_edge("Local Search Algorithms", "Prototype Development")

G.add_edge("Prototype Development", "Feature Expansion")
G.add_edge("Feature Expansion", "Refinement & Testing")

# Creating iterative loops
G.add_edge("Refinement & Testing", "Prototype Development")
G.add_edge("Feature Expansion", "Prototype Development")

# Connecting to final deployment
G.add_edge("Refinement & Testing", "Final Deployment")

# Drawing the graph
plt.figure(figsize=(10, 8))
pos = nx.get_node_attributes(G, 'pos')
colors = [G.nodes[n]['color'] for n in G.nodes]

nx.draw(G, pos, with_labels=True, node_color=colors, node_size=4000, edge_color='grey', font_size=10, arrows=True)
plt.title("Iterative Project Development Flow Chart")
plt.show()

