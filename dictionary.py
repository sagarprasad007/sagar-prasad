##d={"First":"mango",
##   "Second":"apple",
##   "third":"bananna"}
##print(d)
####print("1st fruits is "+d[4])
####print("3rd fruits is "+d[1])
##
##for x in d:
##    print(x+"->"+d[x])
##print(d.keys())
##print(d.values())
##
####d["Fourth"]="orange"
####print(d)
##
z=d["Second"]
z=d.get("Second")
print(z)

n=d.popitem()
print(n)


n=d.popitem()
print(d)


k={"one", "two", "three"}
l=0
h=dict.fromkeys(k,l)
print(h)


x=int(input("Enter a number :"))
if x%10==0:
        print("It is even")
else:
    print("It is odd")




















