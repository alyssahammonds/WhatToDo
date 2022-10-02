classificationWords = {
    "Openness": ["Adventurous", "Creative", "Artistic", "Curious", "Abstract"],
    "Conscientiousness": ["Self-Disciplined", "Organized", "Plan-Driven", "Aware", "Detail Focused"],
    "Extraversion": ["Energetic", "Center of Attention", "Assertive", "Impulsive", "Sociable"],
    "Agreeableness": ["Empathetic", "Trusting", "Honest", "Helping", "Put others first"],
    "Neuroticism": ["Stress Easy", "Moody", "Worrisome", "Emotionally Unstable", "Irritable"]
}

classifictions = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

attributes = ["Adventurous", "Plan-Driven", "Detail Focused", "Honest", "Helping", "Creative", "Sociable", "Aware", "Curious"]

#This function classifies the scores for each big 5 attribute by 
def classificationScore(attributeChosen):
    #each element of the scores represents a classification score
    #openness being 0, conscientiosness 1, Extraversion 2, ... matching the structure that the dict was made
    score = [0, 0, 0, 0, 0]
    
    counter = 0
    for classification in classificationWords:
        for word in classificationWords[classification]:
            for attribute in attributeChosen:
                if(word == attribute):
                    score[counter] = score[counter] + 1
        counter = counter + 1
    
    if score.index(max(score)) == 0:
        return "Openness"
    elif score.index(max(score)) == 1:
        return "Conscientiousness"
    elif score.index(max(score)) == 2:
        return "Extravertion"
    elif score.index(max(score)) == 3:
        return "Agreeableness"
    
    return "Neuroticism"
        

print(classificationScore(attributes))  
