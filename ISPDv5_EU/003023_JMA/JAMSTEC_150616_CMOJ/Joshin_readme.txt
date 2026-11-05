Readme for Joshin station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Joshin 3 to 6 time a day sea level pressure data 1907-1941
 
Station information
  location: 40deg 40'N 129deg 11'E (1907-1928)
            40deg 40'N 129deg 12'E (1929-1941)
  altitude: 4.0m (1907-1919)
            31.9m (1920-1941)
  time: local time (+9 UTC) 1907-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_JOSHIN.xls
  gravity adjustment -0.3 mmHg

 

Data files
  JOSHIN_yyyy.xls
    yyyy: year
  CMOJ_sl_JOSHIN.xls


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
       