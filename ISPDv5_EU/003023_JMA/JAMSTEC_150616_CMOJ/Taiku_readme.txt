Readme for Taiku station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Taiku 3 to 6 time a day sea level pressure data 1908-1941
 
Station information
  location: 35deg 50'N 128deg 36'E (1908-1914)
            35deg 52'N 128deg 35'E (1915-1929 1931)
            35deg 52'N 128deg 36'E (1930 1932-1936)
            35deg 53'N 128deg 37'E (1937-1941)
  altitude: 39.4m (1908-1914)
            42.2m (1915)
            52.4m (1916-1928)
            53.4m (1929-1936)
            60.9m (1937-1941)
  time: local time (+9 UTC) 1908-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_TAIKU.xls
  gravity adjustment -0.6 mmHg

 

Data files
  TAIKU_yyyy.xls
    yyyy: year
  CMOJ_sl_TAIKU.xls


Data format
1908,1919-1923,1930-1941
  Month day (local time) 6 14 22
  1     1
  1     2
  .
  .
  12   30
  12   31


1909-1918,1924-1929
  Month day (local time) 2 6 10 14 18 22
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
       