# Hack Ranker 解題

###### tags: `hack`, `hack_ranker`, `code`

[個人 Hacker Rank 筆記](https://hackmd.io/@zz8yeJXcQYOjqL6CsPNdlg/rJD6sLWeh)

# Solved
Day1
- [X] plus_minus
- [X] mini_max_sum
- [X] time_conversion

Day2

- [X] lonely_integer
- [X] diagonal_difference
- [X] counting_sort_1

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
