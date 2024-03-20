import pandas as pd
import pytest

df = pd.read_csv(r"C:\Users\StanleyChan\SynologyDrive\Work Backup\my document\Test\test-repo-to-git\pipeline\test1.csv")

def shape(df):
    return df.shape[0]
