from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score,recall_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV

class Trainer:
    def __init__(self, test_size=0.2, random_state=42):
        self.model = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.test_size = test_size
        self.random_state = random_state
    def split_data(self, x, y):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=self.test_size, random_state=self.random_state)
    
    def train_baseline(self, model):
        self.model = model
        self.model.fit(self.x_train, self.y_train)
        return self.model
    def evaluate_model(self):
        y_pred = self.model.predict(self.x_test)
        y_prob = self.model.predict_proba(self.x_test)[:,1]
        return {
            "accuracy": accuracy_score(self.y_test, y_pred),
            "precision": precision_score(self.y_test, y_pred),
            "recall": recall_score(self.y_test, y_pred),
            "f1_score": f1_score(self.y_test, y_pred),
            "roc_auc": roc_auc_score(self.y_test, y_prob)
        }
    def hyperparameter_tuning(self, model, cv=5, param_grid=None):
        
        grid = GridSearchCV(model, param_grid, cv=cv, scoring='roc_auc', n_jobs=-1)
        grid.fit(self.x_train, self.y_train)
        self.model = grid.best_estimator_
        return self.model, grid.best_params_
