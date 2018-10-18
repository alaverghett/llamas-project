import ijson
import json
import time


class Dataset():

    def __init__(self):
        '''
        Expects a dataset directory with yelp_business_new.json and yelp_review_new.json
        '''
        self.BUSINESS_DATASET_NEW = "dataset/yelp_business_new.json"
        self.REVIEW_DATASET_NEW = "dataset/yelp_review_minified.json"
        self.BUSINESS_DATASET = "./dataset/yelp_academic_dataset_business.json"
        self.REVIEW_DATASET = "./dataset/yelp_academic_dataset_review.json"
        # self.business_file = open(BUSINESS_DATASET_NEW)
        # self.review_file = open(REVIEW_DATASET_NEW)

    def get_business_ids(self):
        return (json.loads(business)['business_id'] for business in open(self.BUSINESS_DATASET, 'r'))

    def get_reviews(self, business_id):
        '''
        Returns generator
        Slower in traversal
        '''
        with open(self.REVIEW_DATASET_NEW) as reviews_file:
            for text in reviews_file:
                if text.strip('\n') in ['[', ',', ']']:
                    continue

                review = json.loads(text)
                if review['business_id'] == business_id:
                    yield review
        # return (review for review in ijson.items(self.review_file, 'item') if review['business_id'] == business_id)

    def get_reviews_std(self, business_id):
        '''
        DEPRECATED: DO NOT USE
        Returns a list
        Uses standard json module
        Big overhead to load data
        '''
        pass
        # print("Loading")
        # reviews = json.load(self.review_file)
        # out = [review for review in reviews if review['business_id'] == business_id]
        # print("Loaded")
        # return out


if __name__ == '__main__':
    '''
    Testing the two functions in Dataset
    '''
    i = Dataset()

    j = i.get_business_ids().__next__()

    for n in i.get_business_ids():
        for review in i.get_reviews(n):
            print(review["business_id"], review["user_id"])
        pass
    # start = time.time()
    # end = None
    # for review in i.get_reviews_std(j):
    #     end = time.time()
    #     print(review)
    #     print("Time = " + str(end - start) + " seconds")
    #     input()
    #     start = time.time()
