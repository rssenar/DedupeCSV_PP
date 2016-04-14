
#!/usr/bin/env python3.4.3
import os, re, glob
# ---------------------------------------------------------------------------- #
# Set Constant Variables
SeqNumDatabase = 10000
SeqNumPurchaseP = 30000
SeqNumPurchaseN = 40000
SeqNumPurchase = 50000
# ---------------------------------------------------------------------------- #
CustomerID = 0
FullName = 1
FirstName = 2
MI = 3
LastName = 4
Address1 = 5
Address2 = 6
AddressComb = 7
City = 8
State = 9
Zip = 10
Zip4 = 11
SCF = 12
Phone = 13
HPhone = 14
WPhone = 15
MPhone = 16
Email = 17
VIN = 18
Year = 19
Make = 20
Model = 21
DelDate = 22
Date = 23
Radius = 24
Coordinates = 25
VINLen = 26
DSF_WALK_SEQ = 27
CRRT = 28
ZipCRRT = 29
KBB = 30
AdjustedKBBValue = 31
WinningNum = 32
MailDNQ = 33
BlitzDNQ = 34
Drop = 35
PURL = 36
SCF3DFacility = 37
Vendor = 38
ExpState = 39
Ethnicity = 40
Misc1 = 41
Misc2 = 42
Misc3 = 43
# ---------------------------------------------------------------------------- #
# Header Output list
HeaderRowMain = [
	'CustomerID',
	'FullName',
	'FirstName',
	'MI',
	'LastName',
	'Address1',
	'Address2',
	'AddressFull',
	'City',
	'State',
	'Zip',
	'4Zip',
	'SCF',
	'Phone',
	'HPH',
	'BPH',
	'CPH',
	'Email',
	'VIN',
	'Year',
	'Make',
	'Model',
	'DelDate',
	'Date',
	'Radius',
	'Coordinates',
	'VINLen',
	'DSF_WALK_SEQ',
	'Crrt',
	'ZipCrrt',
	'KBB',
	'Buyback_Value',
	'WinningNumber',
	'MailDNQ',
	'BlitzDNQ',
	'Drop',
	'PURL',
	'SCF3DFacility',
	'Vendor',
	'ExpandedState',
	'Ethnicity',
	'Misc1',
	'Misc2',
	'Misc3'
	]
# ---------------------------------------------------------------------------- #
HeaderReMapDict = {}
def MatchHeaderFields(field, index):
	if bool(re.search('cust.+id',field,flags=re.I)):
		HeaderReMapDict[CustomerID] = 'line[{}]'.format(str(index))
	if bool(re.search('ful.+me',field,flags=re.I)):
		HeaderReMapDict[FullName] = 'line[{}]'.format(str(index))
	elif bool(re.search('fir.+me',field,flags=re.I)):
		HeaderReMapDict[FirstName] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmi\b',field,flags=re.I)):
		HeaderReMapDict[MI] = 'line[{}]'.format(str(index))
	elif bool(re.search('las.+me',field,flags=re.I)):
		HeaderReMapDict[LastName] = 'line[{}]'.format(str(index))
	elif bool(re.search('addr.+1',field,flags=re.I)):
		HeaderReMapDict[Address1] = 'line[{}]'.format(str(index))
	elif bool(re.search('addr.+2',field,flags=re.I)):
		HeaderReMapDict[Address2] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bcity\b',field,flags=re.I)):
		HeaderReMapDict[City] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bstate\b',field,flags=re.I)):
		HeaderReMapDict[State] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bzip\b',field,flags=re.I)):
		HeaderReMapDict[Zip] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\b4zip\b',field,flags=re.I)) or\
	bool(re.search(r'\bzip4\b',field,flags=re.I)):
		HeaderReMapDict[Zip4] = 'line[{}]'.format(str(index))
	elif bool(re.search('HPho.+',field,flags=re.I)) or\
	bool(re.search(r'\bhph\b',field,flags=re.I)):
		HeaderReMapDict[HPhone] = 'line[{}]'.format(str(index))
	elif bool(re.search('WPho.+',field,flags=re.I)) or\
	bool(re.search(r'\bbph\b',field,flags=re.I)):
		HeaderReMapDict[WPhone] = 'line[{}]'.format(str(index))
	elif bool(re.search('MPho.+',field,flags=re.I)) or\
	bool(re.search(r'\bcph\b',field,flags=re.I)):
		HeaderReMapDict[MPhone] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bemail\b',field,flags=re.I)):
		HeaderReMapDict[Email] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bvin\b',field,flags=re.I)):
		HeaderReMapDict[VIN] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\byear\b',field,flags=re.I)) or\
	bool(re.search(r'\bvyr\b',field,flags=re.I)):
		HeaderReMapDict[Year] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmake\b',field,flags=re.I)) or\
	bool(re.search(r'\bvmk\b',field,flags=re.I)):
		HeaderReMapDict[Make] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmodel\b',field,flags=re.I)) or\
	bool(re.search(r'\bvmd\b',field,flags=re.I)):
		HeaderReMapDict[Model] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bdeldate\b',field,flags=re.I)):
		HeaderReMapDict[DelDate] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bdate\b',field,flags=re.I)):
		HeaderReMapDict[Date] = 'line[{}]'.format(str(index))
	elif bool(re.search('dsf.+seq',field,flags=re.I)):
		HeaderReMapDict[DSF_WALK_SEQ] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bcrrt\b',field,flags=re.I)):
		HeaderReMapDict[CRRT] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bkbb\b',field,flags=re.I)):
		HeaderReMapDict[KBB] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bdrop\b',field,flags=re.I)) or\
	bool(re.search(r'\bposition\b',field,flags=re.I)):
		HeaderReMapDict[Drop] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bpurl\b',field,flags=re.I)):
		HeaderReMapDict[PURL] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmisc1\b',field,flags=re.I)):
		HeaderReMapDict[Misc1] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmisc2\b',field,flags=re.I)):
		HeaderReMapDict[Misc2] = 'line[{}]'.format(str(index))
	elif bool(re.search(r'\bmisc3\b',field,flags=re.I)):
		HeaderReMapDict[Misc3] = 'line[{}]'.format(str(index))
