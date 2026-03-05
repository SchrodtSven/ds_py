# Matplotlib

 The following three methods are central to dataframe workflows used throughout this course:

    df.eval(): Does calculations.
    df.query(): Finds rows.
    df.groupby(): Builds groups of rows.

We'll first explore each core move on its own, then combine them to tackle multistep tasks. 


Activity Goal:
Find the average weight for each group.
1
2
groups['weight'].mean()
banana	124.333
pineapple	850
strawberry	11.4

Series: weight, Length: 3, dtype: number
[8]

This gave us a series object where the index is the fruit.

We can turn the index into a column using reset_index(). This will convert the series into a dataframe.
Activity Goal:
Reset the index for the series.



his entire groupby calculation is often done as a single line of code, like this:
1
2
df.groupby('fruit')['weight'].mean().reset_index()

## Pro Tips

Pro Tip Recap

Let's summarize the three tips for compelling bar charts:

    Pro Tip 1: Use horizontal bar charts.
    Pro Tip 2: Give the bars order.
    Pro Tip 3: Swap ticks and spines for faded grid lines.
 These three Pro Tips for paired scatter plots make it easier to compare the opinions of the public and experts. Here's a recap of all the changes we made:

    Pro Tip 1: Add an equality line.
    Pro Tip 2: Square up the plot.
    Pro Tip 3: Change marker transparency.
    