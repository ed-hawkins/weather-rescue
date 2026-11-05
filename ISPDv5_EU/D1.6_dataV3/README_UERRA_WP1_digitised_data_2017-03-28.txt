#C3/URV, 28 March 2017
#Format of the data is: #stationid,stationname,wmocode,latitude,longitude,altitude,sourceid,elementid,year,month,day,hour,V1value,V2value,V3value,convalue,qcversion,flag,conversioncode.
#sourceid, elementid and flag definitions are given at the bottom of this README. 
#conversioncode details are given in the associated metadata Excel spreadsheet (Sheet 2), along with temporal coverage of each variable for each station.
#Each observation in the data file has four versions: V1value, V2value, V3value and convertedvalue. V1 are the original data; V2 are the data with automatic 
#statistical quality control applied; V3 are the data with statistical and spatial quality control applied; convertedvalue are the final version converted into SI units.

#Full station list 
stationid	wmocode	stationname	latitude	longitude	altitude	sourcename	description
ALG0060355	60355	Skidda Cap Bougarouni	37.08	6.47	195	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060357	60357	Annaba Cap de Garde	36.97	7.79	161	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060367	60367	La Calle El Kala	36.9	8.44	10	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060369	60369	Alger Ville	36.78	3.07	59	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060395	60395	Tizi Ouzou	36.72	4.05	222	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060400	60400	Bejaia Cap Carbon	36.78	5.1	225	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060401	60401	Bejaia Bougie	36.75	5.1	9	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060419	60419	Constantine	36.37	6.62	660	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060425	60425	Orleansville	36.17	1.34	112	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060445	60475	Setif	36.18	5.4	1081	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060461	60461	Oran	35.7	-0.65	53	Bulletin Meteorologique de Algerie/Maroc	Available through NOAA-CDMP
ALG0060475	60445	Tebessa	35.42	8.12	863	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060485	60485	Oran Cap Falcon	35.77	-0.8	78	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060517	60517	Nemours	35.1	-1.85	83	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060520	60520	Sidi Bel Abbess	35.2	-0.63	476	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060545	60545	Laghouat	33.8	2.89	767	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060550	60550	Geryville	33.68	1	1320	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060590	60590	El Golea	30.55	3.07	394	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG0060656	60656	Tindouf	27.67	-9.33	431	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG1060525	60525	Biskra	34.85	5.72	125	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
ALG10XXXXX	99999	Fort National	36.63	4.2	942	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
BOH0014652	14652	Bjelasnica	43.72	18.28	2067	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
BOH0014653	14653	Sarajevo-Butmir	43.87	18.43	630	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
CRO0014236	14236	Zagreb-Gric	45.82	15.98	157	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
CRO0014445	14445	Split-Marjan	43.52	16.43	122	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
CYP0017600	17600	Paphos Ktima	34.77	32.43	30	Cyprus Meteorological Returns	Available through the UK Met Office
CYP0017606	17606	Nicosia	35.19	33.37	152	Cyprus Meteorological Returns	Available through the UK Met Office
CZE0011518	11518	Praha-Luzyne	50.1	14.45	381	Rocenka-annuaire	Available through NOAA-CDMP
CZE0011582	11582	Tabor	49.42	14.67	444	Rocenka-annuaire	Available through NOAA-CDMP
CZE0011622	11622	Caslav-filipor	49.9	15.4	252	Rocenka-annuaire	Available through NOAA-CDMP
CZE0011721	11721	Brno-Kvetna	49.2	16.57	233	Rocenka-annuaire	Available through NOAA-CDMP
CZE0011723	11723	Brno Turany	49.15	16.7	241	Rocenka-annuaire	Available through NOAA-CDMP
CZE00XXXXX	99999	Praded	50.08	17.23	1490	Rocenka-annuaire	Available through NOAA-CDMP
CZE10XXXXX	99999	SkalnatePleso	49.2	20.92	1778	Rocenka-annuaire	Available through NOAA-CDMP
EGY0062300	62300	Salloum	31.55	25.18	4	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062306	62306	Mersa Matruh	31.33	27.22	25	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062330	62330	Damietta	31.42	31.82	5	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062333	62333	Port Said	31.28	32.23	6	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062339	62339	Damanhour	31.03	30.47	2	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062342	62342	El Mansura	31.34	31.08	10	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062348	62348	Tanta	30.78	31	15	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062354	62354	Zagazig	30.58	31.5	13	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062374	62374	Cairo Ezbekiya	30.05	31.25	20	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062375	62375	Giza	30.03	31.21	28	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062378	62378	Helwan	29.86	31.34	116	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062381	62381	Fayoum	29.3	30.85	23	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062387	62387	Minya	28.08	30.73	40	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062393	62393	Asyut-Heat airport	27.05	31.02	226	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062405	62405	Luxor Airport	25.67	32.7	93	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062417	62417	Siwa	29.2	25.48	-15	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062441	62441	Ismailia	30.6	32.23	10	Egypt Daily Weather Report	Available through NOAA-CDMP
EGY0062450	62450	El Suez	29.93	32.55	10	Egypt Daily Weather Report	Available through NOAA-CDMP
ESP10XXX42	99999	Tarragona	41.1	0.75	58	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
ESPXX00201	99999	Barcelona	41.41	2.16	94	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
ESPXX0200D	99999	Barcelona Turo Del Putxet	41.41	2.14	179	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
ESPXX0201B	99999	Barcelona Atarazanas	41.38	2.17	37	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
ESPXX9771C	99999	Lleida	41.62	0.69	192	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
ESP00000C6	99999	Castellnou de Seana	41.6566	0.95172	264	MeteoCat
ESP00000C7	99999	Tàrrega	41.66695	1.16234	427	MeteoCat
ESP00000C8	99999	Cervera	41.67555	1.29609	554	MeteoCat
ESP00000C9	99999	Mas de Barberans	40.71825	0.39988	240	MeteoCat
ESP00000CC	99999	Orís	42.07398	2.20862	626	MeteoCat
ESP00000CD	99999	la Seu d'Urgell - Bellestar	42.37083	1.43277	849	MeteoCat
ESP00000CE	99999	els Hostalets de Pierola	41.53109	1.80813	316	MeteoCat
ESP00000CG	99999	Molló - Fabert	42.37717	2.41456	1405	MeteoCat
ESP00000CI	99999	Sant Pau de Segúries	42.25839	2.36429	852	MeteoCat
ESP00000CJ	99999	Organyà	42.21624	1.33132	566	MeteoCat
ESP00000CL	99999	Sant Salvador de Guardiola	41.67399	1.76796	349	MeteoCat
ESP00000CP	99999	Sant Romà d'Abella	42.13924	1.03893	690	MeteoCat
ESP00000CQ	99999	Vilanova de Meià	41.99546	1.02569	594	MeteoCat
ESP00000CR	99999	la Quar	42.08032	1.9624	873	MeteoCat
ESP00000CT	99999	el Pont de Suert	42.39811	0.74362	823	MeteoCat
ESP00000CU	99999	Vielha	42.69856	0.79397	1002	MeteoCat
ESP00000CV	99999	la Pobla de Segur	42.23939	0.96434	513	MeteoCat
ESP00000CW	99999	l'Espluga de Francolí	41.39241	1.09894	446	MeteoCat
ESP00000CY	99999	Muntanyola	41.87813	2.17873	816	MeteoCat
ESP00000D1	99999	Margalef	41.28521	0.75383	404	MeteoCat
ESP00000D2	99999	Vacarisses	41.59252	1.915	343	MeteoCat
ESP00000D3	99999	Vallirana	41.38197	1.93564	252	MeteoCat
ESP00000D4	99999	Roses	42.27065	3.18165	24	MeteoCat
ESP00000D5	99999	Barcelona - Observatori Fabra	41.41843	2.12388	411	MeteoCat
ESP00000D6	99999	Portbou	42.43515	3.16622	196	MeteoCat
ESP00000D7	99999	Vinebre	41.18499	0.59376	53	MeteoCat
ESP00000D8	99999	Horta de Sant Joan	40.95134	0.30565	515	MeteoCat
ESP00000D9	99999	el Vendrell	41.21553	1.52121	59	MeteoCat
ESP00000DB	99999	el Perelló	40.87287	0.71581	179	MeteoCat
ESP00000DC	99999	Olot	42.19144	2.48263	422	MeteoCat
ESP00000DF	99999	la Bisbal d'Empordà	41.97751	3.03543	29	MeteoCat
ESP00000DG	99999	Núria (1.971 m)	42.39848	2.15517	1971	MeteoCat
ESP00000DI	99999	Font-rubí	41.43292	1.62386	415	MeteoCat
ESP00000DJ	99999	Banyoles	42.11653	2.78969	176	MeteoCat
ESP00000DK	99999	Torredembarra	41.14677	1.41846	2	MeteoCat
ESP00000DL	99999	Illa de Buda	40.70719	0.83449	0	MeteoCat
ESP00000DN	99999	Anglès	41.96095	2.63108	150	MeteoCat
ESP00000DO	99999	Castell d'Aro	41.80857	3.03241	14	MeteoCat
ESP00000DP	99999	Das - Aeròdrom	42.38605	1.8664	1097	MeteoCat
ESP00000DQ	99999	Vila-rodona	41.30728	1.36259	287	MeteoCat
ESP00000F2	99999	Port de Barcelona - Sirena	41.31725	2.16537	3	MeteoCat
ESP00000F4	99999	Port de Barcelona - Dispensari	41.31725	2.16537	3	MeteoCat
ESP00000H1	99999	Òdena	41.58642	1.65306	333	MeteoCat
ESP00000J5	99999	Pantà de Darnius - Boadella	42.34215	2.83423	158	MeteoCat
ESP00000MR	99999	Pantà de Siurana	41.25079	0.9106	500	MeteoCat
ESP00000R1	99999	el Pont de Vilomara	41.70637	1.87276	210	MeteoCat
ESP00000U2	99999	Sant Pere Pescador	42.17716	3.0968	4	MeteoCat
ESP00000UP	99999	Cabrils	41.51773	2.37702	81	MeteoCat
ESP00000UU	99999	Amposta	40.70776	0.6321	3	MeteoCat
ESP00000UW	99999	els Alfacs	40.62725	0.65922	0	MeteoCat
ESP00000VK	99999	Raimat	41.68328	0.4487	286	MeteoCat
ESP00000VQ	99999	Constantí	41.1713	1.16774	112	MeteoCat
ESP00000VS	99999	Lac Redon (2.247 m)	42.63835	0.77889	2247	MeteoCat
ESP00000WQ	99999	Montsec d'Ares (1.572 m)	42.0513	0.72952	1572	MeteoCat
ESP00000WS	99999	Viladrau	41.84008	2.41877	953	MeteoCat
ESP00000WT	99999	Malgrat de Mar	41.64707	2.75658	2	MeteoCat
ESP00000WU	99999	Badalona - Museu	41.45215	2.24757	42	MeteoCat
ESP00000WV	99999	Guardiola de Berguedà	42.23414	1.87485	788	MeteoCat
ESP00000WZ	99999	Cunit	41.20187	1.63346	17	MeteoCat
ESP00000X1	99999	Falset	41.15374	0.81953	359	MeteoCat
ESP00000X3	99999	Alguaire	41.74281	0.5358	370	MeteoCat
ESP00000X4	99999	Barcelona - el Raval	41.3839	2.16775	33	MeteoCat
ESP00000X5	99999	PN dels Ports	40.79705	0.31822	1055	MeteoCat
ESP00000X8	99999	Barcelona - Zona Universitària	41.37919	2.1054	79	MeteoCat
ESP00000X9	99999	Caldes de Montbui	41.61265	2.16836	176	MeteoCat
ESP00000XA	99999	la Panadella	41.60257	1.4007	785	MeteoCat
ESP00000XC	99999	Castellbisbal	41.47892	1.97546	147	MeteoCat
ESP00000XD	99999	Ulldemolins	41.32	0.8857	687	MeteoCat
ESP00000XE	99999	Tarragona - Complex Educatiu	41.10393	1.201	5	MeteoCat
ESP00000XF	99999	Sabadell - Parc Agrari	41.56568	2.06952	258	MeteoCat
ESP00000XG	99999	Parets del Vallès	41.56734	2.22619	123	MeteoCat
ESP00000XH	99999	Sort	42.40533	1.12993	679	MeteoCat
ESP00000XI	99999	Mollerussa	41.61817	0.87182	247	MeteoCat
ESP00000XJ	99999	Girona	41.98223	2.80686	72	MeteoCat
ESP00000XT	99999	Solsona	41.98766	1.51165	691	MeteoCat
ESP00000Y9	99999	Port de Barcelona - ZAL Prat	41.31723	2.13091	4	MeteoCat
GER0010453	10435	Brocken	51.8	10.62	1142	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0010488	10488	Dresden	51.13	13.75	230	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0027024	27024	Nusse	53.66	10.58	35	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0027221	27221	Bornhoved	54.07	10.22	40	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0030155	30155	Westerhever	54.38	8.68	1	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0030301	30301	Hademarschen	52.12	9.41	46	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0031115	31115	Cuxhaven	53.83	8.77	2	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0033055	33055	Laar	52.62	6.74	11	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0048261	48261	Hitzacker	53.16	11.04	28	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0048527	48527	Schwarzerbek	53.5	10.49	40	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0048605	48605	Sauensiek	53.38	9.6	39	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0048635	48635	Pinneberg	53.66	9.78	8	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0052336	52336	Hoxter	51.78	9.4	93	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0053024	53024	Werther	52.07	8.42	134	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0053131	53131	Lubbecke	52.32	8.62	55	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0056402	56402	Wildeshausen	52.87	8.4	48	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0070233	70233	Bernau-kaiserhaus	47.8	8.03	920	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0070312	70312	Freiamt-Keppenbach	48.14	7.92	275	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0070677	70677	Landau-Pfalz	49.2	8.1	150	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0070755	70755	Speyer	49.36	8.42	99	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0074151	74151	Biebergemund-Wirtheim	50.23	9.25	135	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0078384	78384	Hilden	51.17	6.97	66	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
GER0079350	79350	Soest,Landwirtshaftliche Schule	51.57	8.12	110	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
LBN0040106	40106	Ksara	33.82	35.89	918	Bulletin Climatologique, Lebanon	Available through NOAA-CDMP
MAR0060100	60100	Tanger city	35.78	-5.82	86	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060115	60115	Oujda	34.78	-1.93	478	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
MAR0060115	60115	Oujda	34.78	-1.93	478	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060120	60120	Kenitra (Port-L Yautey)	34.3	-6.6	14	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060160	60160	Ifrane	33.5	-5.17	1664	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060190	60190	Kasba-Tadla	32.53	-6.28	518	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060195	60195	Midelt	32.68	-4.73	1515	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060250	60250	Agadir	30.38	-9.57	19	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
MAR0060265	60265	Ouarzazate	30.93	-6.9	1136	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
NOR0000700	01393	DREVSJØ	61.89	12.05	672	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0001400	99999	BREKKE SLUSE	59.15	11.56	114	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0003150	99999	KALNES	59.32	11.05	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0004780	01384	GARDERMOEN	60.21	11.08	202	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0004870	99999	EGNERFJELL	60.06	11.27	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0004930	99999	HVAM	60.1	11.38	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0005650	99999	VINGER	60.22	12.03	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0006040	99999	FLISA	60.62	12.02	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0007010	99999	RENA - HAUGEDALEN	61.16	11.44	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0008710	99999	SØRNESSET	61.89	10.15	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0010400	99999	RØROS	62.57	11.38	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0011500	01381	ØSTRE TOTEN - APELSVOLL	60.7	10.87	264	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0012180	99999	ILSENG	60.8	11.2	182	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0012550	01382	KISE PA HEDMARK	60.77	10.81	128	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0014600	99999	VÅGÅ - KLONES	61.86	9.08	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0015540	99999	GJEILO I SKJÅK	61.87	8.45	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0015720	99999	BRÅTÅ	61.91	7.86	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0017050	99999	RÅDE - TOMB	59.32	10.81	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0017150	01494	RYGGE	59.37	10.8	40	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0017290	99999	JELØY	59.44	10.59	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0017850	01463	ÅS	59.66	10.78	92	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0018700	01492	OSLO - BLINDERN	59.94	10.72	94	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0018950	01490	TRYVANNSHØGDA	59.98	10.67	514	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0019400	99999	FORNEBU	59.89	10.62	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0019710	01486	ASKER	59.86	10.43	163	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0023160	01369	ÅBJØRSBRÅTEN	60.92	9.29	639	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0023500	01371	LØKEN I VOLBU	61.12	9.06	521	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0027450	01481	MELSOM	59.23	10.35	26	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0027470	01483	TORP	59.18	10.26	88	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0027500	01482	FÆRDER FYR	59.03	10.52	6	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0028800	99999	LYNGDAL I NUMEDAL	59.91	9.52	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0029770	99999	DAGALI - FAGERLUND	60.42	8.45	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0031970	01461	GAUSTATOPPEN	59.85	8.66	1804	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0032100	99999	GVARV	59.39	9.17	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0034120	99999	JOMFRULAND FYR	58.87	9.6	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0035860	01467	LYNGØR FYR	58.64	9.15	4	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0036200	01465	TORUNGEN FYR	58.4	8.79	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0037230	01455	TVEITSUND	59.03	8.52	252	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0038140	01464	LANDVIK	58.34	8.52	6	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0039040	01452	KJEVIK	58.2	8.08	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0039100	01448	OKSØY FYR	58.07	8.05	9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0040900	99999	BJÅEN	59.64	7.44	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0041110	99999	MANDAL II	58.05	7.45	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0041680	99999	KONSMO - HÆGELAND	58.27	7.31	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0041770	01436	LINDESNES FYR	57.98	7.05	16	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0042160	01427	LISTA FYR	58.11	6.57	14	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0044080	01412	OBRESTAD FYR	58.66	5.56	24	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0044560	01415	SOLA	58.88	5.64	7	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0044640	01416	STAVANGER - VÅLAND	58.96	5.73	72	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0045900	99999	FISTER	59.18	6.07	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0046610	01424	SAUDA	59.65	6.35	5	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0047200	99999	SKUDENES II	59.15	5.25	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0047300	01403	UTSIRA FYR	59.31	4.87	55	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0048330	01406	SLÅTTERØY FYR	59.91	5.07	25	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0049490	01342	ULLENSVANG FORSØKSGARD	60.32	6.65	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0050300	99999	KVAMSKOGEN	60.39	5.91	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0050460	99999	FANA FORSØKSSTASJON	60.26	5.35	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0050500	01311	FLESLAND	60.29	5.23	48	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0050540	01317	BERGEN - FLORIDA	60.38	5.33	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0050560	99999	BERGEN - FREDRIKSBERG	60.4	5.31	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0051670	99999	REIMEGREND	60.69	6.74	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0052300	99999	MODALEN	60.83	5.93	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0052530	99999	HELLISØY FYR	60.75	4.71	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0052860	01319	TAKLE	61.03	5.38	38	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0053100	99999	VANGSNES	61.17	6.64	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0054130	99999	LÆRDAL - TØNJUM	61.06	7.52	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0055160	99999	FORTUN	61.5	7.7	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0055230	99999	FANNARÅKI	61.52	7.91	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0055780	99999	LEIKANGER	61.18	6.86	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0055840	99999	FJÆRLAND - SKARESTAD	61.44	6.77	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0057890	99999	DOMBESTEIN	61.88	5.65	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0058070	01318	SANDANE	61.79	6.18	51	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0058700	99999	OPPSTRYN	61.93	7.23	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0059100	99999	KRÅKENES FYR	62.03	4.99	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0059800	01205	SVINØY FYR	62.33	5.27	38	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0060500	01218	TAFJORD	62.23	7.42	11	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0060990	01210	VIGRA	62.56	6.12	22	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0061770	99999	LESJASKOG	62.23	8.37	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0063420	01226	SUNNDALSØRA III	62.67	8.56	10	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0064260	99999	KRISTIANSUND N	63.11	7.75	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0064580	99999	ÅLVUNDFJORD	62.83	8.52	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0065100	99999	VINJEØRA II	63.21	8.99	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0066100	99999	SONGLI	63.33	9.65	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0066830	99999	SÆTER I KVIKNE	62.62	10.25	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0068860	01257	TRONDHEIM - VOLL	63.41	10.45	127	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0069070	99999	VENNAFJELL	63.31	10.92	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0069100	01271	VÆRNES	63.46	10.93	12	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0070360	99999	SULSTUA	63.67	12.02	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0070850	01124	SNÅSA - KJEVLIA	64.16	12.47	195	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0071550	01241	ØRLAND III	63.7	9.61	10	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0072850	99999	HØYLANDET	64.6	12.27	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0073470	99999	NORDLI III	64.46	13.59	-99.9	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
NOR0075410	01262	NORDØYAN FYR	64.8	10.55	33	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
ROM0015083	15083	Dej	47.13	23.9	232	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
ROM0015118	15118	Stana de Vale	46.69	22.62	1108	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
ROM0015148	15148	Bucin	46.65	25.3	1282	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
ROM0015279	15279	Balea Lac	45.6	24.61	2047	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
ROM0015314	15314	Resita	45.31	21.89	279	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
ROM0015434	15434	Slatina	44.44	24.35	172	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
SER0013262	13262	Loznica	44.55	19.3	121	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
SER0013272	13272	Beograd-Surcin	44.8	20.47	132	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
SER0013367	13367	Zlatibor	43.73	19.92	1029	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
SLO0011814	11814	Bratislava-Trnavaka	48.17	17.13	139	Rocenka-annuaire	Available through NOAA-CDMP
SLO0011930	11930	Lomnicky Stit	49.2	20.22	2638	Rocenka-annuaire	Available through NOAA-CDMP
SLV0014008	14008	Kredarica	46.38	13.85	2515	Slovenian Environmental Agency	Provided by Slovenian Environmental Agency. Contact: Matija Klancar
SLV0014192	14192	Ljubljana	46.7	14.52	300.5	Slovenian Environmental Agency	Provided by Slovenian Environmental Agency. Contact: Matija Klancar
SLV0014249	99999	Novo Mesto	45.8	15.18	220	Slovenian Environmental Agency	Provided by Slovenian Environmental Agency. Contact: Matija Klancar
SWE0052230	99999	Falsterbo	55.38	12.82	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0052510	99999	Örja	55.88	12.87	11	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0053200	99999	Smygehuk	55.34	13.36	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0053220	99999	Maglarp	55.38	13.06	17	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0053260	99999	Ystad	55.44	13.83	32	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0053390	99999	Alnarp Fruktavdelning	55.66	13.09	10	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0053650	99999	Björka	55.7	13.63	32	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0054300	99999	Bollerup	55.49	14.05	55	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0054330	99999	Simrishamn	55.55	14.36	8	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0055570	99999	Utklippan A	55.96	15.71	3	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0062180	99999	Barkåkra	56.3	12.84	18	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0062190	99999	Kullen	56.3	12.45	72	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0062410	99999	Halmstad Flygflottilj	56.68	12.83	30	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0063050	99999	Ljungbyhed	56.08	13.23	43	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0063490	99999	Bolmen	56.81	13.7	160	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0064020	99999	Hanö A	56.01	14.85	55	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0064520	99999	Växjö D	56.88	14.83	162	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0064560	99999	Växjö-Kronoberg	56.92	14.73	182	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0066040	99999	Ölands Södra Grund	56.07	16.68	1	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0066120	99999	Ölands Södra Udde	56.2	16.4	3	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0066410	99999	Kalmar	56.73	16.29	15	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0068550	99999	Hoburg	56.92	18.15	38	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0068560	99999	Hoburg A	56.92	18.15	39	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0071360	99999	Trubaduren	57.6	11.63	1	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0071380	99999	Vinga A	57.63	11.61	12	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0071430	99999	Torslanda	57.72	11.78	3	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0071470	99999	Säve	57.78	11.88	20	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0072080	99999	Varberg	57.11	12.27	20	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0072120	99999	Fagered	57.2	12.81	100	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0072560	99999	Alingsås D	57.89	12.55	70	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0073250	99999	Ambjörnarp	57.42	13.28	220	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0073270	99999	Axelfors	57.45	13.1	150	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0074180	99999	Hagshult Mo	57.29	14.14	169	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0074460	99999	Jönköpings Flygplats	57.75	14.07	226	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0075040	99999	Allgunnen	57.07	15.97	115	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0075140	99999	Blankaström	57.22	15.92	80	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0075280	99999	Arvingetorp	57.45	15.03	210	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0075480	99999	Askeryd	57.81	14.99	250	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0076470	99999	Västervik	57.72	16.47	33	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0076590	99999	Överum	57.99	16.31	30	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0077220	99999	Ölands Norra Udde	57.37	17.1	4	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0078040	99999	Näsudden	57.07	18.22	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0078300	99999	Roma Aut	57.5	18.46	32	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0078400	99999	Visby Flygplats	57.66	18.34	42	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0079580	99999	Fårö	57.9	19.16	8	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0081050	99999	Måseskär A	58.09	11.33	16	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0081060	99999	Måseskär	58.09	11.34	14	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0081350	99999	Väderöarna A	58.58	11.07	22	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0081560	99999	Strömstad	58.93	11.2	20	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0082260	99999	Såtenäs	58.44	12.71	54	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0083460	99999	Lurö	58.79	13.25	55	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0084310	99999	Karlsborg Mo	58.51	14.51	95	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0084580	99999	Snavlunda	58.97	14.9	144	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0085040	99999	Malexander	58.07	15.23	195	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0085050	99999	Malexander A	58.07	15.24	195	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0085160	99999	Bjärka-Säby	58.27	15.74	100	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0085240	99999	Malmslätt	58.4	15.53	93	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0086370	99999	Norrköping-Sörby	58.61	16.12	27	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0087140	99999	Harstena A	58.25	17.01	14	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0087150	99999	Harstena	58.25	17.01	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0087360	99999	Gustaf Dalen A	58.59	17.47	25	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0087450	99999	Landsort	58.74	17.87	4	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0089230	99999	Gotska Sandön A	58.39	19.2	16	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0089240	99999	Gotska Sandön	58.39	19.2	12	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0092040	99999	Bengtsfors D	59.05	12.23	125	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0092480	99999	Adolfsfors	59.8	12.23	125	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0093220	99999	Karlstad Flygplats	59.45	13.34	107	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0093230	99999	Karlstad Aut	59.36	13.47	46	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0094170	99999	Villingsberg	59.28	14.7	148	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0096350	99999	Västerås	59.6	16.6	10	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0097110	99999	Riksten	59.18	17.92	54	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0097200	99999	Stockholm-Bromma	59.35	17.95	14	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0097260	99999	Barkarby	59.42	17.88	17	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0097510	99999	Uppsala Aut	59.86	17.62	13	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0097530	99999	Uppsala Flygplats	59.9	17.59	21	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0098610	99999	Berga	59.08	18.12	15	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0099090	99999	Almagrundet A	59.16	19.13	3	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0099270	99999	Svenska Högarna	59.44	19.51	12	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0099330	99999	Svenska Björn	59.55	20.02	1	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0099450	99999	Söderarm A	59.75	19.41	15	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0103090	99999	Gustavsfors	60.15	13.8	190	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0103410	99999	Malung	60.67	13.71	310	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0105370	99999	Falun-Lugnet	60.62	15.66	140	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0106080	99999	Bjurfors	60.13	16.13	125	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0106100	99999	Folkärna	60.17	16.31	68	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0107400	99999	Gävle	60.65	17.17	16	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0107440	99999	Eggegrund A	60.73	17.56	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0107530	99999	Västra Banken	60.88	17.93	25	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0108170	99999	Understen	60.28	18.92	12	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0108320	99999	Örskär A	60.53	18.38	8	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0112540	99999	Idre Fjäll A	61.89	12.85	869	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0113110	99999	Tandådalen	61.18	13.02	830	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0113410	99999	Särna	61.71	13.13	437	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0114010	99999	Mora	61	14.59	175	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0115230	99999	Edsbyn	61.38	15.84	161	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0116160	99999	Bergvik	61.26	16.84	50	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0117160	99999	Söderhamn A	61.27	17.1	26	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0117330	99999	Agö	61.55	17.47	20	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0124020	99999	Sveg	62.02	14.19	432	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0127130	99999	Brämön A	62.22	17.74	17	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0127380	99999	Härnösand	62.63	17.95	8	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0132030	99999	Sylarna A	63.05	12.28	1030	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0133260	99999	Åreskutan	63.43	13.07	1280	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0133470	99999	Överäng	63.78	13.07	450	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0133570	99999	Stora Stensjön	63.97	13.72	680	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0134110	99999	Frösön	63.2	14.49	376	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0135440	99999	Hallviken	63.73	15.5	337	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0136010	99999	Bispgården	63.03	16.55	165	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0136420	99999	Junsele	63.68	16.95	215	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0139340	99999	Nordmaling	63.57	19.49	4	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0139540	99999	Vännäs	63.92	19.7	87	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0139560	99999	Bjurholm	63.93	19.22	178	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0140200	99999	Sydostbrotten	63.38	20.1	24	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0140360	99999	Holmögadd A	63.59	20.76	6	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0144300	99999	Gäddede	64.5	14.16	328	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0145340	99999	Högland	64.57	15.92	401	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0145500	99999	Avasjö-Borgafjäll D	64.84	15.09	530	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0147100	99999	Åsele	64.16	17.35	310	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0147570	99999	Gunnarn	65.01	17.71	280	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0149160	99999	Hällnäs-Lund	64.27	19.63	181	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0151290	99999	Bjuröklubb	64.48	21.58	36	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0154860	99999	Abelvattnet	65.53	14.97	665	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0155710	99999	Blaikliden	65.05	15.75	520	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0157720	99999	Stensele	65.07	17.15	325	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0158850	99999	Storberg	65.51	18.95	453	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0158900	99999	Bergnäsudden	65.67	18.15	420	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0159970	99999	Suddesjaur	65.89	19.09	342	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0160800	99999	Fagerheden	65.34	20.9	220	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0162800	99999	Farstugrunden	65.33	22.75	1	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0162860	99999	Luleå Flygplats	65.54	22.12	17	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0163950	99999	Haparanda	65.84	24.11	5	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0166840	99999	Ballastviken	66.49	16.54	470	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0167710	99999	Arjeplog A	66.05	17.84	431	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0167980	99999	Kvikkjokk-Årrenjarka	66.89	18.02	314	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0169880	99999	Jokkmokk	66.61	19.83	240	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0171700	99999	Övre Svartlå D	66.02	21.17	60	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0178740	99999	Aktse	67.15	18.31	530	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0180730	99999	Gällivare	67.14	20.66	365	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0180750	99999	Malmberget	67.17	20.64	400	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0183760	99999	Pajala	67.21	23.39	168	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0188800	99999	Abisko	68.36	18.82	388	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0188830	99999	Riksgränsen	68.43	18.13	508	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0188840	99999	Tornehamn	68.43	18.63	512	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0189740	99999	Bergfors	68.15	19.8	480	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0191730	99999	Övre Soppero	68.09	21.7	365	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
SWE0192830	99999	Karesuando	68.44	22.45	330	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
TUN0060714	99999	Bizerte Cap Blanc	37.33	9.84	264	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
TUN0060715	60715	Tunis Carthago	36.8	10.17	36	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
TUN0060741	99999	El Djem	35.33	10.7	112	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
TUN0060760	60760	Tozeur	33.95	8.11	50	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
TUN1060750	99999	Sfax	34.72	10.72	23	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
TUR0017034	17034	Giresun	40.92	38.38	37	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017040	17040	Rize	41.03	40.49	29	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017045	17045	Artvin	41.17	41.42	628	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017062	17062	Istambul-Goztepe	40.97	29.08	40	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017096	17096	Erzurum	39.92	41.27	1756	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017098	17098	Kars	40.6	40.08	1775	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017100	17100	Igdir	39.93	44.03	858	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017116	17116	Bursa	40.23	29.02	101	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017120	17120	Bilecik	40.15	29.98	539	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017155	17155	Kutahya	39.42	29.99	969	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017170	17170	Van	38.4	43.32	1661	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017186	17186	Manisa	38.62	27.43	71	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017195	17195	Kayseri	38.78	35.48	1054	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017202	17202	Elazig	38.6	39.28	903	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017210	17210	Siirt	37.93	42	895	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017234	17234	Aydin	37.85	27.85	57	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017250	17250	Nigde	37.97	34.68	1208	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017260	17260	Gaziantep	37.08	37.37	855	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017280	17280	Diyarbakir	37.88	40.18	686	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017296	17296	Fethiye	36.62	29.12	3	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017320	17320	Anamur	36.08	32.83	4	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017964	17964	Islahiye	37.01	36.38	513	Yillik-Bulteni	Available through NOAA-CDMP
TUR0017984	17984	Antakya	36.12	36.1	100	Yillik-Bulteni	Available through NOAA-CDMP
TUR1099999	99999	Cankiri	40.6	33.63	754	Yillik-Bulteni	Available through NOAA-CDMP
TUR10XXX00	99999	Karakose	39.75	43.05	1632	Yillik-Bulteni	Available through NOAA-CDMP