# ---------------------------------------------------------------------------- #
# Function to Generate ConvPercentage Value
def ConvPercentage(part, whole):
	if whole == 0:
		return 0
	else:
		return 100 * float(part)/float(whole)

# Function to Convert String To List
def ConvertStringToList(input):
	AppendedList = []
	input = input.split('|')
	for item in input:
		item = item.strip()
		item = str.lower(item)
		AppendedList.append(item)
	return AppendedList

# Function to Reformat Phone Number and strip white space and extra char
def ReformatPhoneNum(Phone):
	Phone = str(Phone).strip()
	Phone = str(Phone).replace('-','')
	Phone = str(Phone).replace('(','')
	Phone = str(Phone).replace(')','')
	return Phone

def StripAndCleanName(Name):
	Name = str(Name).strip()
	Name = str(Name).replace('-','')
	Name = str(Name).replace(' ','')
	Name = str.title(Name)
	return Name

# Convert list item to string
def ConvListToString(input):
	for item in input:
		return item

# Remove temporary files
def Upkeep():
	Files = glob.glob('*.csv')
	for Record in Files:
		if os.path.getsize(Record) == 0: # Empty files
			os.remove(Record)
		if bool(re.match('.+Re-Mapped.+', Record, flags = re.I)):
			os.remove(Record)
# ---------------------------------------------------------------------------- #
DoNotMailSet = set([
	'inc',
	'inc.',
	'incorporated',
	'international',
	'corporation',
	'corporations',
	'corp',
	'corp.',
	'construction',
	'constructions',
	'const',
	'const.',
	'prof',
	'prof.',
	'professional',
	'professionals',
	'service',
	'services',
	'consultancy',
	'consultant',
	'consultants',
	'living',
	'trust',
	'trusts',
	'llc',
	'enterprise',
	'enterprises',
	'infrastructure',
	'infrastructures',
	'the',
	'resource',
	'resources',
	'cooperative',
	'cooperatives',
	'comp',
	'comp.',
	'company',
	'companies',
	'store',
	'stores',
	'dealer',
	'dealers',
	'dealership',
	'dealerships',
	'fleet',
	'office',
	'offices',
	'station',
	'stations',
	'health',
	'partner',
	'partners',
	'acura',
	'am general',
	'audi',
	'bmw',
	'buick',
	'cadillac',
	'chevrolet',
	'chrysler',
	'daewoo',
	'dodge',
	'ferrari',
	'fiat',
	'gmc',
	'honda',
	'hummer',
	'hyundai',
	'infiniti',
	'isuzu',
	'jaguar',
	'jeep',
	'kia',
	'landrover',
	'lexus',
	'lincoln',
	'maserati',
	'maybach',
	'mazda',
	'mercedes',
	'mercedes-benz',
	'mercury',
	'mini',
	'mitsubishi',
	'nissan',
	'oldsmobile',
	'plymouth',
	'pontiac',
	'porsche',
	'ram',
	'saab',
	'saturn',
	'scion',
	'smart',
	'subaru',
	'suzuki',
	'toyota',
	'volkswagen',
	'volvo',
	'auto',
	'autos',
	'automotive',
	'automotives',
	'group'
	'groups'
	])

YearDecodeDict = dict([
	(0,2000),
	(1,2001),
	(2,2002),
	(3,2003),
	(4,2004),
	(5,2005),
	(6,2006),
	(7,2007),
	(8,2008),
	(9,2009),
	(10,2010),
	(11,2011),
	(12,2012),
	(13,2013),
	(14,2014),
	(15,2015),
	(16,2016),
	(17,2017),
	(18,2018),
	(19,2019),
	(20,2020),
	(40,1940),
	(41,1941),
	(42,1942),
	(43,1943),
	(44,1944),
	(45,1945),
	(46,1946),
	(47,1947),
	(48,1948),
	(49,1949),
	(50,1950),
	(51,1951),
	(52,1952),
	(53,1953),
	(54,1954),
	(55,1955),
	(56,1956),
	(57,1957),
	(58,1958),
	(59,1959),
	(60,1960),
	(61,1961),
	(62,1962),
	(63,1963),
	(64,1964),
	(65,1965),
	(66,1966),
	(67,1967),
	(68,1968),
	(69,1969),
	(70,1970),
	(71,1971),
	(72,1972),
	(73,1973),
	(74,1974),
	(75,1975),
	(76,1976),
	(77,1977),
	(78,1978),
	(79,1979),
	(80,1980),
	(81,1981),
	(82,1982),
	(83,1983),
	(84,1984),
	(85,1985),
	(86,1986),
	(87,1987),
	(88,1988),
	(89,1989),
	(90,1990),
	(91,1991),
	(92,1992),
	(93,1993),
	(94,1994),
	(95,1995),
	(96,1996),
	(97,1997),
	(98,1998),
	(99,1999)
	])

