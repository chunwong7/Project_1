# Executive Summary for the Analysis of Disaster Relief Efforts Compared to Racial Diversity and Wealth
## Project Workers
* Ryan Klueg
* Frankie Wong
* Evan Kamis
* Mahamat A. Ibrahim Oumar
## Project Topics
1. Does the median household income in a county affect the amount of disaster relief aid recieved by FEMA?
2. Is the disaster relief aid recieved by FEMA by a county affected by the racial and/or ethnic profile of the county?
## Data Sets
1. FEMA APIs 
2. SEPIE Data (XLS)
3. Census Data 
## Task Distribution
* Ryan:
  * Retrieval and clean up of SAPIE data
   * Download the relevant years' XLS datasets and convert to csv for easier handling.
   * Pandas DataFrames to limit data to desired variables
* Frankie: 
  * Obtain money data from FEMA Web Decleration Summaries API specifically the money distributed per disaster
  * Clean the data obtained from FEMA
* Evan:
  * Find API or other Data source for racial makeup of counties
  * Collect data and clean it.
* Mahamat:
  * Obtain data about county relief efforts by disaster from FEMA's Disaster Decleration Summaries V2 API
  * Clean data from FEMA