# Missing value codes 
# -99.9	Missing observation
# 99999	No WMO code assigned
#
# All times are local
# 
# Variables
# pp	Sea level pressure (hPa)
# sp	Station level pressure (hPa)
# rr	Precipitation (mm)
# tt	Atmospheric temperature	(ºC)
# dp	Dew point temperature (ºC)
# ff	Wind strength (m/s)
# fg 	10 minutes maximum wind speed (m/s)
# fs	Fresh snow (mm) 
# 
# rh	Relative humidity (%)
# sd	Snow depth (mm)
# wd	Wind direction (º from north)
# hg	Relative humidity hygrometer (%)
# wb	Wet bulb temperature (ºC)
# ffv10	Vector wind velocity at 10 m (m/s)
# wdv10	Vector wind direction at 10 m (º)
# ffv6	Vector wind velocity at 6 m (m/s)
# wdv6	Vector wind direction at 6 m (º)
# ffv2	Vector wind velocity at 2 m (m/s)
# wdv2	Vector wind direction at 2 m (º)
# ffs10	Scalar wind velocity at 10 m (m/s)
# wds10	Scalar wind direction at 10 m (º)
# ffs6	Scalar wind velocity at 6 m (m/s)
# wds6	Scalar wind direction at 6 m (º)
# ffs2	Scalar wind velocity at 2 m (m/s)
# wds2	Scalar wind direction at 2 m (º)
# 
# 
# A note on fs, sd and rr
# values with 9999 indicate 24hour accumulation (0700 the previous day to 0700 recording day)
# fs and sd at 0700 indicates 12 hour accumulation (1900 the previous day to 0700 recording day)
# fs and sd at 1900 indicated 12 hour accumulation (0700 recording day to 1900 recording day)
# Sub-daily rr values are accumulated totals from the hour of previous rainfall observation.
# A rainfall value of -3 indicates trace rainfall (Brocken only)
# A snow depth value of FL indicated broken snow cover (Brocken only)
# Other sub-daily rr values are accumulated totals since the hour of previous rainfall observation.
# 
# Quality control flags
# 
# Values checked by statistical quality control, but not by automatic spatial homogeneity assessment (HadISD procedure)
# fl10	Not flagged in quality control testing, not tested by HadISD procedure
# fl11	Removed due to gross digitiser error, not tested by HadISD procedure
# fl12	Corrected typographical error, not tested by HadISD procedure
# fl13	Removed after expert consideration, not tested by HadISD procedure
# fl14	Validated as correct, not tested by HadISD procedure
# fl15	Corrected after expert consideration, not tested by HadISD procedure
# fl17	Removed as no data in source, not tested by HadISD procedure
# 
# For data provided in digital format only
# fl18	Provided in pre-QCed digitised format by a national meteorological service, not tested by HadISD procedure
# fl20	Flagged as suspicious/aggregated by data provider, not tested by HadISD procedure (provided data only)
# 
# Values checked by statistical quality control and automatic spatial homogeneity assessment (HadISD procedure, V3)
# fl36 	Removed by HadISD procedure
# fl30	Not flagged in quality control testing, passed HadISD procedure
# fl32	Corrected typographical error, passed HadISD procedure
# fl34	Validated as correct, passed HadISD procedure
# fl35	Corrected after expert consideration, passed HadISD procedure
# 
# Sourceid codes
# sourceid	sourcename	description
# so64	Rocenka-annuaire	Available through NOAA-CDMP
# so65	Slovenian Environmental Agency	Provided by Slovenian Environmental Agency. Contact: Matija Klancar
# so16	Egypt Daily Weather Report	Available through NOAA-CDMP
# so12	Bulletin Climatologique, Lebanon	Available through NOAA-CDMP
# so63	Cyprus Meteorological Returns	Available through the UK Met Office
# so06	Bulletin Meteoorologique du Maroc	Available through NOAA-CDMP
# so66	Romanian National Meteorological Administration	Contact: Roxana Bojariu bojariu@meteoromania.ro
# so54	Instituto Nacional de Meteorología Banco de Datos	Provided by the Servei Meteorologic de Catalunya. Contact: Marc Prohom
# so62	Deutscher Wetterdienst	Provided by Deutscher Wetterdienst. Contact: Frank Kaspar
# so61	Yillik-Bulteni	Available through NOAA-CDMP
# so56	Meteoroloski godisnjak 1 - klimatoloski podaci	Provided by Republic Hydro-meteorological Service of Serbia
# so04	Bulletin Meteorologique de Algerie	Available through NOAA-CDMP
# so67	Norwegian Meteorological Institute	Contact: Cristian Lussana cristianl@met.no
# so68	Swedish Meteorological and Hydrological Institute	Contact: Per Unden, Per.Unden@smhi.se
# sources available through NOAA-CDMP were available online at https://www.lib.noaa.gov/collections/imgdocmaps/data_rescue_home.html, 15 February 2017