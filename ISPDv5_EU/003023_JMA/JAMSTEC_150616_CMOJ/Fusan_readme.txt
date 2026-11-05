Readme for Fusan station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Fusan 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 35deg 06'N 129deg 03'E (1907-1909)
　　　　　　35deg 07'N 129deg 05'E (1910-1917)
            35deg 06'N 129deg 01'E (1918-1933)
            35deg 06'N 129deg 02'E (1934-1941)
  altitude: 14.9m (1907-1920)
            12.5m (1921-1933)
            70.5m (1934-1941)
  time: local time (+9 UTC) 1907-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_FUSAN.xls
  gravity adjustment -0.7 mmHg


Data files
  FUSAN_yyyy.xls
    yyyy: year
  CMOJ_sl_FUSAN.xls


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
       