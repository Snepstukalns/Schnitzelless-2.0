Schnitzeless
Komandas nosaukums: Schnitzeless
Biedri: Kristers, Dāvis, Miervaldis, Aigars
Tēma: Mēs apskatījām cik ienesīgi ir uzņēmumiem pārdot dažādus projektus izmantojot datubāzi. Aplūkojām:
Ienākumi no dažādiem produktiem laikā
Kopējos ienākumus no produkta
Ienākumus no produktiem atsevišķos periodos

21.02.2025

Mēs izdomājām, ko katrs darīs Miervaldis(dumplingbooi) Video, kods; Kristers(Snepstukalns) Grafiki; Aigars(Polozet) Statistikas raksturlielumu aprēķināšana; Dāvis(KrumIKAS) Tabula Visi kopā: Prezentācija un video

28.02.2025 Mieris atrada csv failius, kurus varees izmantot, lai izdariitu shito fakino projektu Kristers sadala lomas

21.03.2025 Pēc ilgas nekā nedarīšanas mēs beidzot saņēmāmies un uzrakstījām kodu, kas aizņēma ļoti ilgu laiku, sviedrus, asaras un asinis, bet beidzot mums ir lielāka daļa koda un dzīve liekas daudz labāka 🙂



1. Tehnoloģijas izvēle
Flask tika izvēlēts kā galvenais tīmekļa ietvars, jo tas ir viegls un vienkāršs, taču tajā pašā laikā nodrošina pietiekamu elastību darbam ar datubāzi, API un vizualizācijām. SQLAlchemy tika izmantots kā ORM, lai vienkāršotu mijiedarbību ar SQLite datubāzi.

2. Datubāzes izveide un pārdošanas datu struktūra
Lietotnē tika definēts pārdošanas datu modelis, kurā ietverts produkta nosaukums, cena un pārdošanas datums. Šāda struktūra ļauj efektīvi saglabāt un apstrādāt pārdošanas informāciju.

3. Testdatu ģenerēšana
Lai nodrošinātu vizualizāciju un datu pārvaldības funkcionalitātes testēšanu, tika izveidota funkcija nejaušu pārdošanas datu ģenerēšanai. Katram pārdošanas ierakstam tika piešķirts nejaušs produkts, cena un datums pēdējo 365 dienu laikā.

4. API un maršruti
Lietotnē tika izveidoti vairāki maršruti dažādām funkcionalitātēm:

Galvenā lapa, kurā tiek attēlota joslu diagramma.

Citas lapas dažādām vizualizācijām, tostarp pīrāga diagrammai un histogrammai.

API maršruts, kas atgriež pārdošanas datus JSON formātā, lai tos varētu izmantot ārējās sistēmās vai klienta pusē.

Maršruts CSV lejupielādei, kas ļauj eksportēt pārdošanas datus.

5. Datu vizualizācija ar Matplotlib
Lai attēlotu pārdošanas datus vizuāli, tika izveidota funkcija, kas apkopo ieņēmumus pēc produktiem un attēlo tos joslu diagrammā. Šī diagramma tiek ģenerēta dinamiski, izmantojot Matplotlib, un tiek atgriezta kā attēla fails lietotājam.

6. Lietotnes palaišana un attīstība
Flask tika palaists debug režīmā, kas nodrošina ērtu testēšanu un tūlītējas izmaiņas kodā bez nepieciešamības restartēt serveri. Šāda pieeja atviegloja attīstības procesu un ļāva ātri veikt korekcijas un uzlabojumus.