USStatesDict = {
	'AK':'Alaska',
	'AL':'Alabama',
	'AR':'Arkansas',
	'AS':'American Samoa',
	'AZ':'Arizona',
	'CA':'California',
	'CO':'Colorado',
	'CT':'Connecticut',
	'DC':'District of Columbia',
	'DE':'Delaware',
	'FL':'Florida',
	'GA':'Georgia',
	'GU':'Guam',
	'HI':'Hawaii',
	'IA':'Iowa',
	'ID':'Idaho',
	'IL':'Illinois',
	'IN':'Indiana',
	'KS':'Kansas',
	'KY':'Kentucky',
	'LA':'Louisiana',
	'MA':'Massachusetts',
	'MD':'Maryland',
	'ME':'Maine',
	'MI':'Michigan',
	'MN':'Minnesota',
	'MO':'Missouri',
	'MP':'Northern Mariana Islands',
	'MS':'Mississippi',
	'MT':'Montana',
	'NA':'National',
	'NC':'North Carolina',
	'ND':'North Dakota',
	'NE':'Nebraska',
	'NH':'New Hampshire',
	'NJ':'New Jersey',
	'NM':'New Mexico',
	'NV':'Nevada',
	'NY':'New York',
	'OH':'Ohio',
	'OK':'Oklahoma',
	'OR':'Oregon',
	'PA':'Pennsylvania',
	'PR':'Puerto Rico',
	'RI':'Rhode Island',
	'SC':'South Carolina',
	'SD':'South Dakota',
	'TN':'Tennessee',
	'TX':'Texas',
	'UT':'Utah',
	'VA':'Virginia',
	'VI':'Virgin Islands',
	'VT':'Vermont',
	'WA':'Washington',
	'WI':'Wisconsin',
	'WV':'West Virginia',
	'WY':'Wyoming'
	}

