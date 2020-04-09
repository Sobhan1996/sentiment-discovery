import os
import pandas as pd


cnn_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/cnn_stories_tokenized'
dm_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/dm_stories_tokenized'
dir_path = cnn_dir_path

sentiment_df = pd.read_csv('./CNN_data/CNN_highlights_sentiments.csv')

i = 0

for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)

    f = open(file_path, "r")
    file_name = os.path.basename(f.name)
    lines = f.readlines()
    highlight_index = lines.index('@highlight\n')
    lines.insert(highlight_index-1, '<|' + sentiment_df.iloc[i, 3] + '|>')

    f = open(file_path, 'w')
    f.writelines(lines)
    f.close()

    if i % 1000 == 0:
        print(i)

    i = i+1