
# coding: utf-8

# In[39]:


import ijson
import json
import time
import matplotlib.pyplot as plt
import matplotlib.dates as dates

class Dataset():

    def __init__(self):
        '''
        Expects a dataset directory with yelp_business_new.json and yelp_review_new.json
        '''
        BUSINESS_DATASET_NEW = "dataset/yelp_business_new.json"
        REVIEW_DATASET_NEW = "dataset/yelp_review_minified.json"
        self.business_file = open(BUSINESS_DATASET_NEW)
        self.review_file = open(REVIEW_DATASET_NEW)

    def get_business_ids(self):
        return (business['business_id'] for business in ijson.items(self.business_file, 'item'))

    def get_reviews(self, business_id):
        return (review for review in ijson.items(self.review_file, 'item') if review['business_id'] == business_id)

    def get_reviews_std(self, business_id):
        '''
        Returns a list
        '''
        reviews = json.load(self.review_file)
        return [review for review in reviews if review['business_id'] == business_id]

    
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
        
    @staticmethod
    def genScaledScatterPlot(reviews, imgName):
        '''Identical to default genScatterPlot, but with time represented in scale'''
        X = [review['stars'] for review in reviews]
        Y = [datetime.strptime(review['date'], "%Y-%m-%d").date() for review in reviews]
        X = [x for _,x in sorted(zip(Y,X))] #Reference: https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        Y = sorted(Y)
        plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y'))
        plt.scatter(Y, X, color='red')
        
        plt.xlabel('Date')
        plt.ylabel('Star Rating')
        plt.title('Star Ratings over Time')
        plt.gcf().autofmt_xdate()
        
        plt.savefig('figures/scatter/' + imgName, dpi='figure', bbox_inches='tight')
        plt.show()
        

    @staticmethod
    def scaledAvgRatingsOverTime(reviews, imgName):
        '''Generates line plot showing the average star rating vs time
        Note that you must have a folder "figures/plot/" for this function to work'''
        '''Generalized: Avg[x] = (Avg[x-1] * x + arr[x]) / (x + 1)'''
        X = [review['stars'] for review in reviews]
        Y = [datetime.strptime(review['date'], "%Y-%m-%d").date() for review in reviews]
        X = [x for _,x in sorted(zip(Y,X))] #Reference: https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        Y = sorted(Y)     
        
        avg = X[0]
        avgX = [avg]
        for n in range(1, len(X)):
            avg = (avg * n + X[n]) / (n + 1) #calcs incremental average
            avgX.append(avg)
        
        
        plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m/%d/%Y'))
        #plt.gca().xaxis.set_major_locator(dates.DayLocator())
        plt.plot(Y, avgX, color='red')
        
        plt.xlabel('Date')
        plt.ylabel('Star Rating')
        plt.title('Average Star Rating over Time')
        
        plt.gcf().autofmt_xdate()
        plt.savefig('figures/plot/' + imgName, dpi='figure', bbox_inches='tight')
        plt.show()
        
        
        
if __name__ == '__main__':
    '''
    Testing the two functions in Dataset
    '''
    i = Dataset()
    p = Plotter()

    j = i.get_business_ids().__next__()

    revs = i.get_reviews_std(j);
    
    '''testRevs = []
    for review in revs:
        testRevs.append(review['date'])
    testRevs = sorted(testRevs)
    for r in testRevs:
        print(r) '''
    #p.genScatterPlot(revs, "001.jpg")
    p.genScaledScatterPlot(revs, "scaled_001.jpg")
    #p.avgRatingsOverTime(revs, "001.jpg")
    p.scaledAvgRatingsOverTime(revs, "scaled_001.jpg")

