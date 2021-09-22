#!/usr/bin/env python

# Convert the digitised data from Rob's Emulate files to the format
#  Ed Hawkins is using.

import os
import os.path
import pandas
import numpy
import datetime
import calendar
import sys
import re

# Get script directory
sd=os.path.dirname(os.path.abspath(__file__))

# Load the Station names and locations
md=pandas.read_csv("%s/../../Lisa_storms/metadata/names.csv" % sd,
                   header=None)

# Get station name from file name
def get_station_name(file_name):
    sn=os.path.basename(file_name).split('.')
    if sn[0]=='DWR_stations':
        return sn[1].upper()
    return sn[0].upper()

# The old Emulate data is in several different formats.
# These files are in one-ob-per-day format
Files_opd=(
    'Alexandria.Alexandria.csv',
    'DWR_stations.Aberdeen.csv',
    'DWR_stations.Algiers.csv',
    'DWR_stations.Angra.csv',
    'DWR_stations.Biskra.csv',
    'DWR_stations.Brest.csv',
    'DWR_stations.Funchal.csv',
    'DWR_stations.Galway.csv',
    'DWR_stations.Greencastle.csv',    # Changes to TPD in 1868
    'DWR_stations.Holyhead.csv',
    'DWR_stations.La Coruna.csv',
    'DWR_stations.Liverpool.csv',
    'DWR_stations.Mogador.csv',
    'DWR_stations.Nairn.csv',         # Changes from TPD in 1871
    'DWR_stations.Pembroke.csv',
    'DWR_stations.Plymouth.csv',
    'DWR_stations.Portsmouth.csv',
    'DWR_stations.Rochefort.csv',      # Changes to TPD in 1871
    'DWR_stations.Roches Pt.csv',
    'DWR_stations.Scilly Islands.csv',
    'DWR_stations.Toulon.csv',
    'DWR_stations.Valentia.csv',
    'Lesina_Split.Sheet1.csv',
    'Lisbon.Lisbon.csv',
    'Lyons.Lyons.csv',
    'Rome.Rome.csv',
    'Sibiu.Funchal.csv',
    'Stornaway.Stornaway.csv',
)
# These files are in two-ob-per-day format
Files_tpd=(
    'DWR_stations.Nairn.csv',          # Changes to OPD in 1871
    'DWR_stations.Penzance.csv',
    'DWR_stations.Scarborough.csv',
    'DWR_stations.Greencastle.csv',    # Changes from OPD in 1868
    'DWR_stations.Rochefort.csv',      # Changes from OPD in 1871
)

def load_from_file_opd(file_name):
    station=get_station_name(file_name)
    csv=pandas.read_csv(file_name,header=None)

    Hours={
        'Lyons':      9,
        'Alexandria': 9,
        'Sibu':       8,
        'Stornoway':  9,
        'Brest':      8, # Change to 18 previous day on 1875-04-01
        'Rochefort':  8,
        'Mogador':    7,
        'Biskra':     7,
    }    

    # Hour (gmt) of the daily ob.
    def obs_hour(station,year,month):
        if station=='Brest':
            if year>1875 or (year==1875 and month>3):
                return -6
        return Hours.get(station,8)

    # Find the index numbers starting the data for a year
    #  (Lines with 'January' in the second column)
    def find_year_starts(tab):
        return tab[tab.iloc[:,1].str.contains('January',na=False)].index.values

    # Extract a year's worth of data given the start location
    def get_data_for_year(station,tab,istart):
        dates=[]
        pressures=[]
        year=int(tab.iloc[istart,0])
        for month in range(1,13):
            hour=obs_hour(station,year,month)
            lastday=calendar.monthrange(year,month)[1]
            for day in range(1,lastday+1):
                pre=tab.iloc[istart+day+1,month]
                try:
                    pre=float(pre)
                    if numpy.isnan(pre): continue
                    if pre<0: continue         # -9999 - missing
                    if pre<35: pre=pre*33.8639 # InHg
                    if pre<800: pre=pre*1.33   # mmHg
                except ValueError:
                    continue
                dates.append(datetime.datetime(year,month,day,0)+
                             datetime.timedelta(hours=hour))
                pressures.append(pre)
        return {'dates':dates,'pressures':pressures}

    year_i=find_year_starts(csv)
    file_data={}
    for idx in year_i:
         year=int(csv.iloc[idx,0])
         file_data["%04d" % year]=get_data_for_year(station,csv,idx)
    return file_data

