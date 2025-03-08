# useful.py

import os
import math
from typing import List, Tuple

# 1. 计算列表中所有数字的平均值
def calculate_average(numbers: List[float]) -> float:
    """
    计算一个数字列表的平均值。
    
    Args:
        numbers (List[float]): 包含数字的列表。
    
    Returns:
        float: 数字列表的平均值。如果列表为空，则返回 0。
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 2. 获取指定目录下的文件列表
def list_files_in_directory(directory: str) -> List[str]:
    """
    获取指定目录中的所有文件。
    
    Args:
        directory (str): 目录路径。
    
    Returns:
        List[str]: 目录中所有文件的文件名列表。如果目录不存在，则返回空列表。
    """
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


# 3. 判断一个数是否是质数
def is_prime(number: int) -> bool:
    """
    判断一个整数是否是质数。
    
    Args:
        number (int): 要判断的整数。
    
    Returns:
        bool: 如果是质数返回 True，否则返回 False。
    """
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True