import matplotlib.pyplot as plt

class Plotter():
    
    @staticmethod
    def genScatterPlot(reviews, imgName, xMember='date', yMember='stars'):
        '''Reviews should be a list of reviews,
           Generates scatter plot of star ratings vs time
           * You can send any member variable of the json as the X or Y values here
           **Note that you must have a folder "figures/scatter/" for this function to work'''
        X = [review[yMember] for review in reviews]
        Y = [review[xMember] for review in reviews]
        X = [x for _,x in sorted(zip(Y,X))] #Reference: https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        Y = sorted(Y)
        plt.scatter(Y, X)
        plt.savefig('figures/scatter/' + imgName, dpi='figure', bbox_inches='tight')
        plt.show()
    
    @staticmethod
    def avgRatingsOverTime(reviews, imgName):
        '''Generates line plot showing the average star rating vs time
        Note that you must have a folder "figures/plot/" for this function to work'''
        '''Generalized: Avg[x] = (Avg[x-1] * x + arr[x]) / (x + 1)'''
        X = [review['stars'] for review in reviews]
        Y = [review['date'] for review in reviews]
        X = [x for _,x in sorted(zip(Y,X))] #Reference: https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        Y = sorted(Y)     
        
        avg = X[0]
        avgX = [avg]
        for n in range(1, len(X)):
            avg = (avg * n + X[n]) / (n + 1) #calcs incremental average
            avgX.append(avg)
        
        plt.plot(Y, avgX)
        plt.savefig('figures/plot/' + imgName, dpi='figure', bbox_inches='tight')
        plt.show()
		
'''Useful snippets for main
	p = Plotter()
	
	imgName = str(r + 1) + '.jpg'

    plt.rcParams["figure.figsize"] = [18, 13]
    p.genScatterPlot(revs, imgName)
    p.avgRatingsOverTime(revs, imgName)'''