def load_from_file_tpd(file_name):
    station=get_station_name(file_name)
    csv=pandas.read_csv(file_name,header=None)

    # Find the index numbers starting the data for a year
    #  (Lines with 'January' in the third column)
    def find_year_starts(tab):
        return tab[tab.iloc[:,2].str.contains('January',na=False)].index.values

    # Convert '2pm' into 14'
    def hour_from_string(hrst):
        try:
            hour=int(re.findall('[0-9]+', hrst)[0])
        except IndexError:
            return None
        if len(re.findall('pm', hrst.lower())) !=0:
            hour=hour+12
        if hour==24: hour=12
        return hour


    # Extract a year's worth of data given the start location
    def get_data_for_year(station,tab,istart):
        dates=[]
        pressures=[]
        year=int(tab.iloc[istart,0])
        for month in range(1,13):
            lastday=calendar.monthrange(year,month)[1]
            for day in range(1,lastday+1):
                for hri in (0,1):
                    if hri==0:
                        pre=tab.iloc[istart+day*2,month+1]
                    else:
                        pre=tab.iloc[istart+day*2+1,month+1]
                    try:
                        pre=float(pre)
                        if numpy.isnan(pre): continue
                        if pre<0: continue         # -9999 - missing
                        if pre<35: pre=pre*33.8639 # InHg
                        if pre<800: pre=pre*1.33   # mmHg
                    except ValueError:
                        continue
                    if hri==0:
                        hour=hour_from_string(tab.iloc[istart+day*2,1])
                        if hour is None: continue
                        dates.append(datetime.datetime(year,month,day,hour))
                    else:
                        hour=hour_from_string(tab.iloc[istart+day*2+1,1])
                        if hour is None: continue
                        dates.append(datetime.datetime(year,month,day,hour))
                    pressures.append(pre)
        return {'dates':dates,'pressures':pressures}
    
    year_i=find_year_starts(csv)
    file_data={}
    for idx in year_i:
         year=int(csv.iloc[idx,0])
         file_data["%04d" % year]=get_data_for_year(station,csv,idx)
    return file_data

# Specific functions for custom formats
def load_from_file_teneriffe(file_name):
    csv=pandas.read_csv(file_name,header=None)
    file_data={}
    dc=csv[csv.iloc[:,0].str.contains('\d\d\d\d',na=False,regex=True)].index.values
    for idx in dc:
        try:
            year   = int(csv.iloc[idx,0])
            month  = int(csv.iloc[idx,1])
            day    = int(csv.iloc[idx,2])
            hour   = int(csv.iloc[idx,3])
            minute = int(csv.iloc[idx,4])
        except ValueError: continue # Missing date
        try:
            pre=float(csv.iloc[idx,5])
            if numpy.isnan(pre): continue
            if pre<0: continue         # -9999 - missing
            if pre<35: pre=pre*33.8639 # InHg
            if pre<800: pre=pre*1.33   # mmHg
        except ValueError: continue # Missing pressure
        if "%04d" % year not in file_data:
            file_data["%04d" % year]={}
        if 'dates' not in file_data["%04d" % year]:
            file_data["%04d" % year]['dates']=[]
            file_data["%04d" % year]['pressures']=[]
        file_data["%04d" % year]['dates'].append(
                   datetime.datetime(year,month,day,hour))
        file_data["%04d" % year]['pressures'].append(pre)
    return file_data

