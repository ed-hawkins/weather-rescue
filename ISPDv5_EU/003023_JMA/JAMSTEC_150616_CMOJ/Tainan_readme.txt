Readme for Tainan station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Tainan 3 to 6 time a day sea level pressure data 1901-1941
 
Station information
  location: 22deg 59'N 120deg 12'E (1901-1916)
            23deg 00'N 120deg 12'E (1917-1921)
            23deg 00'N 120deg 13'E (1922-1941)
  altitude: 11.4m (1897-1898)
            14.3m (1899-1941)
  time: local time (+8 UTC) 1897-1937
                   (+9 UTC) 1938-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_TAINAN.xls
  gravity adjustment -1.4 mmHg

 

Data files
  TAINAN_yyyy.xls
    yyyy: year
  CMOJ_sl_TAINAN.xls


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
Hisayuki Kubota 
Department of Coupled Ocean-Atmosphere-Land Processes Research (DCOP)
Japan Agency for Marine-Earth Science and Technology (JAMSTEC)
kubota@jamstec.go.jp 
       