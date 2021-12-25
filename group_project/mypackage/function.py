
#商品リストの表示を行う関数
def output(DATA):
    for i in DATA:
        print(i)

#商品リストを賞味期限順にソートする関数
def sort(DATA):
    for c in range(4,1,-1):
            for i in range(len(DATA)):
                for j in range(len(DATA)-1, i, -1):
                    if DATA[j][c] < DATA[j-1][c]:
                        DATA[j], DATA[j-1] = DATA[j-1], DATA[j]

#データハッシュを作る関数
def make_hash(DATA,DATA_hash):
    for i in range(len(DATA)):
        DATA_hash[DATA[i][0]] = DATA[i]

#商品名を入力するとリストから情報を探す関数
def search(DATA_hash):
    string = input("検索したい商品を入力してください\n")
    if DATA_hash.get(string) is None:
        print("not found")
    else:
        print(DATA_hash.get(string))