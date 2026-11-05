Readme for Hokoto station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Hokoto 3 to 6 time a day sea level pressure data 1901-1941
 
Station information
  location: 23deg 33'N 119deg 34'E (1901-1906)
            23deg 32'N 119deg 33'E (1907-1941)
  altitude: 17.3m (1901-1898)
            11.0m (1899-1941)
  time: local time (+8 UTC) 1901-1937
                   (+9 UTC) 1938-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_HOKOTO.xls
  gravity adjustment -1.3 mmHg (1910,1916,1922,1932)
                     -1.4 mmHg (1924,1933-1941)
 

Data files
  Hokoto_Pressure1897.xls
  HOKOTO_yyyy.xls
    yyyy: year
  CMOJ_sl_HOKOTO.xls


Data format
1901-1918,1924-1929
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
updated Apr. 22 2015
Hisayuki Kubota 
Department of Coupled Ocean-Atmosphere-Land Processes Research (DCOP)
Japan Agency for Marine-Earth Science and Technology (JAMSTEC)
kubota@jamstec.go.jp 
       