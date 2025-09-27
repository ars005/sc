# from fuzzywuzzy import fuzz,process
from fuzzywuzzy import fuzz,process
s1="i love fuzziing"
s2="i am loving fuzz"
print("fuzz ratio",fuzz.ratio(s1,s2))#exact match
print("fuzz partial_ratio",fuzz.partial_ratio(s1,s2))
print("Fuzzy token sort:",fuzz.token_sort_ratio(s1,s2))
print("fuzz token set:", fuzz.token_set_ratio(s1,s2))
# print("only variable",s1)
print("fuzzy WRatio",fuzz.WRatio(s1,s2))


#process library, used when we have a list of strings for matching
query= "fuzzy for fuzzys"
choices =["fuzzy for fuzzy","fuzzy fuzzy","g,for fuzzys"]
print("list of Ratios:")
print(process.extract(query,choices),"n")#get a list of matches ordered by score,default limit to 5 print"Best among the above list

