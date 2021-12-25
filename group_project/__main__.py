import mypackage.function as mod1
import mypackage.DATA as DATA
import mypackage.gui as GUI

def main():

    data = DATA.DATA
    DATA_hash = {}

    root = GUI.tk.Tk()
    app = GUI.Application(master=root)#Inheritクラスの継承！
    app.mainloop()

    while 1:
        print("オプションを入力してください")
        print("1:商品の表示,2:商品を賞味期限順にソートして表示,3:商品の検索,4:終了")
        Number = input()
        if Number == "1":
            mod1.output(data)
        elif Number == "2":
            mod1.sort(data)
            mod1.output(data) 
        elif Number == "3":
            mod1.make_hash(data,DATA_hash)
            mod1.search(DATA_hash)
        elif Number =="4":
            break
        else:
            print("not found")

#ちょっと変更した
if __name__ == "__main__":
    main()