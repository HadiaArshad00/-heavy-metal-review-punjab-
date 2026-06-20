# Citation Analysis Script
# For Hadia Arshad's Review Paper on Heavy Metal Contamination

import pandas as pd
import matplotlib.pyplot as plt

# Nanomaterial comparison data from the review paper
nanomaterials = {
    'Material': ['ZVINPs', 'Fe3O4 NPs', 'TiO2', 'GO', 'CNTs', 'MOFs', 'LDHs', 'NF Membranes'],
    'Max_Capacity_mg_g': [125, 300, 90, 600, 250, 550, 300, 90],  # midpoint of ranges
    'Efficiency_Percent': [85, 92, 75, 95, 88, 96, 90, 93]
}

df = pd.DataFrame(nanomaterials)

# Save to CSV
df.to_csv('data/nanomaterial_comparison.csv', index=False)

print("Nanomaterial data saved successfully.")
print("\nSummary:")
print(df)
