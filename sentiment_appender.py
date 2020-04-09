import numpy as np
import pandas as pd

prob = np.load('./DM_data/clf_results.npy.prob.npy')

df = pd.read_csv('./DM_data/DM_highlights.csv')
ans = [''] * prob.shape[0]
sentiments = ['Anger', 'Anticipation', 'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust']

for i in range(prob.shape[0]):
    ans[i] = sentiments[int(np.argmax(prob[i, :]))]

df['sentiment'] = ans

df.to_csv('./DM_data/DM_highlights_sentiments.csv')