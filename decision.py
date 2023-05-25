import pickle

clf = pickle.load(open("LableDecisionTreeModel_New.pkl", "rb"))

def predict(data):
    try: 
        predict = clf.predict(data)
    except:
        print("Error: Predict failed")
        return "Error"
    
    if predict == 0:
        return "Not Relate"
    elif predict == 1:
        return "Relate"
    else:
        return "Error"

def initialize_data(df):
    features = ["Score" , "Change", "Skip", "Overtime", "Submit", "Worry", "Sad", "Happy", "Natural"]
    d_behavior = {'Y': 1, 'N': 0}

    df["Change"] = df["Change"].map(d_behavior)
    df["Skip"] = df["Skip"].map(d_behavior)
    df["Overtime"] = df["Overtime"].map(d_behavior)
    df["Submit"] = df["Submit"].map(d_behavior)

    try :
        df = df[features]
    except:
        print("Error: Features not found")

    return df
