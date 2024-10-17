import pandas as pd
import os
from sklearn.model_selection import train_test_split

#Split the dataset into training (80%), validation (10%), and test (10%) sets 
# Ensure that no speaker appears in more than one split by grouping data by 'name_unique_speaker'
# The splits are done based on the unique speakers within each WAB_AQ_category

# pre: Check if the output file already exists and delete it if it does
output_path = '../data_processed/dataset_splitted.csv'
if os.path.exists(output_path):
    os.remove(output_path)

# Step 1: Load the dataset
data_path = 'final_clean_dataset.csv'
df = pd.read_csv(data_path)

# Step 2: Initialize an empty 'split' column
df['split'] = None

# Step 3: Perform data splitting by speaker and category
categories = df['WAB_AQ_category'].unique()

for category in categories:
    category_data = df[df['WAB_AQ_category'] == category]

    # Group data by speaker to ensure speaker consistency in the splits
    grouped_by_speaker = category_data.groupby('name_unique_speaker')

    speakers = list(grouped_by_speaker.groups.keys())
    speakers = pd.Series(speakers).sample(frac=1, random_state=42).tolist()  # Shuffle speakers

    # Calculate the split indices
    n = len(speakers)
    train_end = int(0.8 * n)
    val_end = train_end + int(0.1 * n)

    # Assign speakers to splits
    train_speakers = speakers[:train_end]
    val_speakers = speakers[train_end:val_end]
    test_speakers = speakers[val_end:]

    # Mark the split for each row based on the speaker
    df.loc[df['name_unique_speaker'].isin(train_speakers), 'split'] = 'train'
    df.loc[df['name_unique_speaker'].isin(val_speakers), 'split'] = 'validation'
    df.loc[df['name_unique_speaker'].isin(test_speakers), 'split'] = 'test'

# Step 4: Save the updated DataFrame to a new CSV file
output_path = '../data_processed/dataset_splitted.csv'
df.to_csv(output_path, index=False)

print(f"Data splitting completed and saved to '{output_path}'!")


# Step 5:  Verification of the splits
train_speakers = set(df[df['split'] == 'train']['name_unique_speaker'])
val_speakers = set(df[df['split'] == 'validation']['name_unique_speaker'])
test_speakers = set(df[df['split'] == 'test']['name_unique_speaker'])

# Check for intersection (should be empty sets)
assert train_speakers.isdisjoint(val_speakers), "Error: Some speakers are in both Train and Validation!"
assert train_speakers.isdisjoint(test_speakers), "Error: Some speakers are in both Train and Test!"
assert val_speakers.isdisjoint(test_speakers), "Error: Some speakers are in both Validation and Test!"

print("Speaker uniqueness check passed!")