```markdown
# Data Visualization of India

## Overview
This is an interactive Streamlit dashboard for visualizing demographic data across Indian states and districts using geographic scatter plots. It allows users to select states, primary and secondary parameters (e.g., population metrics), and generate map-based visualizations.

## Features
- Select a specific state or view all states.
- Choose primary parameter for bubble size and secondary for color.
- Hover over points to see district names.
- Built with Plotly for interactive maps and Streamlit for the UI.

## Requirements
- Python 3.8+
- Libraries: `streamlit`, `pandas`, `plotly`, `numpy`

Install via:
```
pip install -r requirements.txt
```

## Setup & Run
1. Ensure `India.csv` is in the project directory (contains columns like State, District, Latitude, Longitude, and demographic metrics).
2. Run the app:
   ```
   streamlit run app.py
   ```
3. Open the provided URL in your browser to interact with the dashboard.

## Usage
- Use the sidebar to select state, parameters, and click "Plot Graph".
- Zoom and pan on the map for details.

## Data Source
Demographic data for Indian districts (CSV format). Update `India.csv` for new data.

## License
MIT License - feel free to use and modify.
```