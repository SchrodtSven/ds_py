# Pandas

Merge the data

There are multiple ways to combine dataframes. When bringing together columns, we suggest using a
.

The merge() method allows you to specify the column to align on. In this case, we want to align on the 'year' column.

This left merge will start with all years in the left dataframe, and ignore any extra years from the right dataFrame. This is useful here because we are not interested in all the years before 1990. Especially not all the way back to 10,000 BCE! 