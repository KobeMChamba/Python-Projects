N = 5
M = 5
Arr1 =  [-3, -7, 2, -6, -5]
Arr2 =  [8, 7, 3, 8, 8]
ProdArr = [
    [-24, -21, -9, -24, -24, ],
    [-56, -49, -21, -56, -56, ],
    [16, 14, 6, 16, 16, ],
    [-48, -42, -18, -48, -48, ],
    [-40, -35, -15, -40, -40, ],
]


InfoArr = [[0 for _ in range(N)] for _ in range(M)]
#InfoARR begins as 0 but gets filled in with 
#(3, [(2, -1), (1,10), (0,25)]) where the first val is the longest string possible from that point as well as its value 
# the second value in the tuple is an array that holds tuples that tell you the 
# longest strings possible from that value as well as the value it starts at

for i in range(N - 2, -1, -1):  # Start from the second-to-last row and go upwards
    for j in range(M - 2, -1, -1):  # Start from the second-to-last column and go leftwards
        # Your code to process ProdArr[i][j] goes here
        # You can access ProdArr[i][j] within this loop
        pass  # Placeholder for your processing code
        #print(ProdArr[i][j])
        if i+1<N:
            RI = InfoArr[i+1][j]
        if j+1<M:
            BI = InfoArr[i][j+1]
        if RI != 0:
            sl = max()
            if ProdArr[i][j] < InfoArr[i][j+1]: