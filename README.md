# pythonでビジュネル暗号とワンタイムパッドを実装する

python独学の一環で[ビジュネル暗号](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A3%E3%82%B8%E3%83%A5%E3%83%8D%E3%83%AB%E6%9A%97%E5%8F%B7)と[ワンタイムパッド](https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%B3%E3%82%BF%E3%82%A4%E3%83%A0%E3%83%91%E3%83%83%E3%83%89)を実装してみました．テキストファイルを暗号化するスクリプトです．ただし**アルファベットの小文字しか対応していません．．．**

コマンドラインで`./main.py`を呼び出して使用します．

``` bash
# examples

# ビジュネル暗号で暗号化
$./main.py --vienere <text file> <key>
# ビジュネル暗号を復号化
$./main.py --decrypt-vijnere <text file> <key>

# ワンタイムパッドで暗号化．暗号化すると鍵(pre-share-key.txt)が作成されます．
$./main.py --onetimepad <text file>

# ワンタイムパッドを復号化(暗号化の際に作成されたpre-share-key.txtを使って復号します．)
$./main.py --decrypt-otp <text file> pre-share-key.txt
```



### ビジュネル暗号で暗号化

テキストファイル`text.txt`を鍵として文字列`hullnote`で暗号化する場合

```bash
$./main.py --vigenere text.txt hullnote
```

復号化は以下のようになります

``` bash
$./main.py --decrypt-vigenere text.txt hullnote
```

### ワンタイムパッドで暗号化

テキストファイル`text.txt`を暗号化する場合

````bash
$./main.py --onetimepad text.txt
````

暗号化すると鍵(`pre-share-key.txt`)が作成されます

**復号化**の際は作成された`pre-share-key.txt`を第3引数で指定します．

```bash
$./main.py --decrypt-otp text.txt
```

復号化のあとは`pre-share-key.txt`は削除されます．

