# Analysis Comparing the Federal Relief recieved by Counties Based on Their Household Income
## [Presentation](Comparing Federal Disaster Relief and County Household Income.pptx)
Powerpoint presentation on the analysis of the data collected.
## [SAPIE_Data](SAPIE_DataClean)
Data obtained from the Census's SAPIE survey after cleaning to be used for our analysis.
### [sapie.ipynb](SAPIE_DataClean/sapie.ipynb)
Program created to run through [sapie_data_csv](sapie_data_csv) files and clean the data contained therein and return data in desired format to [SAPIE_DataClean](SAPIE_DataClean) for further use.
### [By State](SAPIE_DataClean/ByState)
Data provided by SAPIE on a state by state level allowing us to view Median Household Income by county in a state.
## [Public Assistance Data](publicAssistanceData)
Data obtained from FEMA's [Public Assistance Funded Projects Summaries - V1](https://www.fema.gov/openfema-dataset-public-assistance-funded-projects-summaries-v1) API and cleaned for use in our analysis.
### [State Data](publicAssistanceData/output_data/state_data)
FEMA API data by state cleaned and used for our analysis.
### [PublicAssistance_clean.ipynb](publicAssistanceData/PublicAssistance_clean.ipynb) & [final_clean_Assistance.ipynb](publicAssistanceData/final_clean_Assistance.ipynb)
Programs written to pull in FEMA data from [Public Assistance Funded Projects Summaries - V1](https://www.fema.gov/openfema-dataset-public-assistance-funded-projects-summaries-v1) API and clean it for use in our analysis. The final clean program provides some extra cleaning for a greater ease of use.
## [Combined FEMA Data](FEMA_combineClean.ipynb)
Program used to create the [by county and disaster](byDisasterandCounty.csv) file of the FEMA data from [Public Assistance Funded Projects Summaries - V1](https://www.fema.gov/openfema-dataset-public-assistance-funded-projects-summaries-v1) API for use in analysis.
### [By Disaster and County Data](byDisasterandCounty.csv)
FEMA data grouped by disaster and county.
## [Analysis](SAPIE_analysis.ipynb)
Program used to run a statistical analysis for the comparison of FEMA relief money versus the median household income in counties.
## [Plots](plots)
Folder containing various plots created from our analysis of the data.
## Built With
* Jupyter Notebook
* Python
* [Public Assistance Funded Projects Summaries - V1 API](https://www.fema.gov/openfema-dataset-public-assistance-funded-projects-summaries-v1)
* [SAPIE State & County Estimates for 2018](https://www.census.gov/data/datasets/2018/demo/saipe/2018-state-and-county.html)
## Authors
* Ryan Klueg
* Evan Kamis
* Mahamat A. Ibrahim Oumar
* Chun (Frankie) Wong
