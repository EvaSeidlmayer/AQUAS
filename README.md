<<<<<<< HEAD
# AQUAS
Project documentation on Automatic Quality Assessment NLP approach for the semantic mapping of texts in the life science
=======
# Automatic Quality Assessment: NLP approach for the semantic mapping of texts in the life science

---

## Project description

The growing incidence of deliberately spread misinformation poses a major challenge to our democratic society. It is increasingly being spread by political interest groups in order to determine public discourse. The recipients sometimes fail to recognize this misinformation as such. Since disinformation can also be found in scientific information, this development also affects scientists. In the medical applications of the life sciences (LeWi), this can have have health-endangering effects. 

In the project AQUAS presented here, the first German-language dataset on disinformation in the life sciences will be created. On this basis, modern machine learning (ML) methods will be used to create an ML model that will be able to gradually classify the semantic proximity of unknown texts to the classes scientific texts, popular science texts and disinforming texts. At the same time, complementary information on the good scientific practices of the publications will be provided. With the enrichment and
AQUAS aims at supporting the reader in making an informed assessment of literature by enriching and publishing the above-mentioned information (basic set and extended set of characteristics, respectively). 

Thereby AQUAS does not aim at a final reading recommendation of the contents or censorship. Based on the developed enrichment methods, AQUAS will implement a service that can be accessed via an application programming interface (API). As a first central application we will use this service through the ZB MED discovery system LIVIVO to make the described classification of literature available to the users of ZB MED. This will initially be used by the scientists of the and practitioners in the health care professions as well as students will benefit from the improved knowledge infrastructure at LIVIVO through AQUAS. The dataset, the model, the workflow for the training and the software for the operation of the service will be made openly available, if possible. and thus also made usable for other subject areas.

AQUAS at [ZB MED](https://www.zbmed.de/forschen/laufende-projekte/aquas/)


## Publications 

## Dataset

## database schema 
![](/home/ruth/ProgrammingProjects/AQUS/AQUAS/2023-03-07_databaseschema.png)



## data set
- 4 categories
- retrieval modi: PDF scraped, HTML scraped, reused data set
  - URLs retrieved with  /home/ruth/ProgrammingProjects/AQUS/AQUAS/analysis/scrap_website-urls.py
  URLs manually checked.

    - scientific: 451 + 312+ 4616 PubMed Central: https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/
    - popular science: 
      - Wikipedia: 648 
      - MedlinePlus: 1.200 https://medlineplus.gov/healthtopics.html 
   
    - disinformation: 
      - health.news: 99
      - healthimpactnews.com: 78
      - cevo.mykajabi.com: 10
      - 7553 items: Covid-misinformation data set retrieved from Poynter.org
    - alternative science  
     
**collecting enough data for disinformation category is the bottle neck of the data set. If you like to inprove te datas set please inform us if you find an article which should be classified as disinformation. please write an email to seidlmayer@zbmed.de** 



## Code
 see this repoitory: ./analysis

## Press release
[Deutsches Ärzteblatt: Künstliche Intelligenz soll Fake News bei medizinischen Informationen erkennen, 2022-12-27](https://www.aerzteblatt.de/nachrichten/139246/Kuenstliche-Intelligenz-soll-Fake-News-bei-medizinischen-Informationen-erkennen)<br/>
[B.I.T.-online: ZB MED sagt Falschinformationen den Kampf an, 2023-01-06](https://www.b-i-t-online.de/neues/7715)<br/>
[Fachbuchjournal: ZB MED sagt Falschinformationen den Kampf an, 2023](https://www.fachbuchjournal.de/zb-med-sagt-falschinformationen-den-kampf-an/)<br/>
[German Circle (privater Blog), 2023-01-14](https://germancircle.blogspot.com/2023/01/aquas-gegen-falschinformationen.html)<br/>


## Responsible
Eva Seidlmayer, Dr. phil., M.LIS <br/>
Data Sciences and Services, Research Fellow <br/>
ORCID: 0000-0001-7258-0532 <br/>
Twitter: @kivilih <br/>
<br/>
ZB MED – Informations Centre for Life Sciences <br/>
Gleueler Straße 60 <br/>
50931 Cologne <br/>
Germany <br/>
<br/>
[www.zbmed.de](www.zbmed.de) <br/>
INFORMATION. KNOWLEDGE. LIFE.




## Funding
DFG-LIS  <br/>
FO 984/6-1

## License
>>>>>>> 16abf1e4419ea0c154748f0336cf3138056dc945
