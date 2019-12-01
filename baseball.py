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
        self.score = 0 #득점
        self.current_player = 0 #현재 타자

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

    def setCurrentP(self):
        turn = self.current_player
        turn += 1
        if turn >= 9 : #마지막선수 다음은 처음 선수로
            turn = 0
        self.current_player = turn

    def printCurrentP(self):
        print(str(self.current_player+1)+'번 '+self.player_list[self.current_player].name)

class Game:
    def __init__(self,team1, team2):
        self.top = team1 #회초
        self.bottom = team2 #회말

    def startGame(self):
        print(self.top.team_name +' VS ' + self.bottom.team_name +'의 시합을 시작합니다.')
        for i in range(6):
            print("+++++++++++++++++++++++++++++++++++++++")
            print(str(i+1)+'회초 '+self.top.team_name+' 공격\n')
            result = self.inning(self.top)
            print('최종 안타수: {}\n GAME OVER'.format(result))
            self.updateScore(result,self.top)
            print("+++++++++++++++++++++++++++++++++++++++")
            print(str(i+1)+'회말 '+self.bottom.team_name+' 공격\n')
            result = self.inning(self.bottom)
            print('최종 안타수: {}\n GAME OVER'.format(result))
            self.updateScore(result,self.bottom)
        self.printResult()

    def inning(self,team):
        # team : 공격 순서인 팀
        round = Attack() #공격결과 hits count만 가져와서 득점 추가?
        # next_player = 1
        while(True):
            """
            if next_player == 1 : #아웃 안타로 다음 선수 입장 여부 확인
                i += 1
                i = self.team.setCurrentP(i) #아예 현재 선수 셋팅하고 print 하는걸로 수정
                next_player = 0
            """
            team.printCurrentP()
            round.throw()
            round.updateResult()
            if(round.outs == 3): #3아웃이면 전체 안타수 출력 후 경기 종료
                round.display()
                team.setCurrentP()
                return round.hits
                # break;
            if(round.result == 'hits' or round.result == 'outs'):
                print('다음 타자가 타석에 입장했습니다.')
                # next_player = 1
                team.setCurrentP()
                round.strike = 0
                round.ball = 0
            round.display()
    def updateScore(self,result,team):
        if result >= 4:
            team.score += result-3
    def printResult(self):
        print("=======================================")
        print("경기 종료")
        print(self.top.team_name +' VS ' + self.bottom.team_name)
        print(str(self.top.score)+' : '+str(self.bottom.score))
        print("Thank you")
        print("=======================================")


class Attack: #Inning->attack ?
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
        #self.result =result_list[math.floor(random.random()*len(result_list))]
        self.result = random.choice(result_list)
    def updateResult(self):
        if self.result == 'strike':
            self.strike += 1
            print("스트라이크!")
            if self.strike == 3: # 3 strike => 1 outs
                # print("3 스트라이크~", end=' ')
                self.result = 'outs'
                self.strike = 0
        if self.result == 'ball':
            self.ball += 1
            print("볼!")
            if self.ball == 4: #4 ball => 1 hits
                # print("4볼~", end=' ')
                self.result = 'hits'
                self.ball = 0
        if self.result == 'outs':
            self.outs += 1
            print("아웃!", end=' ')
        if self.result == 'hits':
            self.hits += 1
            print("안타!", end=' ')


def main():
    while(True):
        print("신나는 야구 시합\n1. 데이터 입력\n2. 데이터 출력\n3. 시합 시작\n0. 종료")
        # print("메뉴선택 ( 1 - 2) ", end=' ')
        sys.stdout.write("\n 메뉴 선택 (1 - 3) ")

        try:
            choose = int(sys.stdin.readline().rstrip())
        except ValueError:
            print("숫자를 입력해주세요.\n")
            continue

        #sample player data
        """
        team1 = Team("DOGS")
        team1.player_list.append( Player(0,"지성",0.123) )
        team1.player_list.append( Player(1,"소지섭",0.323) )
        team1.player_list.append( Player(2,"조승우",0.989) )
        team1.player_list.append( Player(3,"박서준",0.123) )
        team1.player_list.append( Player(4,"현빈",0.323) )
        team1.player_list.append( Player(5,"원빈",0.989) )
        team1.player_list.append( Player(6,"김태리",0.123) )
        team1.player_list.append( Player(7,"송혜교",0.323) )
        team1.player_list.append( Player(8,"공효진",0.989) )
        team2 = Team("CATS")
        team2.player_list.append( Player(0,"공유",0.987) )
        team2.player_list.append( Player(1,"박보검",0.1111) )
        team2.player_list.append( Player(2,"노태규",0.922) )
        team2.player_list.append( Player(3,"강동원",0.987) )
        team2.player_list.append( Player(4,"조인성",0.1111) )
        team2.player_list.append( Player(5,"장나라",0.922) )
        team2.player_list.append( Player(6,"아이유",0.987) )
        team2.player_list.append( Player(7,"수지",0.1111) )
        team2.player_list.append( Player(8,"윤아",0.922) )
        """
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
        elif choose == 3:
            try:
                game = Game(team1, team2)
                game.startGame()
            except UnboundLocalError:
                print("데이터가 없습니다.\n")
                continue
        elif choose == 0:
            print('종료')
            break
        else:
            print("잘못 입력하셨습니다. 0-3 중에서 입력해주세요.\n")






if __name__ == "__main__":
    main()
