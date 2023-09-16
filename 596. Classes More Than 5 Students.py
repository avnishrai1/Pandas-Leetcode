import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    df = courses.groupby('class', as_index = False).count()

    df = df[df['student'] >= 5]

    return df[['class']]

