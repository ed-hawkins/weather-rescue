Readme for Gensan station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Gensan 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 39deg 09'N 127deg 26'E (1907-1909)
            39deg 11'N 127deg 26'E (1910-1941)
  altitude: 2.7m (1907-1912)
            3.5m (1913-1915)
            36.5m (1916-1941)
  time: local time (+9 UTC) 1907-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_GENSAN.xls
  gravity adjustment -0.4 mmHg
 

Data files
  GENSAN_yyyy.xls
    yyyy: year
  CMOJ_sl_GENSAN.xls


Data format
1907-1918
  Month day (local time) 2 6 10 14 18 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1919-1941
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
       