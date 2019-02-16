import pandas as pd
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def prepare_X(df):
    feature_columns_to_use = ['Pclass', 'Sex', 'Age', 'Fare', 'Parch']
    nonnumeric_columns = ['Sex']

    X = df[feature_columns_to_use].fillna(0.0)

    le = LabelEncoder()
    for feature in nonnumeric_columns:
        X[feature] = le.fit_transform(X[feature])

    X = X.as_matrix()
    return X


def train_model(df):
    train_X = prepare_X(df)
    train_y = df['Survived']
    clf = RandomForestClassifier(max_depth=3, n_estimators=300)
    model = clf.fit(train_X, train_y)
    return model


def load_data():
    train_df = pd.read_csv('data/raw/train.csv', header=0)
    test_df = pd.read_csv('data/raw/test.csv', header=0)
    return train_df, test_df


if __name__ == "__main__":
    train_df, test_df = load_data()
    model = train_model(train_df)
    test_X = prepare_X(test_df)
    predictions = model.predict(test_X)
    submission = pd.DataFrame({'PassengerId': test_df['PassengerId'],
                               'Survived': predictions})
    submission.to_csv("data/processed/submission.csv", index=False)
