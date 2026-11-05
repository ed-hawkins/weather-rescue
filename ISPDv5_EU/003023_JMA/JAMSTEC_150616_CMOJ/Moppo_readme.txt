Readme for Moppo station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Moppo 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 34deg 47'N 126deg 22'E (1907-1909)
            34deg 47'N 126deg 20'E (1910-1928)
            34deg 47'N 126deg 23'E (1929-1941)
  altitude: 28.2m (1907-1928)
            32.5m (1929-1941)
  time: local time (+9 UTC) 1907-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_MOPPO.xls
  gravity adjustment -0.7 mmHg

 

Data files
  MOPPO_yyyy.xls
    yyyy: year
  CMOJ_sl_MOPPO.xls


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
       