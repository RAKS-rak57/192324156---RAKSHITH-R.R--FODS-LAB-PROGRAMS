import pandas as pd

df = pd.DataFrame({'ReviewID': [1, 2, 3, 4], 
                   'ReviewText': ["Great product, really loved it!", 
                                  "Good quality but too expensive.", 
                                  "Worth the price.", 
                                  "Not bad, but expected better quality."]})

df.to_csv('customer_reviews.csv', index=False)
print("Dataset saved as 'customer_reviews.csv'")
