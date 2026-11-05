Readme for Tairen station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Tairen 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 38deg 56'N 121deg 36'E (1907-1917)
            38deg 54'N 121deg 36'E (1918-1925)
            38deg 54'N 121deg 38'E (1926-1941)
  altitude: 15.4m (1907)
            13.8m (1908-1917)
            97.3m (1918-1941)
  time: local time (+9 UTC) 1907-1912
                   (+8 UTC) 1913-1936
                   (+9 UTC) 1937-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_TAIREN.xls
  gravity adjustment -0.4 mmHg

 

Data files
  TAIREN_yyyy.xls
    yyyy: year
  CMOJ_sl_TAIREN.xls


Data format
1907-1918,1923-1929
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
       