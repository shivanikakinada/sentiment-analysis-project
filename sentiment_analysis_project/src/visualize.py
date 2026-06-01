import matplotlib.pyplot as plt

def sentiment_chart(df):

    counts = df["sentiment"].value_counts()

    fig, ax = plt.subplots()

    counts.plot(kind="bar", ax=ax)

    return fig