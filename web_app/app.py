from flask import Flask, render_template
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# load the pickled model
with open('../data/X.pkl', 'rb') as f:
    X = pickle.load(f)

# load the df
all_df = pd.read_pickle('../data/df.pkl')


def get_trail_recommendations(trail_name, X, n=5):
    index = all_df.index[(all_df['id'] == trail_name)][0]
    trail = X[index].reshape(1,-1)
    cs = cosine_similarity(trail, X)
    rec_index = np.argsort(cs)[0][::-1][1:]
    ordered_df = all_df.loc[rec_index]
    rec_df = ordered_df.head(n)
    orig_row = all_df.loc[[index]].rename(lambda x: 'original')
    total = pd.concat((orig_row,rec_df))
    return total

# home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_trail', methods=['GET','POST'])
def trails():
    return render_template('select_trail.html',df=all_df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8105, threaded=True)