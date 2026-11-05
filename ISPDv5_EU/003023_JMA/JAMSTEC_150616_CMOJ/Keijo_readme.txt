Readme for Keijo station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Keijo 3 to 6 time a day sea level pressure data 1908-1941
 
Station information
  location: 37deg 34'N 126deg 55'E (1908-1909)
            37deg 34'N 126deg 58'E (1910-1914 1933-1941)
            37deg 34'N 126deg 59'E (1915-1932)
  altitude: 39.0m (1908-1912)
            32.3m (1913-1923)
            29.5m (1924-1932)
            87.0m (1933-1941)
  time: local time (+9 UTC) 1908-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_KEIJO.xls
  gravity adjustment -0.5 mmHg

 

Data files
  KEIJO_yyyy.xls
    yyyy: year
  CMOJ_sl_KEIJO.xls


Data format
1908,1919-1923,1930-1941
  Month day (local time) 6 14 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1909-1918,1924-1929
  Month day (local time) 2 6 10 14 18 22
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
       