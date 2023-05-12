# Written almost entirely by ChatGPT.

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import subprocess
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.widgets import Slider
import mplcursors

lemmatizer = WordNetLemmatizer()

result = subprocess.run(['git', 'log', '--pretty=format:%s'], capture_output=True, text=True)

result2 = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True)

repository_name = result2.stdout.strip().split('/')[-1]

text = re.sub(r'[^\w\s]', '', result.stdout)

words = [lemmatizer.lemmatize(w, wordnet.VERB) for w in word_tokenize(text)]

stop_words = set(stopwords.words('english'))

filtered_words = [w for w in words if w.lower() not in stop_words]

word_counts = Counter(filtered_words)

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

sorted_words_only = [x[0] for x in sorted_words]

with open('sorted_words.txt', 'w') as f:
    f.write(f'The full list of words from the {repository_name} commit messages, sorted from most common.\n\n')
    for word, count in sorted_words:
        if len(word) >= 16:
            f.write(f'{word} - {count} - excluded from graph\n')
        else:
            f.write(f'{word} - {count}\n')

subprocess.run(['xdg-open', 'sorted_words.txt'])
    
df_cache = pd.DataFrame([w for w in sorted_words if len(w[0]) <= 16], columns=['Word', 'Frequency'])

sns.set_style('darkgrid')
plt.style.use('grayscale')

fig, ax = plt.subplots(figsize=(12, 6))

def update(val, ax=ax):
    freq = int(slider_freq.val)
    df = df_cache[:freq]
    ax.clear()
    sns.barplot(x='Word', y='Frequency', data=df, color='#2E86C1', ax=ax)
    ax.set_title(f'Top {freq} Words in {repository_name} Commit Messages', fontweight='bold')
    ax.set_xlabel('Word', fontweight='bold')
    ax.set_ylabel('Frequency', fontweight='bold')
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)
    plt.subplots_adjust(bottom=0.25)

    cursors = []
    for annot in ax.containers:
        mpl_cursor = mplcursors.cursor(annot, hover=True)
        mpl_cursor.connect('add', lambda sel: update_annotation(sel, df_cache))
        cursors.append(mpl_cursor)

    if hasattr(update, "cursors"):
        for cursor in update.cursors:
            cursor.remove()

    update.cursors = cursors

    fig.canvas.draw_idle()


def update_annotation(sel, df):
    if sel.artist is not None and sel.artist.patches is not None and len(sel.artist.patches) > 0:
        index = int(round(sel.target[0]))
        if index < len(df):
            sel.annotation.set_text(f"{df.iloc[index]['Word']}: {sel.target[1]}")

axfreq = plt.axes([0.25, 0.001, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_freq = plt.Slider(axfreq, 'Words', valmin=1, valmax=len(df_cache), valinit=20, valstep=1)

update(20)

slider_freq.on_changed(update)

plt.show()