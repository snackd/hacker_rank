# Hack Ranker 解題

###### tags: `hack`, `hack_ranker`, `code`

[個人 Hacker Rank 筆記](https://hackmd.io/@zz8yeJXcQYOjqL6CsPNdlg/rJD6sLWeh)

[Blind 75 LeetCode](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)

[Best Practice Question](https://www.techinterviewhandbook.org/best-practice-questions/)


# Solved
Day1
- [X] plus_minus
- [X] mini_max_sum
- [X] time_conversion
- [X] mock - find_median

Day2

- [X] lonely_integer
- [X] diagonal_difference
- [X] counting_sort_1
- [X] mock - find_median

Day3 

- [X] zig_zag_zequence
- [X] tower_breakers
- [X] caesar_cipher
- [ ] mock - 

Day4
- [X] grid_challenge
- [X] recusion_digit_num 
- [X] [new_year_choas](https://csanim.com/tutorials/hackerrank-solution-new-year-chaos)
- [ ] mock - 

Day5
- [X] merge_two_sorted_linked_lists
- [X] queue_use_two_stack
- [X] balance_bracket
- [ ] mock - 

Day6 
- [ ] simple_text_editor
- [ ] lego_blocks
- [ ] jesse_and_cookies
- [ ] mock - 

Day7
- [ ] tree_preorder_traversal
- [ ] tree_huffman_decoding
- [ ] no_prefix_set

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
##### 簡單輸出 Unique_list
```python=
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
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

##### 簡單遞迴：費氏數列
Functional Programming
```python=
def fib(n):                         
    if n > 1:                       
        return fib(n-1) + fib(n-2)  
    return n

n = 10
for i in range(n):                
    print(fib(i), end=',')
```
##### 最大公因數 (GCD)
```python=
def f(a, b):
    # 如果相除餘數為 0，回傳結果
    if a % b == 0:
        return b
    # 如果相除不為 0，表示還沒找到最大公因數
    else:
        return f(b, a % b)

print(f(120, 24))
```
##### 考古題練習

- [ ] 1. balance or Not
- [ ] 2. linked list creation
- [ ] 3.
- [ ] 4.



##### Interview Question

時間複雜度(time complexity)和空間複雜度(space complexity)

![](https://i.imgur.com/U3P69DP.png)


> algorithm
1.  sorting 
2.  BST
3.  stack
4.  queue
5.  binary tree
6.  hash map 


> HTTP protocol 流程和 package format

> cookie

> Linux
1. 查看記憶體
2. network package
3. service port
4. process

###### 後話：個人感言
在不依靠 Google、工具等輔助自己的情況下，真的是感到很挫折、很挫敗...
