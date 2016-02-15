from random import randint
class Card(object):
    def __init__(self,name, value, color, shape):
        self.name = name
        self.value = value
        self.color = color
        self.shape = shape
        
    def __str__(self):
        st = self.name + " " + str(self.value) + " " + self.color + " " + self.shape
        return st     
        
class Deck(object):
    def __init__(self):
        self.list = list()
        self.list.insert(0, Card("ace", 1, "red", "heart"))
        self.list.insert(1, Card("2",2, "red", "heart"))
        self.list.insert(2, Card("3",3, "red", "heart"))
        self.list.insert(3, Card("4",4, "red", "heart"))
        self.list.insert(4, Card("5",5, "red", "heart"))
        self.list.insert(5, Card("6",6, "red", "heart"))
        self.list.insert(6, Card("7",7, "red", "heart"))
        self.list.insert(7, Card("8",8, "red", "heart"))
        self.list.insert(8, Card("9",9, "red", "heart"))
        self.list.insert(9, Card("10",10, "red", "heart"))
        self.list.insert(10, Card("Jack",10, "red", "heart"))
        self.list.insert(11, Card("Queen",10, "red", "heart"))
        self.list.insert(12, Card("King",10, "red", "heart"))
        self.list.insert(13, Card("ace",1, "red", "diamond"))
        self.list.insert(14, Card("2",2, "red", "diamond"))
        self.list.insert(15, Card("3",3, "red", "diamond"))
        self.list.insert(16, Card("4",4, "red", "diamond"))
        self.list.insert(17, Card("5",5, "red", "diamond"))
        self.list.insert(18, Card("6",6, "red", "diamond"))
        self.list.insert(19, Card("7",7, "red", "diamond"))
        self.list.insert(20, Card("8",8, "red", "diamond"))
        self.list.insert(21, Card("9",9, "red", "diamond"))
        self.list.insert(22, Card("10",10, "red", "diamond"))
        self.list.insert(23, Card("Jack",10, "red", "diamond"))
        self.list.insert(24, Card("Queen",10, "red", "diamond"))
        self.list.insert(25, Card("King",10, "red", "diamond"))
        self.list.insert(26, Card("ace",1, "black", "spade"))
        self.list.insert(27, Card("2",2, "black", "spade"))
        self.list.insert(28, Card("3",3, "black", "spade"))
        self.list.insert(29, Card("4",4, "black", "spade"))
        self.list.insert(30, Card("5",5, "black", "spade"))
        self.list.insert(31, Card("6",6, "black", "spade"))
        self.list.insert(32, Card("7",7, "black", "spade"))
        self.list.insert(33, Card("8",8, "black", "spade"))
        self.list.insert(34, Card("9",9, "black", "spade"))
        self.list.insert(35, Card("10",10, "black", "spade"))
        self.list.insert(36, Card("Jack",10, "black", "spade"))
        self.list.insert(37, Card("Queen",10, "black", "spade"))
        self.list.insert(38, Card("King",10, "black", "spade"))
        self.list.insert(39, Card("ace",1, "black", "club"))
        self.list.insert(40, Card("2",2, "black", "club"))
        self.list.insert(41, Card("3",3, "black", "club"))
        self.list.insert(42, Card("4",4, "black", "club"))
        self.list.insert(43, Card("5",5, "black", "club"))
        self.list.insert(44, Card("6",6, "black", "club"))
        self.list.insert(45, Card("7",7, "black", "club"))
        self.list.insert(46, Card("8",8, "black", "club"))
        self.list.insert(47, Card("9",9, "black", "club"))
        self.list.insert(48, Card("10",10, "black", "club"))
        self.list.insert(49, Card("Jack",10, "black", "club"))
        self.list.insert(50, Card("Queen",10, "black", "club"))
        self.list.insert(51, Card("King",10, "black", "club"))
        
    def deal(self):
        return self.list.pop()
        
    def shuff(self):
        for i in range(1000):
            for j in range(51):
                tmp = self.list[j]
                rnd = randint(0,51)
                self.list[j] = self.list[rnd]
                self.list[rnd] = tmp
 
class Player(object):
    def __init__(self):
        self.cash = 100
        self.yad = Hand()
    
    def getBal(self):
        return self.cash    
    
    def hit(self, de):
        self.yad.get(de.deal)
 
class Hand(object):
    def __init__(self):
        self.lst = list()
        self.value = 0
        self.status = 0
    def get(self, card):
        self.lst.append(card)
        self.value += card.value
        
 
def main():
    print("black jack begins!")
    bsizestr = input("set bet size:")
    bsize = int(bsizestr)
    p1 = Player()
    p2 = Player()
    while p1.getBal() > 0 and p2.getBal() > 0:
        dd = Deck()
        dd.shuff()
        p1.yad = Hand()
        p2.yad = Hand()
        p1.yad.get(dd.deal())
        p1.yad.get(dd.deal())
        p2.yad.get(dd.deal())
        p2.yad.get(dd.deal())
        while p1.yad.status != 1:
            for i in range(len(p1.yad.lst)):
                print(p1.yad.lst[i])
            print("total hand value is: " + str(p1.yad.value))
            if p1.yad.value > 21:
                break    
            inp = input("press h to hit and s to stand\n")
            if inp == "h":
                p1.yad.get(dd.deal())
            else:
                p1.yad.status = 1    
             
        while p2.yad.status != 1:
            if p2.yad.value > 21:
                break    
            if p2.yad.value < 17:
                p2.yad.get(dd.deal())
            else:
                p2.yad.status = 1
                
        print("player 2 value is: " + str(p2.yad.value))        
        if (p1.yad.value > p2.yad.value and p1.yad.value < 22) or (p1.yad.value < 22 and p2.yad.value > 21):
            print("player 1 wins this round\n") 
            p1.cash += bsize
            p2.cash -= bsize   
        elif (p2.yad.value > p1.yad.value and p2.yad.value < 22) or (p2.yad.value < 22 and p1.yad.value > 21):
            print("player 2 wins this round\n") 
            p2.cash += bsize
            p1.cash -= bsize
        else:
            print("Both players lost this round\n")
    
        print ("Player1 balance : " + str(p1.cash)) 
        print ("Player2 balance : " + str(p2.cash) + "\n")
    if p1.cash > p2.cash:
        print("You won the game")
    else:
        print("You lost the game") 
        
          
    
    
            
if __name__ == '__main__': main()
   
        







        

