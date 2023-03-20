# Hack Ranker 解題

###### tags: `hack`, `hack_ranker`, `code`

[個人 Hacker Rank 筆記](https://hackmd.io/@zz8yeJXcQYOjqL6CsPNdlg/rJD6sLWeh)

[Blind 75 LeetCode](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)

# Solved
Day1
- [X] plus_minus
- [X] mini_max_sum
- [X] time_conversion
- [X] Mock Test - find_median

Day2

- [X] lonely_integer
- [X] diagonal_difference
- [X] counting_sort_1
- [X] Mock Test - find_median

Day3 

- [X] zig_zag_zequence
- [X] tower_breakers
- [X] caesar_cipher
- [ ] Mock Test - 


#### 編輯環境

> 在 Win10，使用 VSCode 編輯與編譯，使用 Python Extension Debug 跟測試

![VSCode](https://i.imgur.com/C8l3AoW.png)


#### 取得當前資料夾名稱
```python==
fold_path = os.path.abspath(os.getcwd())
```
#### 取得當前檔案名稱
```python==
file_name = os.path.basename(__file__)[:-3] + '.txt'
```
#### 絕對路徑
幫助我快速建置環境:測試或 Debug
```python==
abs_path = fold_path + "\\" + file_name
os.environ['OUTPUT_PATH'] = abs_path
```

##### 簡單逆轉字串

```=python
s = "hello"


def reverse_slicing(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: list
    """
    result = s[::-1]
    return result


def reverse_list(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    temp_list = list(s)
    temp_list.reverse()
    result = ''.join(temp_list)
    return result


def reverse_join_reversed_iter(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    s1 = ''.join(reversed(s))
    return s1


def reverse_for_loop(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    result = ""
    for c in s:
        # appending chars in reverse order
        result = c + result

    return result


print(reverse_s)
print(reverse_list(s))
print(reverse_join_reversed_iter(s))
print(reverse_for_loop(s))
```
