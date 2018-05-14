import pandas as pd
import quandl
import pickle
import os


FNAME = 'googl.bin'


def save_pickle():
    try:
        with open(FNAME, 'wb') as f:
            df = quandl.get('WIKI/GOOGL')

            pickle.dump(df, f)
    except Exception:
        os.remove(FNAME)


def load_pickle():
    with open(FNAME, 'rb') as f:
        return pickle.load(f)


if not os.path.exists(FNAME):
    save_pickle()


df = load_pickle()


print(df.head())
