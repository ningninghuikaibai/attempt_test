#coding:utf-8
import numpy as np

# 定义步数
num_steps = 2000
step_length = 0.5

# 生成一个包含2000个元素的数组，每个元素随机选择1或-1
steps = np.random.choice([1, -1], size=num_steps)

# 将每一步转换成实际的移动距离
actual_steps = steps * step_length

# 计算每一步之后的位置
positions = np.cumsum(actual_steps)

# 最终位置
final_position = positions[-1]

print("Final position from the origin:", final_position, "meters")
