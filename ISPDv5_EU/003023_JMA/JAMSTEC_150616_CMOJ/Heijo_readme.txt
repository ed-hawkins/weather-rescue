Readme for Heijo station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Heijo 3 to 6 time a day sea level pressure data 1908-1941
 
Station information
  location: 39deg 01'N 125deg 41'E (1908-1928)
            39deg 02'N 125deg 45'E (1929-1941)
  altitude: 30.0m (1908-1912)
            48.0m (1913-1925)
            56.6m (1926-1941)
  time: local time (+9 UTC) 1908-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_HEIJO.xls
  gravity adjustment -0.4 mmHg

 

Data files
  HEIJO_yyyy.xls
    yyyy: year
  CMOJ_sl_HEIJO.xls


Data format
1908, 1919-1923,1930-1941
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
       