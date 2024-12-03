import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams,font_manager

# Set the font to Times New Roman
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 8

# Data
encoder_layers = [
    0, 5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
]
wer_values = [
    15.84, 16.99,16.55, 16.42, 16.23, 15.87, 16.38, 16.46, 16.85, 18.18, 16.31, 17.47, 16.49, 17.8, 18.18, 
    18.38, 15.93, 18.27, 18.13, 16.16, 19.08, 17.51, 17.72, 17.25, 
    17.70, 19.31, 17.70, 18.96, 18.38
]

# Filter valid data points
valid_layers = [layer for layer, wer in zip(encoder_layers, wer_values) if wer is not None]
valid_wer = [wer for wer in wer_values if wer is not None]

# Plot
plt.figure(figsize=(6, 3))

# # Plot the first dot in red
# plt.scatter(valid_layers[0], valid_wer[0], color="#C8102E", s=20, label="First Point")
# plt.text(valid_layers[0]+0.5, valid_wer[0], f'{valid_wer[0]:.2f}', fontsize=10, ha='left', color="#C8102E",fontweight='bold')

# # Plot the lowest dot in gold
# plt.scatter(valid_layers[10], valid_wer[10], color="#A4804A", s=20, label="lowest Point")
# plt.text(valid_layers[10]+0.2, valid_wer[10]+0.4, f'{valid_wer[10]:.2f}', fontsize=10, ha='left', color="#A4804A",fontweight='bold')
# plt.text(valid_layers[10]+3, valid_wer[10]-0.9, f'Layers 1 to {valid_layers[10]} frozen', fontsize=10, ha='right', color="#A4804A",fontweight='bold')

# # Plot the rest of the dots in black
# other_layers = valid_layers[1:10] + valid_layers[11:]
# other_wer = valid_wer[1:10] + valid_wer[11:]
# plt.scatter(other_layers, other_wer, color="#000000", s=20, label="Other Points")

plt.scatter(valid_layers, valid_wer, color="#000000",s=20, label="")

# plt.title("WER (%) for Different Number of Bottom Layers Frozen", fontsize=16)
plt.xlabel("Number of Layers Frozen", fontsize=12)
plt.ylabel("WER (%)", fontsize=12)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(0, 33, 5)) 
plt.xticks(fontsize=10)
plt.yticks(range(10, 22, 2)) 
plt.yticks(fontsize=10)
# plt.xlim(left=0)  

# Remove upper and right borders
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()