import os
import pandas as pd


cnn_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/cnn_stories_tokenized'
dm_dir_path = os.path.dirname(os.path.realpath(__file__)) + '/CNN_DM_dataset/dm_stories_tokenized'
dir_path = cnn_dir_path

sentiment_df = pd.read_csv('./CNN_data/CNN_highlights_sentiments.csv')
# sentiment_df = pd.read_csv('./DM_data/DM_highlights_sentiments.csv')

i = 0

for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)

    if i >= sentiment_df.shape[0]:
        os.remove(file_path)
    else:
        f = open(file_path, "r")
        file_name = os.path.basename(f.name)
        lines = f.readlines()
        highlight_index = lines.index('@highlight\n')
        lines.insert(highlight_index-1, '<|' + sentiment_df.iloc[i, 3] + '|>')

        highlight_indices = [i for i, line in enumerate(lines) if line == '@highlight\n']
        highlight_indices = highlight_indices + [i+1 for i, line in enumerate(lines) if line == '@highlight\n']

        for index in sorted(highlight_indices, reverse=True):
            del lines[index]

        # f = open('./example.txt', 'w')
        # f.writelines(lines)
        # f.close()
        # f = open('./example.txt', 'r')
        # print(f.read())

        f = open(file_path, 'w')
        f.writelines(lines)
        f.close()

    if i % 1000 == 0:
        print(i)

    i = i+1