d1={"prav":23}
d2={"Ash":24}
d3=dict()
for item in (d1,d2):
    d3.update(item)
print(d3)
d4=dict()

for key in d1:
    d4[key]=d1[key]
for key in d2:
    d4[key]=d2[key]

print(d4)