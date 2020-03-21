# Analysis Comparing the Federal Relief recieved by Counties Based on Their Household Income
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
