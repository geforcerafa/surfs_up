# Surf Shop Analysis


Weather analysis using Python, SQLite, SQLAlchemy, Pandas and NumPy.

## Overview of Project


In this project we are analyzing temperature trends in Oahu. The goal is to determine if a surf and ice cream shop business is sustainable year-round in that location, and present the results to an investor, W. Avy. For this we are going to analyze the months of June and December.

### Resources used in this audit
-	Data Sources: hawaii.sqlite
-	Software: Python 3.7.6


## Temperature Analysis Results:

For the analysis we have a good sample of temperatures, 1700 for the month of June, and 1517 for the month of December. The statistical analysis considers measures of central tendency and measures of spread. 

•	The mean for the June temperature was of 74.9 degrees, and the mean for the month of December was of 71.0 degrees. As we can see there was not a big difference in the mean of the temperatures for both months.
•	The standard deviation of the temperature for June was of 3.25 and for December of 3.75. It can be concluded that there are bigger swings of temperature in December, and the temperature ranges for both months are similar.
•	The average minimum temperature for June was of 65 degrees, and for December of 56 degrees. As we could expect there were lower average temperatures in December.
•	The average maximum temperature for June was 85 degrees, and for December of 83 degrees. Slightly higher in June, but very close the two of them.

We can see here the temperature statistical summary for June and December 



![June Temps](https://user-images.githubusercontent.com/96758511/159399429-4f7cf663-0072-4562-bbf0-932ecbee5d52.png)


Statistical Analysis of the June temperatures



![December Temps](https://user-images.githubusercontent.com/96758511/159399462-fd804b13-f425-4943-b9ed-b2e42c0fcb32.png)


Statistical Analysis of the December temperatures


## Temperature Analysis Summary:

From the statistical analysis we can conclude that the mean temperatures for the months of June and December were pretty close for each other, 74.9 degrees for June and 71.0 degrees for December. The standard deviation was 3.25 for June and 3.75 for December. A higher variation in the temperature for December, which was explained for the average minimum temperatures lower in this month of 56 degrees, compared to 65 degrees for June. The average maximum temperatures were very similar, having 85 degrees for the month of June, and 83 degrees for the month of December. 

In the case of the ice cream sales, the temperature ranges are in an adequate range, not too cold in winter and reasonably high in summer. 


Considering other queries for this case: 

•	The analysis can also be made in the precipitation of the rainiest months in Oahu. This could also give us some clues of hurricanes in the region.


•	It would be interesting analyze the weather in the places with the most sells of ice cream, and how they would correlate with the weather in Oahu.
