ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
values=[]
desc2=dict()
desc={value : key for key, value in ascii_dict.items()}

print(desc)

for i in ascii_dict:
    z=i
    z2=ascii_dict[i]
    desc2[z2]=i
print(desc2)

rli=[i for i in ascii_dict]
rli=rli[::-1]
rdi=dict()
for i in rli:
    rdi[i]=ascii_dict[i]
print(rdi)
