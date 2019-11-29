#-*- coding: utf-8 -*-
import math
import random
import sys

class Player: #타자 정보
    def __init__(self,turn,name,ba):
        self.turn = turn
        self.name = name
        self.ba = ba #Batting average

class Team: #팀 정보
    def __init__(self,team_name):
        self.team_name = team_name
        self.player_list = []

    def inputInfo(self): #선수 데이터 입력
        for i in range(9): 
            print(str(i+1)+'번 타자 정보 입력> ')
            name, ba = sys.stdin.readline().rstrip().split(' ')
            self.player_list.append( Player(i,name,ba) );


    def printInfo(self): #선수 데이터 출력
        print("=====================")
        print(self.team_name+' 팀 정보')
        for i in self.player_list:
            print(str(i.turn+1)+'번 '+i.name+', '+str(i.ba))
        print()

class Game:
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
    while(True):
        print("신나는 야구 시합\n1. 데이터 입력\n2. 데이터 출력\n0. 종료")
        # print("메뉴선택 ( 1 - 2) ", end=' ')
        sys.stdout.write("\n 메뉴 선택 (1 - 2) ")
        choose = int(sys.stdin.readline().rstrip())

        '''
        #sample player data
        team1 = Team("Team01")
        team1.player_list.append( Player(0,"지성",0.123) )
        team1.player_list.append( Player(1,"소지섭",0.323) )
        team1.player_list.append( Player(2,"조승우",0.989) )
        team2 = Team("Team02")
        team2.player_list.append( Player(0,"공유",0.987) )
        team2.player_list.append( Player(0,"박보검",0.1111) )
        team2.player_list.append( Player(0,"노태규",0.922) )
        '''
        if choose == 1:
            # print("1팀의 이름을 입력하세요> ")

            sys.stdout.write("\n 1팀의 이름을 입력하세요 > ")
            team_name = sys.stdin.readline().rstrip()
            team1 = Team(team_name)
            team1.inputInfo()
            sys.stdout.write("\n 2팀의 이름을 입력하세요 > ")
            team_name = sys.stdin.readline().rstrip()
            team2 = Team(team_name)
            team2.inputInfo()
            print("팀 데이터 입력이 완료되었습니다.\n")
        elif choose == 2:
            #팀정보가 없을 경우 에러처리 구현
            try:
                team1.printInfo()
                team2.printInfo()
            except UnboundLocalError:
                print("데이터가 없습니다.\n")
                continue
        elif choose == 0:
            print('종료')
            break
        else:
            print("잘못 입력하셨습니다. 0-2 중에서 입력해주세요.")

'''
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
'''


if __name__ == "__main__":
    main()
