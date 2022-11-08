#  Write a Python program to remove an empty tuple(s) from a list of tuples. 
movie_list= [("Dangle-2016"),("Drishyam-2015"),(),("KGF-2022"),(),("Barfi-2021"),("PK-2014")]
for tuple in movie_list:
    if(len(tuple)==0):
        movie_list.remove(tuple)
print(movie_list)        




