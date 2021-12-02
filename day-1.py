#%%
## part 1
with open("day-1-input", 'r') as file: 
    depths = list( map(int, file.readlines()) )
increases = 0
window_increases = 0

for i in range(0, len(depths)-1):
    if depths[i] < depths [i+1]:
        increases += 1

print (increases)

## part 2
for i in range(0, len(depths) - 3):
    window1 = depths[i] + depths[i+1] + depths[i+2]
    window2 = depths[i+1] + depths[i+2] + depths[i+3]
    if window2 > window1:
        window_increases += 1

print (window_increases)
# %%
