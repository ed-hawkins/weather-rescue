Readme for Shana station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Shana 3 to 6 time a day sea level pressure data 1902-1941
 
Station information
  location: 45deg 14'N 147deg 51'E (1903-1906)
            45deg 14'N 147deg 53'E (1907-1941)
  altitude: 39.3m (1903-1915 1934-1941)
            38.2m (1916-1933)
  time: local time (+9 UTC) 1902-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_SHANA.xls
  gravity adjustment +0.0 mmHg

 

Data files
  SHANA_yyyy.xls
    yyyy: year
  CMOJ_sl_SHANA.xls


Data format
1902-1918,1923-1929
  Month day (local time) 2 6 10 14 18 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1919-1922,1930-1941
  Month day (local time) 6 14 22
  1     1
  1     2
  .
  .
  12   30
  12   31



Data Policy
   This dataset is available for research only and not allowed to provide it to third party. 
   
----------------------------------------------------------------
May 29 2014
Hisayuki Kubota 
Department of Coupled Ocean-Atmosphere-Land Processes Research (DCOP)
Japan Agency for Marine-Earth Science and Technology (JAMSTEC)
kubota@jamstec.go.jp 
       