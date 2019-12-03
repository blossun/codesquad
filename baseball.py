#-*- coding: utf-8 -*-
import math
import random
import sys
import numpy as np

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
        i=0
        while i<9:
            try:
                name, ba = input(str(i+1)+'번 타자 정보 입력> ').split(' ')
                if float(ba)>0.1 and float(ba)<0.5:
                    self.player_list.append( Player(i,name,format(float(ba),".3f")) )
                    i += 1
                else:
                    print("타율은 0.1 < h < 0.5 범위로 입력하셔야합니다.")
                    continue
            except ValueError:
                print("잘못된 입력입니다.")
                continue


    def printInfo(self): #선수 데이터 출력
        print("=====================")
        print(self.team_name+' 팀 정보')
        for i in self.player_list:
            print(str(i.turn+1)+'번 '+i.name+', '+str(i.ba))
        print()

    def setCurrentP(self): #현재 타자 정보 업데이트
        turn = self.current_player
        turn += 1
        if turn >= 9 : #마지막선수 다음은 처음 선수로
            turn = 0
        self.current_player = turn

    def printCurrentP(self): #현재 타자의 순번과 이름을 출력
        print(str(self.current_player+1)+'번 '+self.player_list[self.current_player].name)

class Game:
    def __init__(self,team1, team2):
        self.top = team1 #회초 공격 팀
        self.bottom = team2 #회말 공격 팀

    def startGame(self):
        print(self.top.team_name +' VS ' + self.bottom.team_name +'의 시합을 시작합니다.')
        for i in range(6):
            AttackTeam = self.top
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(str(i+1)+'회초 '+self.top.team_name+' 공격\n')
            result = self.inning(self.top,self.bottom)
            print('최종 안타수: {}\n'.format(result))
            self.updateScore(result,self.top)
            AttackTeam = self.bottom
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(str(i+1)+'회말 '+self.bottom.team_name+' 공격\n')
            #6회말 시작 시 팀2가 승리하고 있다면 곧바로 경기가 종료
            if(i==5 and self.top.score < self.bottom.score):
                 break
            result = self.inning(self.bottom,self.top)
            print('최종 안타수: {}\n'.format(result))
            self.updateScore(result,self.bottom)
            next = input('다음 투구 보기(enter) or 스킵하고 X회말 후 투구보기(숫자+enter) ?')
        self.printResult() #경기의 최종 결과를 화면에 표시

    def inning(self,AttackTeam,DefensiveTeam): #각 회초/ 회말별 팀의 공격진행
        round = Attack()
        displayRound = Board(AttackTeam,DefensiveTeam,round)
        while(True):
            AttackTeam.printCurrentP()
            #현재팀 타자의 타율(ba)넘겨 주기
            round.throw(AttackTeam.player_list[AttackTeam.current_player].ba)
            round.updateResult()
            displayRound.display()
            if(round.outs == 3): #3아웃이면 전체 안타수 출력 후 경기 종료
                # round.display()
                AttackTeam.setCurrentP()
                return round.hits
            if(round.result == 'hits' or round.result == 'outs'):
                print('다음 타자가 타석에 입장했습니다.')
                AttackTeam.setCurrentP()
                round.strike = 0
                round.ball = 0
            #round.display() #전광판 표시 하는 함수에 team이랑 round 둘다 넘기면 될듯
            # displayRound.display()

    def updateScore(self,result,team): #공격이 끝난 후 팀의 성적 업데이트
        if result >= 4:
            team.score += result-3

    def printResult(self):
        print("=======================================")
        print("경기 종료")
        print(self.top.team_name +' VS ' + self.bottom.team_name)
        print(str(self.top.score)+' : '+str(self.bottom.score))
        print("Thank you")
        print("=======================================")


