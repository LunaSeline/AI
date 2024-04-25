from sklearn.feature_extraction.text import CountVectorizer
documents= [ "HI! THIS IS LUNA.",
    "HOW DO YOU DO.",
    "TODAY IS A SUNNY DAY.",
    "I LOVE ICE-CREAM."]
# Create the CountVectorizer object
vectorizer = CountVectorizer()
# Fit the vectorizer to the documents and transform the documents into BoW
bow_matrix = vectorizer.fit_transform(documents)
# Get the vocabulary (unique words) learned by the vectorizer
vocabulary = vectorizer.get_feature_names_out()
# Print the BoW matrix and vocabulary
print("Bag of Words Matrix:")
print(bow_matrix.toarray())
print("\nVocabulary:")
print(vocabulary)
