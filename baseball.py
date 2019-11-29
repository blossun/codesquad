#-*- coding: utf-8 -*-
import math
import random

class Game():
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.outs = 0
        self.hits = 0
        self.result = ''
    def display(self):
        print("{}S {}B {}O\n".format(self.strike, self.ball, self.outs))
    def throw(self):
        result_list = ['strike', 'ball', 'outs', 'hits']
        self.result =result_list[math.floor(random.random()*len(result_list))]
    def updateResult(self):
        if(self.result == 'strike'):
            self.strike += 1
            print("스트라이크!")
            if(self.strike == 3): # 3 strike => 1 outs
                print("3 스트라이크~", end=' ')
                self.result = 'outs'
                self.strike = 0
        if(self.result == 'ball'):
            self.ball += 1
            print("볼!")
            if(self.ball == 4): #4 ball => 1 hits
                print("4볼~", end=' ')
                self.result = 'hits'
                self.ball = 0
        if(self.result == 'outs'):
            self.outs += 1
            print("아웃!", end=' ')
        if(self.result == 'hits'):
            self.hits += 1
            print("안타!", end=' ')


def main():
    print("신나는 야구 게임!\n첫 번째 타자가 타석에 입장했습니다.\n")
    round = Game()
    while(True):
        round.throw()
        round.updateResult()
        if(round.outs == 3): #3아웃이면 전체 안타수 출력 후 경기 종료
            round.display()
            print('최종 안타수: {}\n GAME OVER'.format(round.hits))
            break;
        if(round.result == 'hits' or round.result == 'outs'):
            print('다음 타자가 타석에 입장했습니다.')
            round.strike = 0
            round.ball = 0
        round.display()



if __name__ == "__main__":
    main()
