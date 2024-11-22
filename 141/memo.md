# step1

- まずそもそも作法がわからなかった。
- inputとListNodeのクラスの確認を実際にしてイメージを作ることが出来なかった。
  - head.valを得れても、「で？」ってなってしまった。
- ググったらListNodeの記事がそのままあったため、見ました。
  - https://note.com/ym202110/n/n3c05bb7014a3
  - そこでイメージがついたので、解法を考えました。
- 3, 2, 0, 4, 2, 0, 4, 2, ...と続くため、一度行った地点を記憶して、そことマッチしていたらTrue
  - setで判定、判定時は次のvalがsetの中にいたらreturn
- Noneが返ってきた場合はFalseを返す
  - valだけで判断していたのが良くなかった

# step2
## 自分のコードを書き直す
- outputが合うかのみで、他の考慮も抜けていた
  - 時間計算量、空間計算量の考慮
    - O(n), O(n)
- 他の方のPR見て調査する
  - now_point.nextでも判定していたが、now_pointで判定して良い
  - 先頭で判断することでnow_pointを判定一度行ったと判定されない
    - 1回目の判定が空のsetを使うので良くないと思ってしまった
  - 変数名current, visitedの方がシンプル
  
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

```
  
# 他の人のコードを参考にする
https://github.com/katataku/leetcode/pull/1

- Fast-Slowという単語を聞いたことがない。。
  - いったん理解してみる
  - https://qiita.com/yutach/items/379b817867c4db0cbd8f
- 訪問済みの方を書き直していたので、これを参考に既存コードを直す
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

```

# step3

- 修正済みコードを書いて覚える

# step4

- レビューを元に書き直し

```python
class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False

```

```python
class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        fast, slow = head, head
        if fast is not None and fast.next is not None:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
        
```