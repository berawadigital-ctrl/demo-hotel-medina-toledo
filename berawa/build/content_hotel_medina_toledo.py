# Contenido de la demo Hotel Medina (Toledo) (es/ca/en/fr). Hechos de hotelmedina.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Individual','Doble de dos camas','Doble de cama de matrimonio'],
'ca':['Individual','Doble de dos llits','Doble de llit de matrimoni'],
'en':['Single','Double with two beds','Double with a double bed'],
'fr':['Simple','Double à deux lits','Double à lit double']}
RD={
'es':['Habitación de 12 m² con aire acondicionado, calefacción, wifi gratuito y TV de pantalla plana.','Habitación de 14 m² con dos camas individuales, aire acondicionado, calefacción y wifi gratuito. Algunas tienen balcón.','Habitación de 14 m² con cama de 135 o 150 cm, aire acondicionado, calefacción y wifi gratuito. Algunas tienen balcón.'],
'ca':['Habitació de 12 m² amb aire condicionat, calefacció, wifi gratuït i TV de pantalla plana.','Habitació de 14 m² amb dos llits individuals, aire condicionat, calefacció i wifi gratuït. Algunes tenen balcó.','Habitació de 14 m² amb llit de 135 o 150 cm, aire condicionat, calefacció i wifi gratuït. Algunes tenen balcó.'],
'en':['12 m² room with air conditioning, heating, free wifi and a flat-screen TV.','14 m² room with two single beds, air conditioning, heating and free wifi. Some have a balcony.','14 m² room with a 135 or 150 cm bed, air conditioning, heating and free wifi. Some have a balcony.'],
'fr':['Chambre de 12 m² avec climatisation, chauffage, wifi gratuit et TV à écran plat.','Chambre de 14 m² avec deux lits simples, climatisation, chauffage et wifi gratuit. Certaines ont un balcon.','Chambre de 14 m² avec lit de 135 ou 150 cm, climatisation, chauffage et wifi gratuit. Certaines ont un balcon.']}
ART={
'hero':('skyline',9501,['#3b4a6b','#e9915a','#fbd8a1','#38476a','#2a3857','#1a2336']),
'intro':('arches',9502,['#f0e1c6','#dcbd8c','#b0693a','#7a4e36','#53382a']),
'r1':('arches',9511,['#efe0c4','#dbb988','#a95f33','#73482f','#4f3526']),
'r2':('columns',9512,['#ede0c8','#f4e8d0','#b5703c','#85593d','#573a2a']),
'r3':('hills',9513,['#e8e2cd','#f3e3bf','#f2c27f','#b3b88f','#8a9f7c','#5f7a64']),
'g1':('arches',9521,['#f1e2c7','#ddbf8f','#af6a38','#774d35','#523729']),
'g2':('skyline',9522,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('hills',9523,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g4':('columns',9524,['#eee1c8','#f5e9d3','#b46d3a','#88603f','#593c2b']),
'g5':('skyline',9525,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f']),
'g6':('arches',9526,['#f2e3c6','#dfc28e','#b0693a','#7a4f36','#563a2b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Medina · Hotel de tres estrellas en el casco histórico de Toledo',see_rooms='Ver habitaciones',hero_k='Toledo · Casco histórico',hero_t='Un hotel con aire toledano en el corazón de Toledo',hero_s='Hotel de tres estrellas a 150 metros de la Plaza de Zocodover, con terraza y vistas al casco histórico.',
 intro_t='Estilo rústico toledano con toques modernos',intro_p1='Hotel Medina combina el estilo rústico de una típica casa toledana con toques de vanguardia, junto a las escaleras mecánicas de acceso al casco histórico.',
 intro_p2='Tiene recepción 24 horas, wifi gratis y una terraza con vistas panorámicas. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['Hotel de tres estrellas','Terraza con vistas','Wifi gratis','Recepción 24 horas'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Terraza con vistas','Wifi gratis','Recepción 24 horas','Guardaequipaje','Habitación insonorizada','Caja fuerte','Limpieza diaria','Early check-in gratis según disponibilidad'],
 loc_p='Bajada de los Desamparados 2, 45003 Toledo, en el casco histórico.',
 chips=['¿Qué habitaciones tiene?','¿Hay terraza?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Medina · Hotel de tres estrelles al casc històric de Toledo',see_rooms='Veure habitacions',hero_k='Toledo · Casc històric',hero_t='Un hotel amb aire toledà al cor de Toledo',hero_s='Hotel de tres estrelles a 150 metres de la Plaça de Zocodover, amb terrassa i vistes al casc històric.',
 intro_t='Estil rústic toledà amb tocs moderns',intro_p1='Hotel Medina combina l\'estil rústic d\'una típica casa toledana amb tocs d\'avantguarda, al costat de les escales mecàniques d\'accés al casc històric.',
 intro_p2='Té recepció 24 hores, wifi gratuït i una terrassa amb vistes panoràmiques. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['Hotel de tres estrelles','Terrassa amb vistes','Wifi gratuït','Recepció 24 hores'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Terrassa amb vistes','Wifi gratuït','Recepció 24 hores','Guardaequipatges','Habitació insonoritzada','Caixa forta','Neteja diària','Early check-in gratuït segons disponibilitat'],
 loc_p='Bajada de los Desamparados 2, 45003 Toledo, al casc històric.',
 chips=['Quines habitacions té?','Hi ha terrassa?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Hotel Medina · Three-star hotel in the historic centre of Toledo',see_rooms='See the rooms',hero_k='Toledo · Historic centre',hero_t='A hotel with Toledo character in the heart of Toledo',hero_s='A three-star hotel 150 metres from Plaza de Zocodover, with a terrace and views of the historic centre.',
 intro_t='Rustic Toledo style with modern touches',intro_p1='Hotel Medina combines the rustic style of a typical Toledo house with avant-garde touches, next to the escalators up to the historic centre.',
 intro_p2='It has 24-hour reception, free wifi and a terrace with panoramic views. To book, contact the hotel by phone or email.',
 stats=['Three-star hotel','Terrace with views','Free wifi','24-hour reception'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Terrace with views','Free wifi','24-hour reception','Luggage storage','Soundproofed rooms','Safe','Daily cleaning','Early check-in free subject to availability'],
 loc_p='Bajada de los Desamparados 2, 45003 Toledo, in the historic centre.',
 chips=['What rooms does it have?','Is there a terrace?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel Medina · Hôtel trois étoiles dans le centre historique de Tolède',see_rooms='Voir les chambres',hero_k='Tolède · Centre historique',hero_t='Un hôtel au caractère tolédan au cœur de Tolède',hero_s='Hôtel trois étoiles à 150 mètres de la Plaza de Zocodover, avec terrasse et vue sur le centre historique.',
 intro_t='Style rustique tolédan avec touches modernes',intro_p1='Hotel Medina allie le style rustique d\'une maison tolédane typique à des touches d\'avant-garde, à côté des escaliers mécaniques menant au centre historique.',
 intro_p2='Il dispose d\'une réception 24 heures, du wifi gratuit et d\'une terrasse avec vue panoramique. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['Hôtel trois étoiles','Terrasse avec vue','Wifi gratuit','Réception 24 heures'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Terrasse avec vue','Wifi gratuit','Réception 24 heures','Consigne à bagages','Chambre insonorisée','Coffre-fort','Ménage quotidien','Early check-in gratuit selon disponibilité'],
 loc_p='Bajada de los Desamparados 2, 45003 Tolède, dans le centre historique.',
 chips=['Quelles chambres propose-t-il ?','Y a-t-il une terrasse ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='correo@hotelmedina.com')
D=dict(name='Hotel Medina',ac='#5b3a29',ac2='#a8582b',ac2_a11y='#8a3f17',book=BOOK,around=[],foot=FOOT,
 address='Bajada de los Desamparados 2 · 45003 Toledo',phones=['925 69 99 99'],emails=['correo@hotelmedina.com'],maps='Hotel Medina, Bajada de los Desamparados 2, Toledo',t=T)
META=dict(repo='demo-hotel-medina-toledo',name='Hotel Medina',legal_name='Sociedad de Autogestión de Hoteles Rurales, S.L.',registry_ids=['CIF B21493747'],
 url='https://www.hotelmedina.com/',domain='hotelmedina.com',municipality='Toledo',province='Toledo',sector='hotel de tres estrellas en el casco histórico',
 read_at='2026-10-29T05:14:00+01:00',created_at='2026-10-29T05:16:00+01:00',built_at='2026-10-29T05:17:00+01:00',audit_date='2026-10-29T05:16:00+01:00',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T05:07:04+01:00',url='https://www.google.com/maps/place/Hotel+Medina/@39.8617051,-4.021741,17z/data=!4m9!3m8!1s0xd6a0baf99fe65fb:0xb74473a1d7ccfd63!5m2!4m1!1i2!8m2!3d39.8617051!4d-4.021741!16s%2Fg%2F1hcb5j3wt'),
 book=dict(mode='mail',email='correo@hotelmedina.com',note='La web del negocio tiene su propio motor de reservas (boton Reservar) cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen?','K02'),('¿Hay terraza?','K03'),('¿Hay wifi y recepción 24 horas?','K04'),('¿A qué hora es el check-in?','K05'),('¿Hay habitaciones triples?','K06'),('¿Hay parking?','K07'),('¿Dónde está el hotel?','K08'),('¿Qué hay cerca del hotel?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Es accesible para silla de ruedas?',None),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10')],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen?','K02'),('Hi ha terrassa?','K03'),('Hi ha wifi i recepció 24 hores?','K04'),('A quina hora és el check-in?','K05'),('Hi ha habitacions triples?','K06'),('Hi ha pàrquing?','K07'),('On és l\'hotel?','K08'),('Què hi ha a prop de l\'hotel?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('És accessible amb cadira de rodes?',None),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10')],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there a terrace?','K03'),('Is there wifi and 24-hour reception?','K04'),('What time is check-in?','K05'),('Are there triple rooms?','K06'),('Is there parking?','K07'),('Where is the hotel?','K08'),('What is near the hotel?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('Is it wheelchair accessible?',None),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10')],
'fr':[('Quelles chambres propose-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il une terrasse ?','K03'),('Y a-t-il du wifi et une réception 24 heures ?','K04'),('À quelle heure est le check-in ?','K05'),('Y a-t-il des chambres triples ?','K06'),('Y a-t-il un parking ?','K07'),('Où est l\'hôtel ?','K08'),('Qu\'y a-t-il près de l\'hôtel ?','K09'),('Comment réserver ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Est-il accessible en fauteuil roulant ?',None),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10')]}
