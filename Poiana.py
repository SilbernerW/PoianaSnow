import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta

# --- 1. Generate Synthetic Data ---
# Since specific daily historical snow data for Poiana Brasov over 5 years is not easily accessible online,
# we will simulate a dataset for demonstration purposes.
# Replace this section with your actual data when you have it.

def generate_synthetic_data():
    """Generates synthetic snow depth data for 5 winter seasons."""
    base_year = 2021
    num_years = 5
    start_month = 12  # Winter starts in December
    end_month = 4     # Winter ends in April

    all_data = []

    for year in range(num_years):
        current_year = base_year + year
        # Simulate snow season from Dec to April of the next year
        dates = pd.date_range(start=f'{current_year}-{start_month}-01', end=f'{current_year+1}-{end_month}-30')
        season_label = f"Winter {current_year}-{current_year+1}"

        # Simulate a realistic-looking snow depth pattern for a season
        snow_depths = []
        for i, d in enumerate(dates):
            # A simple sinusoidal curve to simulate accumulation and melting
            peak_day = dates.size // 2
            amplitude = np.random.uniform(70, 100)  # Peak snow depth between 70-100 cm
            offset = amplitude * 0.5  # Ensure values stay positive
            snow = amplitude * np.sin(np.pi * i / dates.size) + offset
            snow_depths.append(max(0, snow + np.random.uniform(-10, 10))) # Add some random noise

        # Store the synthetic data for this season
        df = pd.DataFrame({'Date': dates, 'Snow_Depth_cm': snow_depths, 'Season': season_label})
        all_data.append(df)
    
    return pd.concat(all_data).reset_index(drop=True)

# Generate the data
df = generate_synthetic_data()

# --- 2. Visualize the Data ---
plt.style.use('ggplot')  # Use a nice-looking plot style

# Create the plot
plt.figure(figsize=(15, 8))

# Get the unique seasons to plot each one separately
seasons = df['Season'].unique()

# Define a color palette for the different seasons
colors = plt.cm.viridis(np.linspace(0, 1, len(seasons)))

# Plot each season's data
for i, season in enumerate(seasons):
    season_data = df[df['Season'] == season]
    plt.plot(season_data['Date'], season_data['Snow_Depth_cm'], label=season, color=colors[i], lw=2)

# --- 3. Customize the Graph ---
plt.title('Simulated Historical Snow Depth for Poiana Brașov (5 Years)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Snow Depth (cm)', fontsize=12)
plt.legend(title='Winter Season', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust layout to make room for the legend
plt.xticks(rotation=45) # Rotate x-axis labels for better readability

# Add annotations for typical peak season conditions
plt.text(pd.to_datetime('2023-01-15'), 120, 'Typical Peak Season', 
         fontsize=10, color='darkgreen', ha='center',
         bbox=dict(boxstyle='round,pad=0.3', fc='lightgreen', alpha=0.5))

# Display the plot
plt.show()