class Attack:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.outs = 0
        self.hits = 0
        self.result = ''
        self.ip = 0 #투구회수 - Innings Pitched
        self.so = 0 #삼진아웃 - Strike Out

    def display(self): #경기진행상황 화면에 표시 --> 전광판 표시 구현하는 걸로 수정
        print("{}S {}B {}O\n".format(self.strike, self.ball, self.outs))
        print("투구 : {}\n삼진 : {}\n안타 : {}\n".format(self.ip, self.so, self.hits))

    def throw(self,ba): #타자의 타율을 넘겨받아서 random 으로 뽑기
        self.ip += 1
        result_list = ['hits','strike', 'ball', 'outs']
        #타율별 확률 구하기
        p_hits = ba
        p_strike = (1-ba)/2 - 0.05
        p_ball = (1-ba)/2 - 0.05
        p_outs = 0.1
        result_list_p = [p_hits,p_strike,p_ball,p_outs]
        self.result = np.random.choice(result_list,1,p=result_list_p)

    def updateResult(self):
        if self.result == 'strike':
            self.strike += 1; print("스트라이크!")
            if self.strike == 3: # 3 strike => 1 outs
                self.result = 'outs'
                self.strike = 0; self.so += 1
        if self.result == 'ball':
            self.ball += 1; print("볼!")
            if self.ball == 4: #4 ball => 1 hits
                self.result = 'hits'
                self.ball = 0
        if self.result == 'outs':
            self.outs += 1; print("아웃!", end=' ')
        if self.result == 'hits':
            self.hits += 1; print("안타!", end=' ')

class Board:
    def __init__(self,AttackTeam,DefensiveTeam,round):
        self.AttackTeam = AttackTeam
        self.DefensiveTeam = DefensiveTeam
        self.round = round
    def display(self):
        # print(str(self.AttackTeam.current_player+1)+'번 '+self.AttackTeam.player_list[self.AttackTeam.current_player].name)
        print("{}S {}B {}O\n".format(self.round.strike, self.round.ball, self.round.outs))
        print("투구 : {}\n삼진 : {}\n안타 : {}\n".format(self.round.ip, self.round.so, self.round.hits))

def main():
    while(True):
        print("신나는 야구 시합\n1. 데이터 입력\n2. 데이터 출력\n3. 시합 시작\n0. 종료")
        sys.stdout.write("\n 메뉴 선택 (1 - 3) ")

        #잘못된 값 입력할 경우 에러처리 구현
        try:
            choose = int(sys.stdin.readline().rstrip())
        except ValueError:
            print("숫자를 입력해주세요.\n")
            continue

        #sample player data

        team1 = Team("DOGS")
        team1.player_list.append( Player(0,"지성",0.123) )
        team1.player_list.append( Player(1,"소지섭",0.223) )
        team1.player_list.append( Player(2,"조승우",0.339) )
        team1.player_list.append( Player(3,"박서준",0.443) )
        team1.player_list.append( Player(4,"현빈",0.499) )
        team1.player_list.append( Player(5,"원빈",0.499) )
        team1.player_list.append( Player(6,"김태리",0.101) )
        team1.player_list.append( Player(7,"송혜교",0.222) )
        team1.player_list.append( Player(8,"공효진",0.333) )
        team2 = Team("CATS")
        team2.player_list.append( Player(0,"공유",0.387) )
        team2.player_list.append( Player(1,"박보검",0.111) )
        team2.player_list.append( Player(2,"노태규",0.322) )
        team2.player_list.append( Player(3,"강동원",0.487) )
        team2.player_list.append( Player(4,"조인성",0.111) )
        team2.player_list.append( Player(5,"장나라",0.222) )
        team2.player_list.append( Player(6,"아이유",0.487) )
        team2.player_list.append( Player(7,"수지",0.111) )
        team2.player_list.append( Player(8,"윤아",0.122) )

        if choose == 1:
            team_name = input("1팀의 이름을 입력하세요 >").rstrip()
            team1 = Team(team_name)
            team1.inputInfo()
            team_name = input("2팀의 이름을 입력하세요 >").rstrip()
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
            #팀정보가 없을 경우 에러처리 구현
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