CommonHispLastNameList = set([
	'Abad',
	'Abarca',
	'Abeyta',
	'Abrego',
	'Abreu',
	'Abril',
	'Abundis',
	'Aburto',
	'Acevedo',
	'Aceves',
	'Acosta',
	'Acuna',
	'Adame',
	'Adames',
	'Adorno',
	'Agosto',
	'Aguado',
	'Aguayo',
	'Agudelo',
	'Aguero',
	'Aguiar',
	'Aguila',
	'Aguilar',
	'Aguilera',
	'Aguillon',
	'Aguinaga',
	'Aguirre',
	'Agustin',
	'Ahumada',
	'Aispuro',
	'Alamillo',
	'Alamo',
	'Alaniz',
	'Alarcon',
	'Alas',
	'Alatorre',
	'Alba',
	'Albarado',
	'Albarran',
	'Alberto',
	'Albino',
	'Alcala',
	'Alcantar',
	'Alcantara',
	'Alcaraz',
	'Alcazar',
	'Alcocer',
	'Alcorta',
	'Aldaco',
	'Aldana',
	'Aldape',
	'Alderete',
	'Aldrete',
	'Alegria',
	'Alejandre',
	'Alejandro',
	'Alejo',
	'Alejos',
	'Aleman',
	'Alfaro',
	'Alfonso',
	'Algarin',
	'Alicea',
	'Almaguer',
	'Almanza',
	'Almanzar',
	'Almaraz',
	'Almazan',
	'Almeida',
	'Almendarez',
	'Almodovar',
	'Almonte',
	'Alonso',
	'Alonzo',
	'Altamirano',
	'Alva',
	'Alvarado',
	'Alvardo',
	'Alvarenga',
	'Alvares',
	'Alvarez',
	'Alvear',
	'Alvidrez',
	'Alzate',
	'Amado',
	'Amador',
	'Amaro',
	'Amaya',
	'Ambriz',
	'Amezcua',
	'Amezquita',
	'Anaya',
	'Anchondo',
	'Andino',
	'Andrade',
	'Andres',
	'Andujar',
	'Angel',
	'Angeles',
	'Anguiano',
	'Angulo',
	'Antonio',
	'Antunez',
	'Anzaldua',
	'Aparicio',
	'Apodaca',
	'Aponte',
	'Aquino',
	'Aragon',
	'Araiza',
	'Arambula',
	'Arana',
	'Aranda',
	'Arango',
	'Araujo',
	'Arauz',
	'Araya',
	'Arboleda',
	'Arce',
	'Arceo',
	'Archuleta',
	'Arciniega',
	'Arcos',
	'Ardon',
	'Arechiga',
	'Arellanes',
	'Arellano',
	'Arenas',
	'Arevalo',
	'Arguelles',
	'Arguello',
	'Argueta',
	'Arias',
	'Arispe',
	'Ariza',
	'Arizmendi',
	'Armas',
	'Armendariz',
	'Armenta',
	'Armijo',
	'Arocho',
	'Arredondo',
	'Arreguin',
	'Arreola',
	'Arriaga',
	'Arrieta',
	'Arriola',
	'Arroyo',
	'Arteaga',
	'Arvizu',
	'Arzate',
	'Arzola',
	'Ascencio',
	'Asencio',
	'Astorga',
	'Astudillo',
	'Atencio',
	'Atilano',
	'Atkinson',
	'Avalos',
	'Avelar',
	'Avendano',
	'Avila',
	'Aviles',
	'Avilez',
	'Avina',
	'Avitia',
	'Ayala',
	'Ayon',
	'Baca',
	'Badillo',
	'Baez',
	'Baeza',
	'Bahena',
	'Bailon',
	'Balbuena',
	'Balcazar',
	'Balderas',
	'Balderrama',
	'Ballesteros',
	'Baltazar',
	'Banda',
	'Banegas',
	'Banos',
	'Banuelos',
	'Barahona',
	'Barajas',
	'Barba',
	'Barbosa',
	'Barboza',
	'Barcenas',
	'Barcia',
	'Barela',
	'Bargas',
	'Barillas',
	'Barragan',
	'Barranco',
	'Barraza',
	'Barrera',
	'Barreras',
	'Barreto',
	'Barrientes',
	'Barrientos',
	'Barriga',
	'Barrios',
	'Barros',
	'Barroso',
	'Barton',
	'Basquez',
	'Basurto',
	'Batista',
	'Batres',
	'Bautista',
	'Bazan',
	'Beas',
	'Becerra',
	'Becerril',
	'Bedolla',
	'Bedoya',
	'Bejar',
	'Bejarano',
	'Bello',
	'Beltran',
	'Benavides',
	'Benavidez',
	'Bencomo',
	'Benites',
	'Benitez',
	'Berlanga',
	'Bermea',
	'Bermejo',
	'Bermudez',
	'Bernabe',
	'Bernal',
	'Berrios',
	'Berumen',
	'Betances',
	'Betancourt',
	'Bianco',
	'Blancas',
	'Blanco',
	'Blas',
	'Blea',
	'Bobadilla',
	'Bocanegra',
	'Bojorquez',
	'Bolanos',
	'Bolivar',
	'Bonilla',
	'Borges',
	'Borja',
	'Borjas',
	'Borrego',
	'Borrero',
	'Borunda',
	'Bosquez',
	'Botello',
	'Bracamonte',
	'Bracamontes',
	'Bracero',
	'Brambila',
	'Bravo',
	'Brenes',
	'Briceno',
	'Briones',
	'Briseno',
	'Brito',
	'Brizuela',
	'Bruno',
	'Bucio',
	'Buendia',
	'Bueno',
	'Buenrostro',
	'Buentello',
	'Bugarin',
	'Buitrago',
	'Buitron',
	'Burciaga',
	'Burgos',
	'Bustamante',
	'Bustillo',
	'Bustillos',
	'Bustos',
	'Caba',
	'Caballero',
	'Caban',
	'Cabanas',
	'Cabello',
	'Cabezas',
	'Cabral',
	'Cabrales',
	'Cabrera',
	'Caceres',
	'Cadena',
	'Cadenas',
	'Caicedo',
	'Caldera',
	'Calderon',
	'Calero',
	'Calixto',
	'Calle',
	'Callejas',
	'Calles',
	'Calvillo',
	'Calvo',
	'Calzada',
	'Camacho',
	'Camarena',
	'Camargo',
	'Camarillo',
	'Camilo',
	'Campa',
	'Campo',
	'Campos',
	'Campuzano',
	'Canales',
	'Canas',
	'Cancel',
	'Canchola',
	'Cancino',
	'Candelaria',
	'Candelario',
	'Canela',
	'Canez',
	'Canizales',
	'Cano',
	'Cantu',
	'Capetillo',
	'Caraballo',
	'Caraveo',
	'Carbajal',
	'Carballo',
	'Carbonell',
	'Carcamo',
	'Cardenas',
	'Cardona',
	'Cardoso',
	'Cardoza',
	'Cardozo',
	'Carias',
	'Carillo',
	'Carino',
	'Carlos',
	'Carmona',
	'Caro',
	'Carpio',
	'Carranza',
	'Carrasco',
	'Carrasquillo',
	'Carreno',
	'Carreon',
	'Carrera',
	'Carreras',
	'Carrero',
	'Carrillo',
	'Carrion',
	'Carrizales',
	'Cartagena',
	'Carvajal',
	'Casado',
	'Casares',
	'Casarez',
	'Casas',
	'Casiano',
	'Casillas',
	'Castaneda',
	'Castano',
	'Castanon',
	'Castelan',
	'Castellano',
	'Castellanos',
	'Castellon',
	'Castilla',
	'Castilleja',
	'Castillo',
	'Castorena',
	'Castrejon',
	'Castro',
	'Castruita',
	'Catalan',
	'Catano',
	'Caudillo',
	'Cavazos',
	'Cazares',
	'Cazarez',
	'Ceballos',
	'Cedeno',
	'Cedillo',
	'Ceja',
	'Celaya',
	'Celis',
	'Cendejas',
	'Ceniceros',
	'Centeno',
	'Cepeda',
	'Cerda',
	'Cerna',
	'Ceron',
	'Cervantes',
	'Cervantez',
	'Cervera',
	'Cespedes',
	'Cevallos',
	'Chacon',
	'Chaidez',
	'Chairez',
	'Chamorro',
	'Chapa',
	'Chaparro',
	'Chavarin',
	'Chavarria',
	'Chaves',
	'Chavez',
	'Chavira',
	'Chicas',
	'Chico',
	'Chinchilla',
	'Christian',
	'Cifuentes',
	'Cintron',
	'Cisneros',
	'Claros',
	'Claudio',
	'Clemente',
	'Cobian',
	'Cobos',
	'Coello',
	'Colindres',
	'Collado',
	'Collazo',
	'Colmenares',
	'Colmenero',
	'Colon',
	'Colorado',
	'Colunga',
	'Compean',
	'Concepcion',
	'Concha',
	'Conde',
	'Contreras',
	'Corchado',
	'Cordero',
	'Cordoba',
	'Cordova',
	'Corea',
	'Coreas',
	'Coria',
	'Cornejo',
	'Cornelio',
	'Corona',
	'Coronado',
	'Coronel',
	'Corpus',
	'Corral',
	'Corrales',
	'Correa',
	'Cortes',
	'Cortez',
	'Cortina',
	'Cortinas',
	'Cosio',
	'Cosme',
	'Costa',
	'Costilla',
	'Cota',
	'Coto',
	'Cotto',
	'Covarrubias',
	'Crespin',
	'Crespo',
	'Cruz',
	'Cuadra',
	'Cuellar',
	'Cuenca',
	'Cuesta',
	'Cueto',
	'Cueva',
	'Cuevas',
	'Curiel',
	'Dasilva',
	'Davalos',
	'Davila',
	'Dealba',
	'Deanda',
	'Dearmas',
	'Dedios',
	'Deharo',
	'Deherrera',
	'Dehoyos',
	'Dejesus',
	'Delacerda',
	'Delacruz',
	'Delafuente',
	'Delagarza',
	'Delamora',
	'Delangel',
	'Delao',
	'Delapaz',
	'Delapena',
	'Delariva',
	'Delarosa',
	'Delatorre',
	'Delavega',
	'Delbosque',
	'Delcastillo',
	'Delcid',
	'Deleon',
	'Delgadillo',
	'Delgado',
	'Deloera',
	'Delosreyes',
	'Delossantos',
	'Delreal',
	'Delrio',
	'Delrosario',
	'Deltoro',
	'Deluna',
	'Delvalle',
	'Depaz',
	'Deras',
	'Desantiago',
	'Dial',
	'Dias',
	'Diaz',
	'Diazdeleon',
	'Diego',
	'Diez',
	'Dimas',
	'Disla',
	'Domingo',
	'Domingues',
	'Dominguez',
	'Dominquez',
	'Dones',
	'Donis',
	'Dorado',
	'Dorantes',
	'Duarte',
	'Duenas',
	'Duque',
	'Duran',
	'Durazo',
	'Duron',
	'Echavarria',
	'Echevarria',
	'Echeverria',
	'Elias',
	'Elizalde',
	'Elizondo',
	'Encarnacion',
	'Encinas',
	'Enciso',
	'Enriquez',
	'Erazo',
	'Escalante',
	'Escalera',
	'Escalona',
	'Escamilla',
	'Escandon',
	'Escarcega',
	'Escareno',
	'Escobar',
	'Escobedo',
	'Escoto',
	'Escudero',
	'Escutia',
	'Espada',
	'Espana',
	'Esparza',
	'Espinal',
	'Espindola',
	'Espino',
	'Espinosa',
	'Espinoza',
	'Espitia',
	'Esqueda',
	'Esquer',
	'Esquibel',
	'Esquivel',
	'Esteban',
	'Esteves',
	'Estevez',
	'Estrada',
	'Estrella',
	'Evangelista',
	'Fabela',
	'Fabian',
	'Fajardo',
	'Farias',
	'Favela',
	'Faz',
	'Federico',
	'Felan',
	'Feliciano',
	'Felipe',
	'Felix',
	'Feliz',
	'Fernandes',
	'Fernandez',
	'Ferreira',
	'Ferrer',
	'Fierro',
	'Fierros',
	'Figueredo',
	'Figueroa',
	'Fimbres',
	'Flores',
	'Florez',
	'Fonseca',
	'Fontanez',
	'Fraga',
	'Fragoso',
	'Fraire',
	'Francisco',
	'Franco',
	'Frausto',
	'Fregoso',
	'Freire',
	'Fresquez',
	'Frias',
	'Fuentes',
	'Fuentez',
	'Fuerte',
	'Funes',
	'Gabaldon',
	'Gabriel',
	'Gaeta',
	'Gaitan',
	'Galan',
	'Galarza',
	'Galaviz',
	'Galdamez',
	'Galeana',
	'Galeano',
	'Galicia',
	'Galindo',
	'Gallardo',
	'Gallego',
	'Gallegos',
	'Galvan',
	'Galvez',
	'Gama',
	'Gamboa',
	'Gamez',
	'Gamino',
	'Gandara',
	'Garces',
	'Garcia',
	'Gardea',
	'Garduno',
	'Garibay',
	'Garica',
	'Garnica',
	'Garrido',
	'Garza',
	'Garzon',
	'Gasca',
	'Gaspar',
	'Gastelum',
	'Gatica',
	'Gauna',
	'Gaxiola',
	'Gaytan',
	'Genao',
	'Gerardo',
	'Gerena',
	'Gimenez',
	'Giraldo',
	'Giron',
	'Gloria',
	'Godina',
	'Godines',
	'Godinez',
	'Godoy',
	'Gomes',
	'Gomez',
	'Gongora',
	'Gonsales',
	'Gonsalez',
	'Gonzales',
	'Gonzalez',
	'Gordillo',
	'Goto',
	'Govea',
	'Gracia',
	'Graciano',
	'Grado',
	'Grajales',
	'Grajeda',
	'Granado',
	'Granados',
	'Granda',
	'Grande',
	'Granillo',
	'Griego',
	'Grijalva',
	'Grimaldo',
	'Grullon',
	'Guadalupe',
	'Guadarrama',
	'Guajardo',
	'Guardado',
	'Guardiola',
	'Gudino',
	'Guel',
	'Guerra',
	'Guerrero',
	'Guevara',
	'Guillermo',
	'Guizar',
	'Gurrola',
	'Gutierres',
	'Gutierrez',
	'Guzman',
	'Henao',
	'Henriquez',
	'Heredia',
	'Hermosillo',
	'Hernandes',
	'Hernandez',
	'Herrera',
	'Hidalgo',
	'Higareda',
	'Higuera',
	'Hilario',
	'Hinojos',
	'Hinojosa',
	'Horta',
	'Hoyos',
	'Huerta',
	'Huertas',
	'Huezo',
	'Huizar',
	'Hurtado',
	'Ibanez',
	'Ibarra',
	'Iglesias',
	'Infante',
	'Iniguez',
	'Iraheta',
	'Irizarry',
	'Islas',
	'Izaguirre',
	'Izquierdo',
	'Jacinto',
	'Jacobo',
	'Jacome',
	'Jacquez',
	'Jaime',
	'Jaimes',
	'Jaquez',
	'Jara',
	'Jaramillo',
	'Jarquin',
	'Jasso',
	'Jauregui',
	'Javier',
	'Jerez',
	'Jimenes',
	'Jimenez',
	'Jiminez',
	'Jiron',
	'Jorge',
	'Jose',
	'Joya',
	'Juan',
	'Juarez',
	'Jurado',
	'Jusino',
	'Justiniano',
	'Laboy',
	'Lacayo',
	'Lagos',
	'Laguna',
	'Lagunas',
	'Lainez',
	'Lamas',
	'Landa',
	'Landaverde',
	'Landeros',
	'Lantigua',
	'Lara',
	'Lares',
	'Larios',
	'Latorre',
	'Laureano',
	'Lazaro',
	'Lazcano',
	'Lazo',
	'Leanos',
	'Lechuga',
	'Ledesma',
	'Ledezma',
	'Leija',
	'Leiva',
	'Lema',
	'Lemos',
	'Lemus',
	'Leon',
	'Leos',
	'Lepe',
	'Lerma',
	'Levario',
	'Leyba',
	'Leyva',
	'Lezama',
	'Licea',
	'Licon',
	'Lima',
	'Limas',
	'Limon',
	'Linares',
	'Lira',
	'Liriano',
	'Lizama',
	'Lizarraga',
	'Llamas',
	'Llanes',
	'Llanos',
	'Llerena',
	'Loaiza',
	'Lobato',
	'Lobo',
	'Loera',
	'Lomas',
	'Lomeli',
	'Londono',
	'Longoria',
	'Lopes',
	'Lopez',
	'Lora',
	'Loredo',
	'Lorenzana',
	'Lorenzo',
	'Losoya',
	'Lovato',
	'Loya',
	'Loyola',
	'Loza',
	'Lozada',
	'Lozano',
	'Lozoya',
	'Lucas',
	'Lucatero',
	'Lucero',
	'Lucio',
	'Luera',
	'Luevano',
	'Lugo',
	'Luis',
	'Lujan',
	'Lujano',
	'Luna',
	'Lupercio',
	'Luque',
	'Macedo',
	'Machado',
	'Machuca',
	'Macias',
	'Maciel',
	'Madera',
	'Madero',
	'Madrid',
	'Madrigal',
	'Maestas',
	'Maez',
	'Magallanes',
	'Magallon',
	'Magana',
	'Magdaleno',
	'Maisonet',
	'Majano',
	'Malagon',
	'Malave',
	'Maldonado',
	'Mancera',
	'Mancha',
	'Mancia',
	'Mancilla',
	'Mancillas',
	'Mandujano',
	'Mangual',
	'Manjarrez',
	'Manrique',
	'Manriquez',
	'Mantilla',
	'Manuel',
	'Manzanares',
	'Manzano',
	'Manzo',
	'Maravilla',
	'Marcano',
	'Marcial',
	'Marcos',
	'Mares',
	'Marez',
	'Maria',
	'Marinez',
	'Marino',
	'Mariscal',
	'Marmol',
	'Marmolejo',
	'Marques',
	'Marquez',
	'Marrero',
	'Marroquin',
	'Marrufo',
	'Marte',
	'Martin',
	'Martines',
	'Martinez',
	'Mascarenas',
	'Mascorro',
	'Mata',
	'Matamoros',
	'Mateo',
	'Matias',
	'Matos',
	'Matta',
	'Matus',
	'Matute',
	'Mauricio',
	'Maya',
	'Mayo',
	'Mayorga',
	'Mazariegos',
	'Medellin',
	'Mederos',
	'Medina',
	'Medrano',
	'Mejia',
	'Mejias',
	'Melara',
	'Melchor',
	'Melendez',
	'Melendrez',
	'Melgar',
	'Melgoza',
	'Melo',
	'Membreno',
	'Mena',
	'Menchaca',
	'Mendes',
	'Mendez',
	'Mendieta',
	'Mendiola',
	'Mendivil',
	'Mendosa',
	'Mendoza',
	'Menendez',
	'Meneses',
	'Menjivar',
	'Mera',
	'Meraz',
	'Mercado',
	'Merced',
	'Mercedes',
	'Merida',
	'Merino',
	'Mesa',
	'Mestas',
	'Meza',
	'Miguel',
	'Mijares',
	'Minaya',
	'Minjarez',
	'Mirabal',
	'Miramontes',
	'Mireles',
	'Moctezuma',
	'Mojica',
	'Molina',
	'Molinar',
	'Monarrez',
	'Moncada',
	'Moncayo',
	'Mondragon',
	'Monge',
	'Monroy',
	'Monsivais',
	'Montalvo',
	'Montanez',
	'Montano',
	'Montejano',
	'Montelongo',
	'Montemayor',
	'Montenegro',
	'Montero',
	'Monterrosa',
	'Monterroso',
	'Montes',
	'Montesdeoca',
	'Montesinos',
	'Montez',
	'Montgomery',
	'Montiel',
	'Montijo',
	'Montoya',
	'Monzon',
	'Mora',
	'Morado',
	'Moraga',
	'Morales',
	'Moralez',
	'Moran',
	'Moreira',
	'Morejon',
	'Morel',
	'Morelos',
	'Moreno',
	'Morillo',
	'Morin',
	'Morones',
	'Moscoso',
	'Mosqueda',
	'Mosquera',
	'Mota',
	'Moya',
	'Mungia',
	'Munguia',
	'Muniz',
	'Munos',
	'Munoz',
	'Murcia',
	'Murguia',
	'Murillo',
	'Muro',
	'Murrieta',
	'Najar',
	'Najera',
	'Nanez',
	'Napoles',
	'Naranjo',
	'Narvaez',
	'Natal',
	'Natividad',
	'Nava',
	'Navarrete',
	'Navarrette',
	'Navarro',
	'Navas',
	'Nazario',
	'Negrete',
	'Negron',
	'Neira',
	'Neri',
	'Nevarez',
	'Nieto',
	'Nieves',
	'Nino',
	'Noguera',
	'Nolasco',
	'Noriega',
	'Nova',
	'Novoa',
	'Noyola',
	'Nunes',
	'Nunez',
	'Nuno',
	'Obando',
	'Obregon',
	'Ocampo',
	'Ocana',
	'Ocasio',
	'Oceguera',
	'Ochoa',
	'Ocon',
	'Ojeda',
	'Olague',
	'Olea',
	'Olguin',
	'Oliva',
	'Olivares',
	'Olivarez',
	'Olivas',
	'Olivera',
	'Oliveras',
	'Oliveros',
	'Olivo',
	'Olmeda',
	'Olmedo',
	'Olmos',
	'Olvera',
	'Onofre',
	'Ontiveros',
	'Oquendo',
	'Orantes',
	'Ordaz',
	'Ordonez',
	'Orduna',
	'Orduno',
	'Orellana',
	'Ornelas',
	'Orona',
	'Oropeza',
	'Orosco',
	'Orozco',
	'Orta',
	'Ortega',
	'Ortegon',
	'Ortez',
	'Ortis',
	'Ortiz',
	'Oseguera',
	'Osorio',
	'Osornio',
	'Ospina',
	'Osuna',
	'Otero',
	'Ovalle',
	'Oviedo',
	'Oyola',
	'Ozuna',
	'Pablo',
	'Pabon',
	'Pacheco',
	'Padilla',
	'Padron',
	'Paez',
	'Paiz',
	'Palacio',
	'Palacios',
	'Palencia',
	'Palma',
	'Palomares',
	'Palomino',
	'Palomo',
	'Palos',
	'Pando',
	'Paniagua',
	'Pantaleon',
	'Pantoja',
	'Parada',
	'Paramo',
	'Pardo',
	'Paredes',
	'Parga',
	'Parra',
	'Parrilla',
	'Partida',
	'Pascual',
	'Pasillas',
	'Pastor',
	'Pastrana',
	'Patino',
	'Patlan',
	'Paulino',
	'Pavon',
	'Payan',
	'Paz',
	'Pecina',
	'Pedraza',
	'Pedro',
	'Pedroza',
	'Peguero',
	'Pelaez',
	'Pelayo',
	'Pena',
	'Penaloza',
	'Penate',
	'Pera',
	'Perales',
	'Peralez',
	'Peralta',
	'Peraza',
	'Perdomo',
	'Perea',
	'Pereda',
	'Pereira',
	'Peres',
	'Pereyra',
	'Perez',
	'Pesina',
	'Picazo',
	'Pichardo',
	'Piedra',
	'Pimentel',
	'Pina',
	'Pinales',
	'Pineda',
	'Pinedo',
	'Pineiro',
	'Pinero',
	'Pino',
	'Pinon',
	'Pinto',
	'Pintor',
	'Pinzon',
	'Pizana',
	'Pizano',
	'Pizarro',
	'Placencia',
	'Plascencia',
	'Plasencia',
	'Plata',
	'Plaza',
	'Polanco',
	'Polo',
	'Pompa',
	'Ponce',
	'Porras',
	'Portillo',
	'Posada',
	'Posadas',
	'Pozo',
	'Prado',
	'Preciado',
	'Prieto',
	'Provencio',
	'Pruneda',
	'Puebla',
	'Puente',
	'Puentes',
	'Puga',
	'Puig',
	'Pulido',
	'Quesada',
	'Quevedo',
	'Quezada',
	'Quijada',
	'Quijano',
	'Quinones',
	'Quinonez',
	'Quintana',
	'Quintanar',
	'Quintanilla',
	'Quintero',
	'Quinteros',
	'Quiroga',
	'Quiros',
	'Quiroz',
	'Rabago',
	'Rael',
	'Rafael',
	'Ramires',
	'Ramirez',
	'Ramon',
	'Ramos',
	'Rangel',
	'Rascon',
	'Raya',
	'Raygoza',
	'Raymundo',
	'Rayo',
	'Razo',
	'Rebollar',
	'Rebolledo',
	'Recinos',
	'Recio',
	'Redondo',
	'Regalado',
	'Reina',
	'Reinoso',
	'Rendon',
	'Rentas',
	'Renteria',
	'Resendez',
	'Resendiz',
	'Resto',
	'Restrepo',
	'Retana',
	'Reveles',
	'Revilla',
	'Reyes',
	'Reyna',
	'Reynaga',
	'Reynosa',
	'Reynoso',
	'Reza',
	'Ricardo',
	'Rico',
	'Rincon',
	'Riojas',
	'Rios',
	'Rivas',
	'Rivera',
	'Rivero',
	'Rizo',
	'Roa',
	'Robledo',
	'Robles',
	'Roca',
	'Rocha',
	'Roche',
	'Rodarte',
	'Rodas',
	'Rodela',
	'Rodgers',
	'Rodriges',
	'Rodrigues',
	'Rodriguez',
	'Rodriquez',
	'Rogel',
	'Rojas',
	'Rojo',
	'Roldan',
	'Rolon',
	'Romano',
	'Romero',
	'Romo',
	'Rondon',
	'Ronquillo',
	'Roque',
	'Rosa',
	'Rosado',
	'Rosales',
	'Rosalez',
	'Rosario',
	'Rosas',
	'Roybal',
	'Ruano',
	'Rubalcaba',
	'Rubalcava',
	'Rubio',
	'Rueda',
	'Ruelas',
	'Ruiz',
	'Ruvalcaba',
	'Saavedra',
	'Sabala',
	'Saenz',
	'Saez',
	'Sagastume',
	'Sahagun',
	'Sainz',
	'Saiz',
	'Salamanca',
	'Salas',
	'Salazar',
	'Salcedo',
	'Salcido',
	'Saldana',
	'Saldivar',
	'Salgado',
	'Salguero',
	'Salinas',
	'Salmeron',
	'Salomon',
	'Salvador',
	'Salvatierra',
	'Samaniego',
	'Samano',
	'Samayoa',
	'Sambrano',
	'Samora',
	'Sanabria',
	'Sanches',
	'Sanchez',
	'Sanders',
	'Sandoval',
	'Sanjuan',
	'Sanmartin',
	'Sanmiguel',
	'Santacruz',
	'Santamaria',
	'Santana',
	'Santiago',
	'Santibanez',
	'Santillan',
	'Santistevan',
	'Santizo',
	'Santos',
	'Santoyo',
	'Sarabia',
	'Saravia',
	'Sarmiento',
	'Sauceda',
	'Saucedo',
	'Savala',
	'Sebastian',
	'Seda',
	'Sedano',
	'Sedillo',
	'Segarra',
	'Segovia',
	'Segundo',
	'Segura',
	'Sena',
	'Sepeda',
	'Sepulveda',
	'Sequeira',
	'Serna',
	'Serra',
	'Serrano',
	'Serrato',
	'Servantes',
	'Servin',
	'Sevilla',
	'Sierra',
	'Sifuentes',
	'Sigala',
	'Silva',
	'Silvas',
	'Silverio',
	'Silvestre',
	'Simental',
	'Sisneros',
	'Solano',
	'Solares',
	'Soler',
	'Solis',
	'Soliz',
	'Solorio',
	'Solorzano',
	'Soltero',
	'Soria',
	'Soriano',
	'Sorto',
	'Sosa',
	'Sotelo',
	'Soto',
	'Sotomayor',
	'Souza',
	'Soza',
	'Suarez',
	'Suazo',
	'Suniga',
	'Sustaita',
	'Tabares',
	'Tafolla',
	'Tafoya',
	'Talamantes',
	'Talamantez',
	'Talavera',
	'Tamayo',
	'Tamez',
	'Tapia',
	'Tarango',
	'Tavares',
	'Tavarez',
	'Tavera',
	'Taveras',
	'Tejada',
	'Tejeda',
	'Telles',
	'Tellez',
	'Tello',
	'Tena',
	'Tenorio',
	'Teran',
	'Tercero',
	'Terrazas',
	'Terrones',
	'Tijerina',
	'Tinajero',
	'Tineo',
	'Tinoco',
	'Tirado',
	'Tiscareno',
	'Tobar',
	'Tolentino',
	'Tomas',
	'Topete',
	'Toribio',
	'Toro',
	'Torres',
	'Torrez',
	'Toscano',
	'Tostado',
	'Tovar',
	'Trejo',
	'Trevino',
	'Trevizo',
	'Triana',
	'Trinidad',
	'Troche',
	'Troncoso',
	'Trujillo',
	'Turcios',
	'Ugalde',
	'Ugarte',
	'Ulibarri',
	'Ulloa',
	'Umana',
	'Umanzor',
	'Urbano',
	'Urbina',
	'Urena',
	'Uresti',
	'Uriarte',
	'Urias',
	'Uribe',
	'Uriostegui',
	'Urquiza',
	'Urrea',
	'Urzua',
	'Vaca',
	'Valadez',
	'Valderrama',
	'Valdes',
	'Valdez',
	'Valdivia',
	'Valdovinos',
	'Valencia',
	'Valentin',
	'Valenzuela',
	'Valera',
	'Valerio',
	'Valero',
	'Valiente',
	'Valladares',
	'Valle',
	'Vallejo',
	'Vallejos',
	'Valles',
	'Valtierra',
	'Valverde',
	'Vanegas',
	'Vaquera',
	'Vara',
	'Varela',
	'Vargas',
	'Vasques',
	'Vasquez',
	'Vazquez',
	'Vega',
	'Vela',
	'Velarde',
	'Velasco',
	'Velasquez',
	'Velazco',
	'Velazquez',
	'Velez',
	'Veliz',
	'Veloz',
	'Vences',
	'Venegas',
	'Ventura',
	'Vera',
	'Veras',
	'Verdin',
	'Verdugo',
	'Verduzco',
	'Vergara',
	'Vicente',
	'Victoria',
	'Vidal',
	'Vidales',
	'Vidaurri',
	'Vides',
	'Vidrio',
	'Viera',
	'Vieyra',
	'Vila',
	'Villa',
	'Villafana',
	'Villafane',
	'Villafuerte',
	'Villagomez',
	'Villagran',
	'Villagrana',
	'Villalba',
	'Villalobos',
	'Villalon',
	'Villalpando',
	'Villalta',
	'Villanueva',
	'Villar',
	'Villareal',
	'Villarreal',
	'Villarruel',
	'Villasana',
	'Villasenor',
	'Villatoro',
	'Villavicencio',
	'Villeda',
	'Villegas',
	'Villela',
	'Villicana',
	'Viramontes',
	'Vital',
	'Vivanco',
	'Vivar',
	'Vivas',
	'Viveros',
	'Vizcaino',
	'Vizcarra',
	'Yanes',
	'Yanez',
	'Ybarra',
	'Yepez',
	'Yzaguirre',
	'Zabala',
	'Zacarias',
	'Zaldivar',
	'Zamarripa',
	'Zamarron',
	'Zambrana',
	'Zambrano',
	'Zamora',
	'Zamorano',
	'Zamudio',
	'Zapata',
	'Zapien',
	'Zaragoza',
	'Zarate',
	'Zarco',
	'Zavala',
	'Zavaleta',
	'Zayas',
	'Zazueta',
	'Zelaya',
	'Zeledon',
	'Zendejas',
	'Zepeda',
	'Zermeno',
	'Zertuche',
	'Zorrilla',
	'Zubia',
	'Zuniga',
	'Zurita'
	])
