import numpy as np

# 生成 10x10 的随机矩阵
matrix = np.random.rand(10, 10)

# 求每列的平均值
col_means = matrix.mean(axis=0)

print("随机矩阵：\n", matrix)
print("每列的平均值：\n", col_means)


