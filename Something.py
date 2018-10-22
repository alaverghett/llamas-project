def plotClusters(self, X, Y):
    
    plt.plot()
    X = np.array(list(zip(X, Y))).reshape(len(X), 2) #sets X to the contents of [[x1], [x2]] - necessary for .fit below
    colors = ['b', 'g', 'c', 'm', 'k']
    markers = ['o', 'v', 's', 'p', 'd']

    # KMeans algorithm 
    # K = 3
    #kmeans_model = KMeans(n_clusters=K).fit(X)

    print(kmeans_model.cluster_centers_)
    centers = np.array(kmeans_model.cluster_centers_)

    plt.plot()
    plt.title('k means centroids')

    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(X[i], Y[i], color=colors[l], marker=markers[l],ls='None')
        plt.xlim([0, 10])
        plt.ylim([0, 10])

    plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
    plt.savefig('centroids.jpg', dpi='figure', bbox_inches='tight')
    plt.show()
    