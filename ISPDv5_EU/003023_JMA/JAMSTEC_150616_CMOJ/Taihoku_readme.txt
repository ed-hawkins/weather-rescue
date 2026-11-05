Readme for Taihoku station data
---------------------------------------------------------------------------------------------

Data source 
Monthly Report of the Central Meteorological Observatory Tokyo Japan 

Datasets
  Taihoku 3 to 24 time a day sea level pressure data 1901-1941
 
Station information
  location: 25deg 04'N 121deg 28'E (1901-1902)
            25deg 02'N 121deg 30'E (1903-1906)
            25deg 02'N 121deg 31'E (1907-1941)
  altitude: 7.6m (1897)
            9.3m (1898-1941)
  time: local time (+8 UTC) 1897-1937
                   (+9 UTC) 1938-1941
  unit: +700 mmHg
  altitude adjustment  data are station pressure 
                       for sea level adjustment see CMOJ_sl_TAIHOKU.xls
  gravity adjustment -1.27 mmHg (1910)
                     -1.28 mmHg (1914)
                     -1.24 mmHg (1922)
                     -1.25 mmHg (1926)
                     -1.26 mmHg (1927)
                     -1.27 mmHg (1930)
                     -1.26 mmHg (1931-1932)
                     -1.28 mmHg (1933)


Data files
  TAIHOKU_yyyy.xls
    yyyy: year(1901-1932,1934-1941)
  TAIHOKU_193301-10.xls
  TAIHOKU_193311-12.xls
  CMOJ_sl_TAIHOKU.xls


Data format
1901-1932,193301-10
  Month day (local time) 1 2 Åc 23 24
  1     1
  1     2
  .
  .
  12   30
  12   31


193311-12,1934-1941
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
       