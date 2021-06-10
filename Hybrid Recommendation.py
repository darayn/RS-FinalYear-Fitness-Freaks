import numpy as np
import pandas as pd
import re
import random
from bs4 import BeautifulSoup as bs
import requests
import datetime
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity, haversine_distances
from math import radians
from sklearn.neighbors import DistanceMetric
global dist 
dist = DistanceMetric.get_metric('haversine')



def get_both_datasets_for_normalisation(df):
    df1 = df[['Name', 'Gender', 'Flexibility', 'Pincode', 'Body Composition', 'Composition Percentage', 'Interactiveness', 'Workout Frequency', 'Workout Mode Preferred', 'is_sports_enthusiast', 'like_to_be_mentored', 'like_to_mentor', 'fitness_goal_to_be achieved','addons in session','Height_in_cms','Age']]
    df2 =df[['Name', 'Name Of Area', 'Pincode', 'Latitude ','Longitude']]
    return df1,df2


def get_df1_normalised(df, names):
    df['Gender'] = df["Gender"].astype('category').cat.codes
    df['Body Composition'] = df["Body Composition"].astype('category').cat.codes
    df['Workout Frequency'] = df["Workout Frequency"].astype('category').cat.codes
    df['Workout Mode Preferred'] = df["Workout Mode Preferred"].astype('category').cat.codes
    df['is_sports_enthusiast'] = df["is_sports_enthusiast"].astype('category').cat.codes
    df['fitness_goal_to_be achieved'] = df["fitness_goal_to_be achieved"].astype('category').cat.codes
    df['addons in session'] = df["addons in session"].astype('category').cat.codes
    df[names] = MinMaxScaler().fit_transform(df[names])
    return df

def getSimilarityMatrix(df1_scaled):
    similarity_cos = cosine_similarity(df1_scaled.drop('Name',axis=1))
    df1_similarity = pd.DataFrame(similarity_cos, columns=df1_scaled['Name'], index=df1_scaled['Name'])
    return df1_similarity



def getUserCorrelation(df1_similarity,name):
    df1_user = df1_similarity.loc[name,:]
    return df1_user


def addLatLongRad(df2):
    df2['Latitude_rad'] = np.radians(df2['Latitude '])
    df2['Longitude_rad'] = np.radians(df2['Longitude'])
    return df2


def getDistanceMatrix(df2):
    distance_similarity_df2 = pd.DataFrame(dist.pairwise(df2[['Latitude_rad','Longitude_rad']].to_numpy())*6371,  columns=df2.Name.unique(), index=df2.Name.unique())
    return distance_similarity_df2



def getUserDistCorrelation(distance_matrix, name):
    df2_user=distance_matrix.loc[name,:]
    df2_scaled_user = 1-MinMaxScaler().fit_transform(pd.DataFrame(df2_user))
    return df2_scaled_user


def getFinalRecommendatonMatrix(Rec1, Rec2 , name):
    df_recommedation = pd.DataFrame(Rec1)
    df_recommedation['Haversine'] = Rec2
    df_recommedation.rename(columns = {name:'Cosine Similarity'}, inplace = True)
    return df_recommedation

def prioritySetter(df_recommedation,df, priority1, priority2):
    df_recommedation['Score'] = priority1* df_recommedation['Cosine Similarity'] + priority2* df_recommedation['Haversine']
    Hybrid_Recommendation=df_recommedation.sort_values(['Score'], ascending=False)
    Hybrid_rec = Hybrid_Recommendation.index.to_list()
    final_rec = df.set_index('Name').loc[Hybrid_rec[:]].reset_index(inplace=False)
    return final_rec





if __name__ == "__main__":
	name = 'Kashvi Chande'
	df = pd.read_csv("Final Dataset before Normalisation.csv", index_col=[0])
	df1,df2 = get_both_datasets_for_normalisation(df)
	names = ['Flexibility','Composition Percentage','Pincode', 'Interactiveness', 'like_to_be_mentored', 'like_to_mentor', 'Height_in_cms', 'Age']
	df1 = get_df1_normalised(df1,names)
	df1_scaled = df1.copy()
	df1_similarity= getSimilarityMatrix(df1_scaled)
	user_corr = getUserCorrelation(df1_similarity, name)
	df2 = addLatLongRad(df2)
	distance_matrix = getDistanceMatrix(df2)
	user_distance = getUserDistCorrelation(test_distance_matrix, name)
	final_rec = getFinalRecommendatonMatrix(user_corr,user_distance,name)
	Recommendations= prioritySetter(final_rec, df, 0.1,0.7) ##Setting the priority Bases on 5 personality Traits and Location
	return Recommendations