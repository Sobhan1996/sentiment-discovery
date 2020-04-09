import os
import pandas as pd


cnn_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/cnn_stories_tokenized'
dm_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/dm_stories_tokenized'

i = 0

df = pd.DataFrame({}, columns=['file_name', 'highlight'])

for filename in os.listdir(dm_dir_path):
    file_path = os.path.join(dm_dir_path, filename)

    f = open(file_path, "r")
    file_name = os.path.basename(f.name)
    lines = f.readlines()
    highlight_index = lines.index('@highlight\n')
    highlight = lines[highlight_index+2]
    df.loc[i] = [file_name, highlight]

    i = i+1

# df.to_csv(r'./DM_highlights.csv', index=False, header=True)
