Readme for Siska station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Siska 3 to 6 time a day sea level pressure data 1908-1941
 
Station information
  location: 49deg 14'N 143deg 11'E (1908-1911)
            49deg 14'N 143deg 07'E (1912-1937)
            49deg 13'N 143deg 06'E (1938-1941)
  altitude: 3.0m (1908)
            3.5m (1909-1941)
  time: local time (+9 UTC) 1908-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_SISKA.xls
  gravity adjustment +0.3 mmHg

 

Data files
  SISKA_yyyy.xls
    yyyy: year
  CMOJ_sl_SISKA.xls


Data format
1908-1918,1924-1929
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
       