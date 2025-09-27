# step1

最初の出現位置を記録する辞書と重複しているか判定する辞書を用意

重複してない文字の中で最小の出現位置を返す

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:

        appearance_dict = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        index_dict = {chr(c): 10 ** 6 for c in range(ord('a'), ord('z') + 1)}
        len_s = len(s)

        for i in range(len_s):
            target = s[i]
            appearance_dict[target] += 1
            index_dict[target] = min(i, index_dict[target])
        
        one_apper_list = [key for key, value in appearance_dict.items() if value == 1]

        if one_apper_list:
            index_value = 10 ** 6
            for c in one_apper_list:
                index_value = min(index_dict[c], index_value)
            return index_value
        else:
            return -1

```

# step2
## 読んだコード

https://github.com/Fuminiton/LeetCode/pull/15
https://github.com/quinn-sasha/leetcode/pull/15
https://github.com/t0hsumi/leetcode/pull/15
https://github.com/katataku/leetcode/pull/14
https://github.com/tarinaihitori/leetcode/pull/15

## 読んだ感想
- defaultdictを用いる方法
- Counterを用いる方法
- LRUcacheを用いる方法
- 最初と最後の出現位置が同じか判定する方法
これらを考えられるようにしたいと思った。

私は小文字アルファベットの辞書を予め作っておくことを思い浮かんだが、これだと出現順に並んでいないので、
indexを記録する辞書が必要なのかと思っていたが、最後のfor文で単純にindexのmin取れば良いと考え直した。

またdefaultdictやCounterだと出現順に並ぶので始めに1が出た時点で走査を終われる点でも良いと思った。
が、始めた時はこのことを知らなかったので、26文字定義する方法でやっていた。

26文字定義する方法は2回目のfor文時に最悪の場合でも26回で終わるので、sで回すよりも短くて良いのではと思った。

- > -1 がどのような意味を持つのかコードを見るだけだと分からないので、定数にして役割に準じた名前をつけたり、コードコメントを残すといったことをした方がいいように思いました。
  - https://github.com/Exzrgs/LeetCode/pull/9/files#r1703858740
  - > `return -1; // Not Found`
    - https://github.com/colorbox/leetcode/pull/29/files#r1861038507

## 理解すること
- Counterの挙動
- LRUcacheを用いる方法

# step3
Counterを用いた方法を練習する
```python

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_frequency = Counter(s)
        for index, c in enumerate(s):
            if char_to_frequency[c] == 1:
                return index
        return -1 # Not Found

```
