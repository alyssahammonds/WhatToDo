
classificationWords = {
    "Openness": ["Adventurous", "Creative", "Artistic", "Curious", "Abstract"],
    "Conscientiousness": ["Self-Disciplined", "Organized", "Plan-Driven", "Aware", "Detail Focused"],
    "Extraversion": ["Energetic", "Center of Attention", "Assertive", "Impulsive", "Sociable"],
    "Agreeableness": ["Empathetic", "Trusting", "Honest", "Helping", "Put others first"],
    "Neuroticism": ["Stress Easy", "Moody", "Worrisome", "Emotionally Unstable", "Irritable"]
}
    


#This function classifies the scores for each big 5 attribute by 
def classificationScore(attributeChosen):
    #each element of the scores represents a classification score
    #openness being 0, conscientiosness 1, Extraversion 2, ... matching the structure that the dict was made
    score = []
    