def load_from_file_middle_east(file_name,column):
    csv=pandas.read_csv(file_name,header=None)
    file_data={}
    dc=csv[csv.iloc[:,0].str.contains('\d\d\d\d',na=False,regex=True)].index.values
    for idx in dc:
        try:
            year   = int(csv.iloc[idx,0])
            month  = int(csv.iloc[idx,1])
            day    = int(csv.iloc[idx,2])
            hour   = 8
            minute = 0
        except ValueError: continue # Missing date
        try:
            pre=float(csv.iloc[idx,column])
            if numpy.isnan(pre): continue
            if pre<0: continue         # -9999 - missing
            if pre<35: pre=pre*33.8639 # InHg
            if pre<800: pre=pre*1.33   # mmHg
        except ValueError: continue # Missing pressure
        if "%04d" % year not in file_data:
            file_data["%04d" % year]={}
        if 'dates' not in file_data["%04d" % year]:
            file_data["%04d" % year]['dates']=[]
            file_data["%04d" % year]['pressures']=[]
        file_data["%04d" % year]['dates'].append(
                   datetime.datetime(year,month,day,hour))
        file_data["%04d" % year]['pressures'].append(pre)
    return file_data

# Add a station's data to the output files
def output_station(name,sdata):
    LastF=''
    Of=None
    opfile=None
    mdl=md[md.iloc[:,0].str.lower()==name.lower()]
    if mdl.empty:
        raise Exception("No station %s in metadata" % 
                                                      name)
    for syr in list(sdata.keys()):
        for idx in range(len(sdata[syr]['dates'])):
            Of=("%s/../../data_from_Emulate/%04d/%02d/prmsl.txt" %
                             (sd,sdata[syr]['dates'][idx].year,
                                 sdata[syr]['dates'][idx].month))
            if Of!=LastF:
                dn=os.path.dirname(Of)
                if not os.path.isdir(dn):
                    os.makedirs(dn)
                if opfile is not None:
                    opfile.close()
                    if os.path.getsize(LastF)==0:
                        os.remove(Of)
                        dn=os.path.dirname(LastF)
                        if not os.listdir(dn):
                            os.rmdir(dn)
                opfile=open(Of, "a")
                LastF=Of

            opfile.write(("%04d %02d %02d %02d %02d %6.2f "+
                          "%7.2f %6.1f %16s\n") %
                         (sdata[syr]['dates'][idx].year,
                          sdata[syr]['dates'][idx].month,
                          sdata[syr]['dates'][idx].day,
                          sdata[syr]['dates'][idx].hour,
                          sdata[syr]['dates'][idx].minute,
                          mdl.iloc[0,2],mdl.iloc[0,3], #latlon
                          sdata[syr]['pressures'][idx],     # ob value
                          mdl.iloc[0,1]))              # name

    if opfile is not None:
        opfile.close()
     

# Load all the data
emulate_data={}
Files=os.listdir("%s/../original_data_csv" % sd)
if True:
    for file_name in Files:
        station_name=get_station_name(file_name)

        # Once-per-day data
        if file_name in Files_opd:
            print(station_name)
            if station_name not in emulate_data:
                emulate_data[station_name]={}
            emulate_data[station_name].update(load_from_file_opd(
                         "%s/../original_data_csv/%s" % (sd,file_name)))

        # Twice_per_day data
        if file_name in Files_tpd:
            print(station_name)
            if station_name not in emulate_data:
                emulate_data[station_name]={}
            emulate_data[station_name].update(load_from_file_tpd(
                         "%s/../original_data_csv/%s" % (sd,file_name)))

    # Special cases
    print('TENERIFE')
    emulate_data['TENERIFE']=load_from_file_teneriffe(
                     "%s/../original_data_csv/Tenerife.Teneriffe.csv" % sd)
    print('BAGHDAD')
    emulate_data['BAGHDAD']=load_from_file_middle_east(
                     "%s/../original_data_csv/ME_daily_pressure.ME_daily_pressure.csv" % sd,3)
    print('BASRA')
    emulate_data['BASRA']=load_from_file_middle_east(
                     "%s/../original_data_csv/ME_daily_pressure.ME_daily_pressure.csv" % sd,4)
    print('DIYARBAKIR')
    emulate_data['DIYARBAKIR']=load_from_file_middle_east(
                     "%s/../original_data_csv/ME_daily_pressure.ME_daily_pressure.csv" % sd,5)
    print('BEIRUT')
    emulate_data['BEIRUT']=load_from_file_middle_east(
                     "%s/../original_data_csv/ME_daily_pressure.ME_daily_pressure.csv" % sd,6)

    # Output the data in new format
    for station in list(emulate_data.keys()):
        output_station(station,emulate_data[station])
