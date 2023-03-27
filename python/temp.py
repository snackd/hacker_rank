initR = 10
finalR = 8

initC = 8
finalC = 8

CostRows = [val for val in range(10)]
CostCols = [val for val in range(10)]

d_R = finalR - initR
d_C = finalC - initC

total_cost = 0

if d_R < 0:
    # print("negative")
    for i in range(1, abs(d_R) + 1):
        # print(i)
        # print(CostRows[initR - i])
        total_cost += CostRows[initR - i]
else:
    for i in range(d_R):
        total_cost += CostRows[initR + i]

if d_C < 0:
    for i in range(1, abs(d_C) + 1):
        # print(i)
        # print(CostRows[initR - i])
        total_cost += CostRows[initC - i]
else:
    for i in range(d_C):
        total_cost += CostRows[initC + i]

print(total_cost)
