Readme for Mukden station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Mukden 3 to 6 time a day sea level pressure data 1907-1937
 
Station information
  location: 41deg 48'N 123deg 23'E (1907-1929)
            41deg 46'N 123deg 24'E (1930-1932)
            41deg 47'N 123deg 24'E (1933-1937)
  altitude: 57.5m (1907-1908)
            43.8m (1909-1929)
            44.3m (1930-1937)
  time: local time (+9 UTC) 1907-1912
                   (+8 UTC) 1913-1936
                   (+9 UTC) 1937
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_MUKDEN.xls
  gravity adjustment -0.2 mmHg

 

Data files
  MUKDEN_yyyy.xls
    yyyy: year
  CMOJ_sl_MUKDEN.xls


Data format
1907-1918,1923-1929
  Month day (local time) 2 6 10 14 18 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1919-1922,1930-1937
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
       