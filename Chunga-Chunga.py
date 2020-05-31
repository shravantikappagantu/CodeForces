x,y,z = map(int,input().split())
coco = (x+y)//z
ans=0
if x//z + y//z == coco:
    ans  = 0
else:
    ans=min(z-(x%z),z-(y%z))
print(coco,ans)




