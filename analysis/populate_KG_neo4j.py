#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "harvest Industry documents of University of California database (https://www.industrydocuments.ucsf.edu/) via SolR "
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de, Ziyad Ziyad ziyad@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import os
import glob
import json
from py2neo import Graph
from py2neo.bulk import create_nodes, create_relationships

from neo4j import GraphDatabase





def load_json(graph, path_to_json):
    cypher_master_parent_data = [{'title': 'Object', 'name' : 'Parent Object' }]
    create_nodes(graph.auto(), cypher_master_parent_data, labels={'Object'})
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    return json_files

def harvest_json(json_files, path_to_json):
    paper_author_rel = []
    paper_type_rel = []
    paper_title_rel =[]
    paper_brand_rel =[]
    paper_grant_rel = []
    paper_organzation_rel = []
    paper_subject_rel = []
    paper_mentioned_rel = []
    node_data = []

    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js), encoding='utf-8') as json_file:
            json_data = json.load(json_file)

            for document in json_data['response']['docs']:
                node_data.append(document)
                id = document['id']
                if 'type' in document:
                    for type in document['type']:
                        paper_type_rel.append((id, [], type))
                if 'author' in document:
                    for author in document['author']:
                        paper_author_rel.append((id, [],author))
                if 'title' in document:
                    title = document['title']
                    paper_title_rel.append((id, [], title))
                if 'brand' in document:
                    for brand in document['brand']:
                        paper_brand_rel.append((id, [], brand))
                if 'grant' in document:
                    grant =  document['grant']
                    if ';' in grant:
                        grant_uniq = grant.split(';')
                        for item in grant_uniq:
                            paper_grant_rel.append((id, [], item))
                    else:
                        paper_grant_rel.append((id, [], grant))
                if 'organization' in document:
                    #### there is no "organization" mentioned in the current data set. this is why there is no output.####
                    for organization in document['organization']:
                        paper_organzation_rel.append((id, [], organization))
                if 'subject' in document:
                    #### there is no "subject" stated in the current data set, this is why there is no output####
                    for subject in document['subject']:
                        paper_subject_rel.append((id, [], subject))
                if 'mentioned'in document:
                    for mentioned in document['mentioned']:
                        paper_mentioned_rel.append((id, [], mentioned))
    #print('paper_title_rel', paper_title_rel[:10])
    #print('paper_type_rel', paper_type_rel[:10])
    print('paper_grant_rel', paper_grant_rel[:10])
    return node_data, paper_type_rel, paper_author_rel, paper_title_rel, paper_brand_rel, paper_grant_rel, paper_organzation_rel, paper_subject_rel, paper_mentioned_rel



def create_publications_nodes(graph, node_data):
    create_nodes(graph.auto(), node_data, labels=['Publication'])
def create_authors_nodes(graph, paper_author_rel):
    authors_uniq = list(set(a[2] for a in paper_author_rel))
    authors_uniq = [[x] for x in authors_uniq]
    create_nodes(graph.auto(), authors_uniq, labels=['Person'], keys=['name'])
def create_types_nodes(graph, paper_type_rel):
    type_uniq = list(set(a[2] for a in paper_type_rel))
    type_uniq = [[x] for x in type_uniq]
    create_nodes(graph.auto(), type_uniq, labels=['Publ_Type'], keys=['publ_type'])
def create_title_nodes(graph, paper_title_rel):
    title_uniq = list(set(a[2] for a in paper_title_rel))
    title_uniq = [[x] for x in title_uniq]
    create_nodes(graph.auto(), title_uniq, labels=['Title'], keys=['publ_title'])

def create_brand_nodes(graph, paper_brand_rel):
    brand_uniq = list(set(a[2] for a in paper_brand_rel))
    brand_uniq = [[x] for x in brand_uniq]
    print(brand_uniq)
    #create_nodes(graph.auto(), brand_uniq, labels=['Brand'], keys=['brand'])

def create_grant_nodes(graph, paper_grant_rel):
    grant_uniq = list(set(a[2] for a in paper_grant_rel))
    grant_uniq = [[x] for x in grant_uniq]
    create_nodes(graph.auto(), grant_uniq, labels=['Grant'], keys=['grant'])

def create_organization_nodes(graph, paper_organization_rel):
    org_uniq = list(set(a[2] for a in paper_organization_rel))
    print(org_uniq)
    org_uniq = [[x] for x in org_uniq]
    create_nodes(graph.auto(), org_uniq, labels=['Organization'], keys=['organization'])

def create_subject_nodes(graph, paper_subject_rel):
    subject_uniq = list(set(a[2] for a in paper_subject_rel))
    subject_uniq = [[x] for x in subject_uniq]
    create_nodes(graph.auto(), subject_uniq, labels='Subject', keys=['subject'])

def create_mentioned_person_nodes(graph, paper_mentioned_rel):
    mentioned_person_uniq = list(set(a[2] for a in paper_mentioned_rel))
    mentioned_person_uniq = [[x] for x in mentioned_person_uniq]
    create_nodes(graph.auto(), mentioned_person_uniq, labels=['Mentioned_Person'], keys=['mentioned_person'])

