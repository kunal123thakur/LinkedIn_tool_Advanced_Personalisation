# class sum:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.sum(self.x,self.y)
#     def sum(self,x,y):
#         print(x+y)



# if __name__ == "__main__":
#     sm = sum(2,4)


import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)
            self.df = df
            # print(self.df)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            print(all_tags)
    

if __name__ == "__main__":
    fs = FewShotPosts()
    pass
