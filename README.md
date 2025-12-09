# Data Analysis & Visualization

This project demonstrates my hands-on experience in analyzing data and creating meaningful visualizations. It highlights my research, problem-solving, and data interpretation skills, showing readiness to contribute as a Graduate Assistant.

## Project Overview
- Collected and analyzed data for insights.
- Generated clear and informative graphs for easy interpretation.
- Focused on research, data visualization, and professional presentation.

## Files
- `graph.png` → Visualization created from the analysis.
- `README.md` → Project summary and details.

## Skills Demonstrated
- #DataAnalysis #DataVisualization #ResearchExperience  
- #ProblemSolving #GraduateAssistantship #Portfolio  
- #Graphs #ProfessionalPresentation  

## Notes
- Completed independently as part of preparation for Graduate Assistantship application.
- Emphasis on clarity, reproducibility, and professional presentation.

## Code preview(python)
import matplotlib.pyplot as plt
import numpy as np

# PV cell data
V = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
I = np.array([5.0, 4.8, 4.5, 4.0, 3.5, 2.5, 0.0])

# Creating the graph
plt.figure(figsize=(8,6))
plt.plot(V, I, 'b-o', linewidth=2, markersize=6)
plt.xlabel('Tension (V)')
plt.ylabel('Courant (A)')
plt.title('Caractéristique I-V')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.35)
plt.ylim(0, 5.5)

# Display
plt.show()
