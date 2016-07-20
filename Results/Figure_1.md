# Mapping of real estate attributes
The scraped data can be analyzed to yield some interesting results. By applying geolocation to the addresses, attributes such as price per unit area can be mapped (Figure 1).

![Heat map of property price per unit area](/Results/Images/OpenHeatMap_map_only.png)
![Legend](/Results/Images/OpenHeatMap_legend_only.png)  
**Figure 1.** Price per unit area (EUR/m<sup>2</sup>) of houses for sale in Amsterdam on 18 July 2016, plotted using [OpenHeatMap](www.openheatmap.com). (Due to a quotum on of the number of geolocation requests per individual address, geolocation was performed by grouping properties by the first 4 digits of their postal codes and using a downloaded [database of their coordinates](https://github.com/bobdenotter/4pp); this is why the 'blobs' are  unevenly distributed). 

As seen from Figure 1, there is a significant price difference across the Ij river between Amsterdam Centrum and Amsterdam Noord. This may in part be due to the fact that one must take a ferry to cross.
