import pandas as pd
import matplotlib.pyplot as plt

# Data for the actuals number from the open report
data = {
    "Region": [
        "USA", "UK", "Australia", "Canada", "Ireland", "New Zealand",
        "China", "Asia", "Hong Kong", "Middle East", "Pacific",
        "Europe", "Australia Other", "New Zealand Other"
    ],
    "Actuals": [
        1150641, 821926, 402171, 332616, 121476, 111003,
        46019, 34884, 20497, 16262, 5294,
        4284, 597, 1000
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort by Actuals descending for better visualization
df = df.sort_values(by="Actuals", ascending=False)

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))
plt.barh(df["Region"], df["Actuals"], color='skyblue')
plt.xlabel('Actuals Number')
plt.title('Actuals Number by Region')
plt.gca().invert_yaxis()  # Highest values on top
plt.tight_layout()

# Save the plot as an image file
plt.savefig("actuals_report.png")

# Display the plot
plt.show()