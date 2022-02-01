Reykjavík pressure data 1820 to 1854
Column headings:

    RVK_PJONTH2054

        INDEX INTEGER NOT NULL, index
        AR SMALLINT NOT NULL, year
        MAN SMALLINT NOT NULL, mon
        DAGUR SMALLINT NOT NULL,  day
        KLST SMALLINT NOT NULL, hr
        P_FRANSK INTEGER DEFAULT NULL, presure as read in french inches and paris lines
        P_AFLES DECIMAL(6,1) DEFAULT NULL, p - converted to hPa
        P_LEIDR DECIMAL(6,1) DEFAULT NULL, p - "obvious errors" corrected
        P_TLEIDR DECIMAL(6,1) DEFAULT NULL, p - corrected - to 0° 
        P_GLEIDR DECIMAL(6,1) DEFAULT NULL, p - corrected to 45°N
        P DECIMAL(6,1) DEFAULT NULL, p - to s.l. 
        TB_C DECIMAL(5,1) DEFAULT NULL, instrument temperature
        INSTRUMENT SMALLINT DEFAULT NULL, instrument id
