Readme for Jinsen station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Jinsen 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 37deg 29'N 126deg 32'E (1907-1913)
            37deg 29'N 126deg 37'E (1914-1927)
            37deg 29'N 126deg 38'E (1928-1941)
  altitude: 70.0m (1907-1909)
            67.0m (1910)
            67.6m (1911-1928)
            70.4m (1929-1941)
  time: local time (+9 UTC) 1907-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_JINSEN.xls
  gravity adjustment -0.5 mmHg

 

Data files
  JINSEN_yyyy.xls
    yyyy: year
  CMOJ_sl_JINSEN.xls


Data format
1907-1918,1924-1929
  Month day (local time) 2 6 10 14 18 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1919-1923,1930-1941
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
       