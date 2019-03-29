import pandas as pd
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
import yaml


def load_configs():
    with open('configs/train_configs.yaml', 'r') as f:
        configs = yaml.load(f)
    return configs


def prepare_X(df):
    feature_columns_to_use = ['Pclass', 'Sex', 'Age', 'Fare', 'Parch']
    nonnumeric_columns = ['Sex']

    X = df[feature_columns_to_use].fillna(0.0)

    le = LabelEncoder()
    for feature in nonnumeric_columns:
        X[feature] = le.fit_transform(X[feature])

    X = X.values
    return X


def train_model(df, configs):
    train_X = prepare_X(df)
    train_y = df['Survived']
    if configs.get('model_type') == 'RandomForest':
        max_depth = configs.get('RandomForest').get('max_depth')
        n_estimators = configs.get('RandomForest').get('n_estimators')
        clf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators)
    elif configs.get('model_type') == 'GradientBoosting':
        max_depth = configs.get('GradientBoosting').get('max_depth')
        n_estimators = configs.get('GradientBoosting').get('n_estimators')
        clf = GradientBoostingClassifier(max_depth=max_depth, n_estimators=n_estimators)
    model = clf.fit(train_X, train_y)
    return model


def load_data():
    train_df = pd.read_csv('data/raw/train.csv', header=0)
    test_df = pd.read_csv('data/raw/test.csv', header=0)
    return train_df, test_df


if __name__ == "__main__":
    train_df, test_df = load_data()
    configs = load_configs()
    model = train_model(train_df, configs.get('training'))
    test_X = prepare_X(test_df)
    predictions = model.predict(test_X)
    submission = pd.DataFrame({'PassengerId': test_df['PassengerId'],
                               'Survived': predictions})
    submission.to_csv("data/processed/submission.csv", index=False)
    print("Done")
