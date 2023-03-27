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
- [ ] mock - palindrome_index

Day4
- [X] grid_challenge
- [X] recusion_digit_num 
- [X] [new_year_choas](https://csanim.com/tutorials/hackerrank-solution-new-year-chaos)
- [X] mock - truck_tour

Day5
- [X] merge_two_sorted_linked_lists
- [X] queue_use_two_stack
- [X] balance_bracket
- [X] mock - pairs

Day6 
- [X] simple_text_editor
- [X] lego_blocks
- [X] jesse_and_cookies
- [X] mock - Breadth First Search_Shortest Reach

Day7
- [X] tree_preorder_traversal
- [X] tree_huffman_decoding
- [X] no_prefix_set

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



##### 資料結構記錄
Prefix 前序 ( 中 左 右 )
Infix 中序 ( 左 中 右 )
Postfix 後序 ( 左 右 中 )

記法: 看中的位置，先左在右。

##### Interview Question

時間複雜度(time complexity)和空間複雜度(space complexity)

![](https://i.imgur.com/U3P69DP.png)


> algorithm
1.  sorting 
    - [ ] [insertsort](http://alrightchiu.github.io/SecondRound/comparison-sort-insertion-sortcha-ru-pai-xu-fa.html)
    - [ ] [quicksort](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)
    - [ ] [mergesort](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
    - [ ] [heapsort](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
2.  BST ([Binary Search Tree](https://pjchender.dev/dsa/dsa-bst/))
3.  stack (FILO)
4.  queue (FIFO)
5.  [binary tree](https://web.ntnu.edu.tw/~algo/BinaryTree.html)
6.  hash map 

BFS (廣度搜尋法)
DFS (深度搜尋法)

> HTTP protocol 流程和 package format
1. 對網址進行DNS域名解析，得到對應的IP地址
2. 根據這個IP，找到對應的服務器，發起TCP的三次握手
3. 建立TCP連接後發起HTTP請求
4. 服務器響應HTTP請求，瀏覽器得到html代碼

5. 瀏覽器解析html代碼，並請求html代碼中的資源（如js、css、圖片等）（先得到html代碼，才能去找這些資源）
6. 瀏覽器對頁面進行渲染呈現給用戶
7. 服務器關閉關閉TCP連接
> cookie

使用者瀏覽網站時由網路伺服器建立並由使用者的網頁瀏覽器存放在使用者電腦或其他裝置上的小文字檔

> Linux

[ShellScipt 指令紀錄](https://hackmd.io/@zz8yeJXcQYOjqL6CsPNdlg/BJA0hWgxh)

1. [查看記憶體](https://www.ltsplus.com/linux/linux-check-ram-usage-spec)
```
free
free -g
free -m
cat /proc/meminfo
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
```
2. [network package](https://www.jinnsblog.com/2020/12/linux-netstat-network-status.html)
```
netstat -at //TCP
netstat -au //UDP

主機、連接埠
netstat -at --numeric-ports
netstat -atn 

路由表
netstat -rn

網卡
netstat -i
```
3. [service port](https://www.ltsplus.com/linux/3-way-check-linux-listen-port)
```
yum install lsof
lsof -i -P -n | grep LISTEN
lsof -i -P -n | grep :80

netstat -tulpn | grep LISTEN
netstat -tulpn | grep :80

yum install nmap
sudo nmap -sT -O localhost
```
4. [process](https://www.ltsplus.com/linux/linux-ps-show-running-processes)
```
ps aux | less
ps aux | grep rsync
ps -u apache
ps -U root -u root -N

kill -9 12345 //PID
killall -9 rsync //進程名稱
```

###### 後話：個人感言
在不依靠 Google、工具等輔助自己的情況下，真的是感到很挫折、很挫敗...
