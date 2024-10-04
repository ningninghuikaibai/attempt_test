import numpy as np
from numpy.lib.stride_tricks import as_strided

# 创建一个10x10的矩阵
matrix = np.arange(100).reshape(10, 10)

# 定义窗口大小
window_shape = (3, 3)

# 获取原始矩阵的形状和步长
original_shape = matrix.shape
original_strides = matrix.strides

# 计算新视图的形状
view_shape = (original_shape[0] - window_shape[0] + 1,
              original_shape[1] - window_shape[1] + 1,
              *window_shape)

# 计算新视图的步长
view_strides = (original_strides[0],
                original_strides[1],
                original_strides[0],
                original_strides[1])

# 使用as_strided创建视图
blocks = as_strided(matrix, shape=view_shape, strides=view_strides)

# 输出所有3x3的子块
for i in range(blocks.shape[0]):
    for j in range(blocks.shape[1]):
        print(f"Block ({i}, {j}):")
        print(blocks[i, j])
        print()