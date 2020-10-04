#Import libraries
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
from sklearn.metrics.pairwise import cosine_similarity

#Simlilarity check function

def similarity_check(text):
  count_matrix = cv.fit_transform(text)
  matchPercentage = cosine_similarity(count_matrix)[0][1] * 100 #Calculate similarity
  matchPercentage = round(matchPercentage, 2) # round to two decimal
  result = matchPercentage
  return result

