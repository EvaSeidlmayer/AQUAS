#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "request pretrained BERT model"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023-2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "




import argparse
import torch
#from BERT_training_sliding_window import AQUASSlidingBERT
from transformers import BertTokenizer, AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoModelForCausalLM


BERT_MODEL_IDENTIFIER = "models/FSoLS-24-v4_Mistral7b_512tokenz_e5_lr3e-5_mlclass"
#BERT_MODEL_IDENTIFIER = "bert-base-uncased"
#BERT_MODEL_IDENTIFIER = "dmis-lab/biobert-v1.1"
max_length = 512

argparser = argparse.ArgumentParser()
argparser.add_argument("model", help="Path to the pre-trained model")
args = argparser.parse_args()


# Load the trained model
#model = AQUASSlidingBERT.from_pretrained(args.model)
model = AutoModelForSequenceClassification.from_pretrained(args.model)

# Preprocess the specific text
text = "World Malaria Day – A community effort to achieve ZERO  April 25, 2023 Johannes Stortz PLOS ONE Listicle  While tremendous progress has been made in fighting malaria, the disease still poses a significant threat to global human health. Especially in hard-to-reach remote and rural areas, fighting malaria remains a challenge. Therefore, this year’s WHO World Malaria Day emphasizes the need for innovative strategies and measurements to combat malaria in the Western Pacific Region with the overall goal of eliminating the burden of malaria worldwide. To emphasise the efforts made by the research community to achieve zero malaria, we are highlighting publications in PLOS ONE that strengthen our understanding of the disease and develop innovative strategies for controlling and eradicating malaria. At PLOS ONE, we are excited to serve as a platform for the malaria research community by making cutting-edge research accessible to everyone. To further strive towards the WHO’s aim of zero malaria, we welcome research submissions that describe novel approaches to combat malaria, increase our understanding of the pathogen and its vector, and deliver epidemiological insights into malaria dynamics in hard-to-reach communities.  Research Highlights jplenio, Pixabay license 1 – Results from a malaria indicator survey highlight the importance of routine data capture in high-risk forest and farm transmission sites in Vietnam to tailor location-specific malaria elimination interventions In this survey, Ngo and co-workers assess the knowledge about malaria and preventative measures in mobile human populations sleeping and working in forests or on farms in Vietnam. The survey highlights the importance of monitoring remote high-risk transmission areas to effectively tailor malaria interventions. Shutterbug75, Pixabay license 2 – Cross-reactive inhibitory antibody and memory B cell responses to variant strains of Duffy Binding Protein II at post-Plasmodium vivax infection Thawornpan and co-workers investigate the cross reactivity of antibodies against the Plasmodium vivax Duffy binding protein (DBP), a potential vaccine candidate. The authors investigate the immune response against DBP in mice, thus providing valuable insights for future design strategies for effective vaccines against Plasmodium vivax. pone.0258580 3 – Cross-sectional Survey of Asymptomatic Malaria in Dak Nong Province in the Central Highlands of Vietnam for the Malaria Elimination Roadmap Quang and colleagues investigate the prevalence of asymptomatic malaria in people living in three communes in Vietnam. The research highlights asymptomatic parasite carriers as undetected reservoirs for future malaria transmissions. This study concludes that knowledge about the prevalence and distribution of asymptomatic malaria will benefit future elimination efforts. jeanvdmeulen, Pixabay license 4 – Study protocol for development of an options assessment toolkit (OAT) for national malaria programs in Asia Pacific to determine best combinations of vivax radical cure for their given contexts  To enable the most effective strategies for combating malaria caused by Plasmodium vivax in the Asia Pacific region, Manash Shrestha and co-workers are planning to identify various factors that determine the unique context of different transmission environments. Based on these factors, the help of experts will be employed to develop an adaptable tool kit that will help decision-makers to tailor their anti-malaria approaches. AhmadArdity, Pixabay license 5 – A systematic review and meta-analysis of asymptomatic malaria infection in pregnant women in Sub-Saharan Africa: a challenge for malaria elimination efforts This systematic review by Yonas Yimam and colleagues finds evidence in the existing literature that asymptomatic malaria infections, predominantly caused by P. falciparum, can cause anemia in pregnant women. The authors conclude that antenatal care should be adapted to take into consideration the possible effect of asymptomatic malaria infections on pregnant women in Sub-Saharan Africa. References 1 – Ngo TD, Canavati SE, Dung DV, Vo TH, Tran DT, Tran LK, et al. (2021) Results from a malaria indicator survey highlight the importance of routine data capture in high-risk forest and farm transmission sites in Vietnam to tailor location-specific malaria elimination interventions. PLoS ONE 16(4): e0250045. https://doi.org/10.1371/journal.pone.0250045 2- Thawornpan P, Changrob S, Kochayoo P, Wangriatisak K, Ntumngia FB, De SL, et al. (2022) Cross-reactive inhibitory antibody and memory B cell responses to variant strains of Duffy binding protein II at post-Plasmodium vivax infection. PLoS ONE 17(10): e0276335. https://doi.org/10.1371/journal.pone.0276335 3 – Quang HH, Chavchich M, Trinh NTM, Manh ND, Edstein MD, Martin NJ, et al. (2021) Cross-sectional survey of asymptomatic malaria in Dak Nong province in the Central Highlands of Vietnam for the malaria elimination roadmap. PLoS ONE 16(10): e0258580. https://doi.org/10.1371/journal.pone.0258580 4 – Shrestha M, Neukom J, Acharya S, Habib MN, Wini L, Duong TT, et al. (2023) Study protocol for development of an options assessment toolkit (OAT) for national malaria programs in Asia Pacific to determine best combinations of vivax radical cure for their given contexts. PLoS ONE 18(3): e0280950. https://doi.org/10.1371/journal.pone.0280950 5 – Yimam Y, Nateghpour M, Mohebali M, Abbaszadeh Afshar MJ (2021) A systematic review and meta-analysis of asymptomatic malaria infection in pregnant women in Sub-Saharan Africa: A challenge for malaria elimination efforts. PLoS ONE 16(4): e0248245. https://doi.org/10.1371/journal.pone.0248245"

#preprocess text
tokenizer = BertTokenizer.from_pretrained('Mistral-7B')
tokens = tokenizer(text, max_length=max_length, padding="max_length", truncation=True, return_tensors= 'pt')
#tokens = torch.tensor(tokens['input_ids'])
#input_tensor = tokens.unsqueeze(0)

input_ids = tokens['input_ids']
attn_mask = tokens['attention_mask']
print("text is preprocessed")


output = model(input_ids=input_ids, attention_mask= attn_mask)

logits = output['logits']
sigmoid_output =torch.sigmoid(logits)
soft_output = torch.softmax(logits, -1)


print('without softmax', sigmoid_output)
print('with softmax', soft_output)

