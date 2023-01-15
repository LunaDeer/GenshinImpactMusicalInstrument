
from YsMusicalInstruments import *
from hotkey import Hotkey 

def main():
    y = YsMusicalInstruments(133,majorTremoloHarmonicaGamut)
    def 春节序曲前奏():
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])

        y.addNote(8,[".1"])
        y.addNote(8,[".1"],4,False)
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])

        y.addNote(8,[".1"])
        y.addNote(8,[".1"],4,False)
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])


        y.addNote(8,[".1"])
        y.addNote(8,["5"],4)
        y.addNote(8,["3"])
        y.addNote(8,["6"],4)

        for i in range(2):
            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["6"])
            y.addNote(8,["5"])
            y.addNote(8,["6"],4)

        # 5676
        for i in range(2):
            y.addNote([8],["5"])
            y.addNote([16],["7"],4)
            y.addNote([16],["6"])

            y.addNote([8],["5"])
            y.addNote([16],["7"],4)
            y.addNote([16],["6"])

        # 5676
        for i in range(2):
            y.addNote([16],["5"])
            y.addNote([16],["6"])
            y.addNote([16],["7"],4)
            y.addNote([16],["6"])
            y.addNote([16],["5"])
            y.addNote([16],["6"])
            y.addNote([16],["7"],4)
            y.addNote([16],["6"])

        y.addNote([8],["5"])
        y.addNote([16],["5"],4)
        y.addNote([16],["5"],4)
        y.addNote([8],["5"])
        y.addNote([8],["5"],4)
        
        y.addNote([8],["5"])
        y.addNote([16],["5"],4)
        y.addNote([16],["5"],4)
        y.addNote([8],["5"])
        y.addNote([8],["5"],4)


        y.addNote(8,["5"])
        y.addNote(16,["5"],4)
        y.addNote(16,["6"])
        y.addNote(8,["5"])
        y.addNote(16,["5"],4)
        y.addNote(16,["6"])

        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,["6"])
        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,[".2"])


        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])

        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,["6"])

        y.addNote(8,["5"])
        y.addNote(16,["5"],4)
        y.addNote(16,["6"])
        y.addNote(8,["5"])
        y.addNote(16,["5"],4)
        y.addNote(16,["6"])

        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,["6"])
        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,[".2"])

        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])

        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,["6"])

        y.addNote(8,["5"])
        y.addNote(16,["5"],4)
        y.addNote(16,["6"])
        y.addNote(8,[".1"])
        y.addNote(16,[".1"],4)
        y.addNote(16,[".2"])


        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        y.addNote(4,[".1"])

        y.addNote([32],["5"])
        y.addNote([32],["6"])
        y.addNote([32],["7"])
        y.addNote([32],[".1"],4)
        y.addNote([8],["0"])
        y.addNote([4],["3"],7)

        y.addNote([32],["5"])
        y.addNote([32],["6"])
        y.addNote([32],["7"])
        y.addNote([32],[".1"],4)
        y.addNote([8],["0"])
        y.addNote([4],["3"],7)

        y.addNote([8],[".1"])
        y.addNote([16],[".1"],4)
        y.addNote([16],["6"])
        y.addNote([8],[".1"])
        y.addNote([8],["6"],4)

        y.addNote([8],["5"])
        y.addNote([8],[".1"],4)
        y.addNote([8],["6"])
        y.addNote([8],["5"],4)

        y.addNote([8],["3"])
        y.addNote([8],["5"],4)
        y.addNote([8],["2"])
        y.addNote([8],["3"],4)

        y.addNote([8],["5"])
        y.addNote([8],["6"],4)
        y.addNote(8,["3"])
        y.addNote(16,["3"],4)
        y.addNote(16,["2"])
        
        y.addNote(8,["1"])
        y.addNote(8,["1"],4)
        y.addNote(8,[".3"])
        y.addNote(16,[".3"],4)
        y.addNote(16,[".2"])
        
        # y.addNote([4,4,4,4],[".1"],4)
        y.addNote([8],[".1"])
        y.addNote([16],[".1"],4)
        y.addNote([16],[".1"],4)
        y.addNote([8],[".1"],4)
        y.addNote([8],[".1"],4)
        y.addNote([8],[".1"])
        y.addNote([16],[".1"],4)
        y.addNote([16],[".1"],4)
        y.addNote([8],[".1"],4)
        y.addNote([8],[".1"],4)

    def 春节戏曲主旋律():
        for i in range(2):
            y.addNote([8],[".1"])
            y.addNote([16],[".1"],4)
            y.addNote([16],[".3"])
            y.addNote([8],[".2"])
            y.addNote([8],[".3"],4)

            y.addNote([8],["5"])
            y.addNote([4],["5"],4)
            y.addNote([8],[".1"],4)

            y.addNote(8,["6"])
            y.addNote(8,["5"],4)
            y.addNote(8,["3"])
            y.addNote(16,["2"],4)
            y.addNote(16,["3"])

            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["5"],4)
            y.addNote([8],["5"],4)
            y.addNote([8],["5"],4)


            y.addNote([8],[".1"])
            y.addNote([16],[".1"],4)
            y.addNote([16],[".3"])
            y.addNote([8],[".2"])
            y.addNote([8],[".3"],4)

            y.addNote([8],["5"])
            y.addNote([4],["5"],4)
            y.addNote([8],[".1"],4)
            
            y.addNote(8,["6"])
            y.addNote(8,["5"],4)
            y.addNote(8,["3"])
            y.addNote(16,["2"],4)
            y.addNote(16,["3"])

            # y.addNote([4,4],["1"])

            y.addNote([8],["1"])
            y.addNote([16],["1"],4)
            y.addNote([16],["1"],4)
            y.addNote([8],["1"],4)
            y.addNote([8],["1"],4)
        
        y.addNote(8,["6"])
        y.addMordent(8,["6","7"])
        y.addNote(8,["5"])
        y.addNote([8,8],["3"])
        y.addMordent(8,["6","7"])
        y.addNote(8,["5"])
        y.addNote([8,8],["3"])
        y.addMordent(8,["6","7"])
        y.addNote(8,["5"])
        y.addNote([8,8],["3"])
        y.addMordent(8,["6","7"])
        y.addNote(8,["5"])
        y.addNote(8,["6"])

        for i in range(3):
            y.addNote(8,["5"])
            y.addNote(8,["6"],4)
            y.addNote(8,["5"])
            y.addNote(8,["6"],4)

        y.addNote([8],["5"])
        y.addNote([16],["5"],4)
        y.addNote([16],["5"],4)
        y.addNote([8],["5"])
        y.addNote([8],["5"],4)
        
        y.addNote([8],["5"])
        y.addNote([8],["5"],4)
        y.addNote([8],["5"])
        y.addNote([8],["5"],4)


        for i in range(2):
            y.addNote([8],["3"])
            y.addNote([8],["2"],4)
            y.addNote([8],["2"])
            y.addNote([8],["3"],4)
            y.addNote([8],["5"])
            y.addNote([8],["5"])
            y.addNote([8],["5"],4)
            y.addNote([8],["6"])

            y.addNote([8],[".1"])
            y.addNote([8],[".1"],4)
            y.addNote([8],["6"])
            y.addNote([8],[".3"],4)
            y.addNote([8],[".1"])
            y.addNote([16],[".1"],4)
            y.addNote([16],[".1"],4)
            y.addNote([8],[".1"],4)
            y.addNote([8],[".1"],4)

            y.addNote([8],[".3"])
            y.addNote([8],["7"],4)
            y.addNote([8],["7"])
            y.addNote([8],["6"],4)
            y.addNote([8],["5"])
            y.addNote([8],["3"],4)
            y.addNote([8],["3"])
            y.addNote([8],["5"],4)

            y.addMordent([8,16],["6","7"])
            y.addNote(16,["5"])
            y.addNote([8],["6"])
            y.addNote([8],["6"],4)
            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["5"],4)
            y.addNote([8],["5"],4)
            y.addNote([8],["5"],4)

            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["6"])

            y.addNote([8],[".1"])
            y.addNote([8],[".1"],4)

            y.addNote([8],["6"])
            y.addNote([8],[".1"],4)
            y.addNote([8],[".1"])
            y.addMordent([8],[".2",".3"])

            y.addNote([8],["6"])
            y.addNote([8],["5"],4)
            y.addNote([8],["6"])
            y.addNote([8],["5"],4)
            y.addNote([8],["3"])
            y.addNote([16],["3"],4)
            y.addNote([16],["3"],4)
            y.addNote([8],["3"],4)
            y.addNote([8],["3"],4)

            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["6"])
            y.addNote([8],[".1"])
            y.addNote([8],[".1"],4)
            y.addMordent([8],[".2",".3"])
            y.addNote([8],[".1"])
            y.addNote([8],[".1"],4)
            y.addNote([8],["7"])

            y.addMordent([8,16],["6","7"])
            y.addNote(16,["5"])
            y.addNote([8],["6"])
            y.addNote([8],["6"],4)
            y.addNote([8],["5"])
            y.addNote([16],["5"],4)
            y.addNote([16],["5"],4)
            y.addNote([8],["5"],4)
            y.addNote([8],["5"],4)


        for i in range(2):
            y.addNote([8],["2"])
            y.addNote([16],["2"],4)
            y.addNote([16],["3"])
            y.addNote(16,["2"])
            y.addNote(16,["3"])
            y.addNote(16,["2"],4)
            y.addNote(16,["3"])

        for i in range(2):
            y.addNote([8],["4"])
            y.addNote([16],["4"],4)
            y.addNote(16,["5"])
            y.addNote(16,["4"])
            y.addNote(16,["5"])
            y.addNote(16,["4"],4)
            y.addNote(16,["5"])

    def 分解和弦小星星():
        y.addNote([8],["1","1."])
        y.addNote([8],["3."])
        y.addNote([8],["1","5."])
        y.addNote([8],["3."])

        y.addNote([8],["5","5."])
        y.addNote([8],["1"])
        y.addNote([8],["5","3"])
        y.addNote([8],["1"])


        y.addNote([8],["6","6."])
        y.addNote([8],["2"])
        y.addNote([8],["6","7."])
        y.addNote([8],["2"])

        y.addNote([8],["5","5."])
        y.addNote([8],["1"])
        y.addNote([8],["3"])
        y.addNote([8],["1"])

        
        y.addNote([8],["4","4."])
        y.addNote([8],["6."])
        y.addNote([8],["4","4."])
        y.addNote([8],["6."])

        y.addNote([8],["3","3."])
        y.addNote([8],["5."])
        y.addNote([8],["3","1"])
        y.addNote([8],["5."])

        y.addNote([8],["2","2."])
        y.addNote([8],["4."])
        y.addNote([8],["2","6."])
        y.addNote([8],["4."])

        y.addNote([8],["1","1."])
        y.addNote([8],["3."])
        y.addNote([8],["5."])
        y.addNote([8],["3."])

        

        for i in range(2):
            y.addNote([8],["5","5."])
            y.addNote([8],["1"])
            y.addNote([8],["5","3"])
            y.addNote([8],["1"])


            y.addNote([8],["4","4."])
            y.addNote([8],["6."])
            y.addNote([8],["4","4."])
            y.addNote([8],["6."])

            y.addNote([8],["3","3."])
            y.addNote([8],["5."])
            y.addNote([8],["3","1"])
            y.addNote([8],["5."])

            y.addNote([8],["2","2."])
            y.addNote([8],["4."])
            y.addNote([8],["6."])
            y.addNote([8],["4."])


        y.addNote([8],["1","1."])
        y.addNote([8],["3."])
        y.addNote([8],["1","5."])
        y.addNote([8],["3."])

        y.addNote([8],["5","5."])
        y.addNote([8],["1"])
        y.addNote([8],["5","3"])
        y.addNote([8],["1"])


        y.addNote([8],["6","6."])
        y.addNote([8],["2"])
        y.addNote([8],["6","7."])
        y.addNote([8],["2"])

        y.addNote([8],["5","5."])
        y.addNote([8],["1"])
        y.addNote([8],["3"])
        y.addNote([8],["1"])

       
        y.addNote([8],["4","4."])
        y.addNote([8],["6."])
        y.addNote([8],["4","4."])
        y.addNote([8],["6."])

        y.addNote([8],["3","3."])
        y.addNote([8],["5."])
        y.addNote([8],["3","1"])
        y.addNote([8],["5."])

        y.addNote([8],["2","2."])
        y.addNote([8],["4."])
        y.addNote([8],["2","6."])
        y.addNote([8],["4."])

        y.addNote([8],["1","1."])
        y.addNote([8],["3."])
        y.addNote([8],["5."])
        y.addNote([8],["3."])

    春节序曲前奏()
    春节戏曲主旋律()
    春节序曲前奏()

    # 分解和弦小星星()

    hotkey = Hotkey()
    hotkey.reg((win32con.MOD_ALT,ord("F")),y.cutPlayState)
    hotkey.reg((win32con.MOD_ALT,ord("P")),lambda:os._exit(0))
    hotkey.start()
    print("-------ALT+F 开始演奏/停止演奏------")
    print("-------ALT+P 退出            ------")

if __name__ == '__main__':
    main()
