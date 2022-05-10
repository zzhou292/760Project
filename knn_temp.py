if test_case == 1:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import GridSearchCV
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    param_grid = [
        {
            'weights': ['uniform'], 
            'n_neighbors': [i for i in range(1, 20)]
        },
        {
            'weights': ['distance'],
            'n_neighbors': [i for i in range(1, 20)], 
            'p': [i for i in range(1, 6)]
        }
    ]



    X = np.array(CT_Data)
    X = X.T
    X = X.astype(float)
    standardScalar = StandardScaler()
    standardScalar.fit(X)
    standardScalar.transform(X)
    y = np.array(Outcome_Data[21])
    y = y.astype(int)
    print(X.shape)
    print(y.shape)
    knn_clf = KNeighborsClassifier()
    grid_search = GridSearchCV(knn_clf, param_grid , cv = 5, scoring = 'average_precision')
    grid_search.fit(X, y)
    print(grid_search.best_estimator_)
    print(grid_search.best_score_)


    # ============================================
    def predict_Knn(test_vec, train_data, train_label, k):
        res_list = []
        dis_list = []
        train_data = train_data.astype(float)
        test_vec = test_vec.astype(float)
        for i in range(train_data.shape[1]):
            diff = (test_vec.reshape((train_data.shape[0],1))) - train_data[:,i]
            dis_list.append(np.linalg.norm(diff))

            
        # Smallest K elements indices
        # using sorted() + lambda + list slicing
        res = sorted(range(len(dis_list)), key = lambda sub: dis_list[sub])[:k] 

        for i in range(len(res)):
            res_list.append(train_label[res[i]])

        count_0 = 0
        count_1 = 0

        for i in range(len(res_list)):
            if res_list[i] == 0:
                count_0 = count_0 + 1
            else:
                count_1 = count_1 + 1

        #if count_1 > count_0:
        #    return 1
        #else:
        #    return 0        

        # as long as one nearest neighbour has cancer,
        # than we predict cancer
        if count_1 > 0:
            return 1
        else:
            return 0