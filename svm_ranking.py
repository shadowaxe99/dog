```python
from sklearn import svm

class SnippetRanking:
    def __init__(self, feature_vector, labels):
        self.feature_vector = feature_vector
        self.labels = labels
        self.classifier = svm.SVC()

    def train(self):
        self.classifier.fit(self.feature_vector, self.labels)

    def rank(self, snippet):
        return self.classifier.predict(snippet)
```