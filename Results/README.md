# Results
The scraped data can be analyzed to yield some interesting results. By applying geolocation to the addresses, attributes such as price per unit area can be mapped (Figure 1).

![Heat map of property price per unit area](/Images/OpenHeatMap_map_only.png)
![Legend](/Results/Images/OpenHeatMap_legend_only.png)  
**Figure 1.** Price per unit area (EUR/m<sup>2</sup>) of houses for sale in Amsterdam on 18 July 2016, plotted using [OpenHeatMap](www.openheatmap.com). (Due to a quotum on of the number of geolocation requests per individual address, geolocation was performed by grouping properties by the first 4 digits of their postal codes and using a downloaded [database of their coordinates](https://github.com/bobdenotter/4pp); this is why the 'blobs' are  unevenly distributed). 

As seen from Figure 1, there is a significant price difference across the Ij river between Amsterdam Centrum and Amsterdam Noord. This may in part be due to the fact that one must take a ferry to cross.

The data can also be visualized in time, and used as a gauge of market sentiment. Figure 2 illustrates the development of (most recent) asking prices and the time it takes for properties to sell.

![Development of the real estate market in Amsterdam](/Images/Amsterdam_property_sales_with_trend_line_big.png)  
**Figure 2.** Asking prices before sale (above) and days the property was offered on Funda (below) for over 11,000 properties in the period 1 April 2015 - 18 July 2016. The blue dots represent individual properties, the red curves weekly averages, and the green curves (weighted) exponential fits of the weekly averages. 

As seen from Figure 2, over the period observed, the house prices increase on average by 15% per year. Despite that, the average time it takes for a property to sell has more than halved. In short, the Amsterdam real estate market is heating up!