def create_our_relationships(graph, paper_type_rel, paper_author_rel, paper_title_rel, paper_brand_rel, paper_grant_rel ,paper_organzation_rel,paper_subject_rel, paper_mentioned_rel):
    #create_relationships(graph.auto(), paper_type_rel, rel_type="IS_PUBLTYPE", start_node_key=('Publication', 'id'),
      #                   end_node_key=('Publ_Type', 'publ_type'), keys=[])
    #print('xxxx', paper_author_rel[:10])
    #create_relationships(graph.auto(), paper_author_rel, rel_type='WRITTEN_BY', start_node_key=('Publication', 'id'),
                       #  end_node_key=('Person', 'name'), keys=[])
    #print('yyy')
    print('xx')
    #create_relationships(graph.auto(), paper_title_rel, rel_type="HAS_TITLE", start_node_key=('Publication', 'id'),
              #          end_node_key=('Title', 'title'), keys=[])

    #create_relationships(graph.auto(), paper_brand_rel, rel_type="HAS_BRAND", start_node_key=('Publication', 'id'),
    #                     end_node_key=('Brand', 'brand'), keys=[])

    create_relationships(graph.auto(), paper_grant_rel, rel_type="HAS_GRANT", start_node_key=('Publication', 'id'),
                         end_node_key= ('Grant, grant'), keys=[])
    print('yy')
    #### there is no "organization" mentioned in the current data set. this is why there is no output.####
    #create_relationships(graph.auto(), paper_organzation_rel, rel_type='HAS_ORGANIZATION', start_node_key=('Publication', 'id'),
       #                  end_node_key=('Organization','organization'), keys=[])
    #### there is no "subject" mentioned in the current data set. this is why there is no output.####
    #create_relationships(graph.auto(), paper_subject_rel, rel_type='HAS_SUBJECT', start_node_key=('Publication', 'id'),
      #                   end_node_key=('Subject', 'subject'), keys=[])
    #create_relationships(graph.auto(), paper_mentioned_rel, rel_type="MENTIONS", start_node_key=('Publication', 'id'),
     #                    end_node_key=('Mentioned_Person', 'mentioned'), keys=[])
def create_same_other_relationship(graph, author_mentioned_rel):
    create_relationships(graph.auto(), author_mentioned_rel, rel_type='MENTIONS_AUTHOR_OF', start_node_key=('Publication', 'id'), end_node_key=('Publication', 'id'), keys=[])

def create_one_relationship(graph, paper_grant_rel):
    create_relationships(graph.auto(), paper_grant_rel, rel_type="HAS_GRANT", start_node_key=('Publication', 'id'),
                         end_node_key=('Grant, grant'), keys=[])
def check_authors_mentioned(paper_author_rel, paper_mentioned_rel):
    person_author_uniq = list(set(a[2] for a in paper_author_rel))
    print('1' , len(person_author_uniq))
    paper_mentioned_uniq = list(set(a[2] for a in paper_mentioned_rel))
    print('2', len(paper_mentioned_uniq))
    same_persons = [x for x in person_author_uniq + paper_mentioned_uniq if x in person_author_uniq or x not in paper_mentioned_uniq]
    #print('3', same_persons)
    author_mentioned_rel = []
    for person in same_persons:
        for id_author, x, person_author in paper_author_rel:
            if person == person_author:
                for id_mentioned, x, person_mentioned in paper_mentioned_rel:
                    if person == person_mentioned:
                        author_mentioned_rel.append((id_mentioned, [],id_author))
    print('author mentioned', author_mentioned_rel[:10])
    return author_mentioned_rel

def check_papers_by_same_author(paper_author_rel):
    paper_uniq = list(set(a[0] for a in paper_author_rel))


    #print(paper_author_rel)
    #print(paper_uniq)





def main():
    graph = Graph("bolt://localhost:7687", auth=("Eva", "123456789"))
    #driver = GraphDatabase.driver("bolt://localhost:7687", auth=('Eva', '123456789'))
    path_to_json = '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/2024_tobacco_industry_documents'

    json_files = load_json(graph, path_to_json)
    node_data, paper_type_rel, paper_author_rel, paper_title_rel, paper_brand_rel, paper_grant_rel, paper_organzation_rel, paper_subject_rel, paper_mentioned_rel = harvest_json(json_files, path_to_json)


    #check_authors_mentioned(paper_author_rel, paper_mentioned_rel)
    #check_papers_by_same_author(paper_author_rel, paper_mentioned_rel)
    #author_mentioned_rel = check_authors_mentioned(paper_author_rel, paper_mentioned_rel)

    #create_publications_nodes(graph, node_data)
    #create_types_nodes(graph, paper_type_rel)
    #create_authors_nodes(graph, paper_author_rel)
    #create_title_nodes(graph, paper_title_rel)
    #create_brand_nodes(graph, paper_brand_rel)

    #create_grant_nodes(graph, paper_grant_rel)
    #### there is no "organization" stated in the current data set, this is why there is no output####
    #create_organization_nodes(graph, paper_organzation_rel)

    #### there is no "subject" stated in the current data set, this is why there is no output####
    #create_subject_nodes(graph, paper_subject_rel)

    #create_mentioned_person_nodes(graph, paper_mentioned_rel)
    #print('created all nodes')
    create_our_relationships(graph, paper_type_rel, paper_author_rel, paper_title_rel, paper_brand_rel, paper_grant_rel, paper_organzation_rel, paper_subject_rel, paper_mentioned_rel)
    #create_one_relationship(graph,paper_grant_rel)
    #print('created relationships')


if __name__ == "__main__":
    main()