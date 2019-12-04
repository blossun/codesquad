############################
 1단계 : 간단 야구 게임 구현하기
############################

Attack 클래스
 - 스트라이크 / 볼 / 안타 / 아웃 결과를 저장하는 strike, ball, outs, hits 속성
 - result : 투수가 공을 던진 후 결과를 저장
 - throw() 메소드 : 랜덤하게 스트라이크 / 볼 / 안타 / 아웃 네 가지 중 한 결과가 출력되고 result에 결과를 저장한다.
 - display() 메소드 : 누적된 스트라이크(S), 볼(B), 아웃(O) 상황을 출력
 - updateResult() 메소드 : throw()함수의 결과로 셋팅된 result 의 값에 따라 현재 진행 중인 게임의 결과를 update 및 print 한다.
  if문을 이용해 규칙1, 규칙2를 적용하여 result 를 반영한다.
  규칙1 ) 스트라이크가 3회 누적되면 1 아웃이다.
  규칙2 ) 볼이 4회 누적되면 1 안타가 된다.

main()
 - while 문을 통해 3 아웃이 나오기 전까지 경기를 계속 진행한다.
  throw() 와 updateResult() 를 진행
 - updateResult() 를 한 뒤, 게임의 결과 outs 이 3번이면 안타수를 출력하고 경기가 종료된다.
 - if문을 통해 게임 결과 안타(hits)거나 아웃(outs)면 다음 타자로 넘어가고, strike와 ball 카운트가 초기화 된다.


############################
 2단계 요구사항 1: 팀데이터 입력 및 저장
############################

Player 클래스
 - 각 팀에 소속될 타자 정보: 순번(turn), 이름(name), 타율(ba)을 저장한다.

Team 클래스
 - team_name : 팀 이름과 player_list : 팀에 소속된 선수들의 목록
 - inputInfo() 메소드 : 팀에 소속될 타자들의 정보를 입력받아 Player객체로 생성 후, player_list 에 저장
 - printInfo() 메소드 : 팀에 소소된 타자들의 정보를 출력

main()
 - 메뉴선택에 따라 선수 데이터를 입력하거나 출력 및 종료
 - 에러 처리 추가 : 데이터 출력 메뉴 선택 시, team 정보가 없다면 UnboundLocalError 에러 처리하여 "데이터가 없습니다." 출력
  - 에러 처리 추가 : 메뉴선택 시 숫자가 아닌 다른 값을 잘못 입력 시, ValueError 에러처리하여 "숫자를 입력해주세요." 출력 후 계속 프로그램 진행



############################
 2단계 요구사항 2: 시합하기 기능 구현
############################

Game 클래스
 - 게임에 참여하는 회초:팀1, 회말:팀2 에 대한 정보 저장
 - startGame() : 총 6회  경기 진행
 - inning() : 각 회초/ 회말별 팀의 공격진행
   3 out 시, (최종 안타수 출력 후) 공격 종료.
   안타 및 아웃 시, team.setCurrentP() 호출하여 다음 타자로 선수 교체
   Attack.throw() 호출 시 현재 타자의 타율정보를 넘겨준다.
 - updateScore() : 공격이 끝난 후 팀의 성적 업데이트
 - printResult() : 경기 종료 후, 최종결과 화면에 표시

Attack 클래스
 - throw() : 타자의 타율을 넘겨받아 타율에 따른 확률을 적용해 random으로 결과 추출
 - display() 메소드 : 경기진행 상황 스트라이크(S), 볼(B), 아웃(O) 출력
 - updateResult() 메소드 : throw()함수의 결과로 셋팅된 result 의 값에 따라 현재 진행 중인 게임의 결과를 update 한다.

main()
 - 메뉴 추가 : 3.게임시작
  경기를 진행할 두 팀 team1, team2의 정보로 Game객체 생성 후, 경기 시작

Team 클래스
 - current_player : 현재 타자 정보 (Player.turn)
 - setCurrentP() : 현재 타자 정보 업데이트. 안타 및 아웃 시 호출하여 다음 순번의 타자의 정보로 업데이트
  마지막선수인 경우 다시 첫번 순서의 타자로 셋팅
 - printCurrentP() : 현재 타자의 순번과 이름을 출력
 - inputInfo() : 선수 데이터 입력 시 잘못된 입력값에 대한 에러처리 구현





############################
3단계 요구사항 : 전광판 표시 기능 구현
############################

Board 클래스
 - display() : 경기진행 상황 전광판에 표시
 - printPlayer() : 각 팀의 선수 리스트 (번호,이름) 표시, 현재 타자 표시
 - printSBO() : 각 팀의 투구,삼진,안타 수, 현재 회초/말 타자의 SBO(스트라이크, 볼, 아웃) 카운트
 - printResult() : 타자의 타격 결과 표시
 - printTeamScore() : 두 팀의 이름, 회초 점수, 전체 누적 점수 표시

Team 클래스
 - inning_score : 각 회차 별 스코어 저장
 - team_name : 설정할 팀 이름
 - setTeamName() : 팀 이름을 설정
 - setTeamInfo() : 팀 이름과 선수 정보를 입력받아 세팅
 - inputInfo() : 기존 선수 데이터가 있으면 삭제하는 코드 추가
 - resetScore() : 경기 종료 후, 획득한 점수 초기화

Attack 클래스
 - so : 삼진아웃 카운트 (Strike Out)
 - ip : 투구 횟수 (Innings Pitched)
 - throw() : 실행될때마다 ip 카운트 +1
 - updateResult() : 3 outs 시 so 카운트 +1

Game 클래스
 - 6회말 시작 시 팀2가 승리하고 있다면 곧바로 경기가 종료
 - startGame() : 경기 최종 결과 표시 외 print 기능 삭제. updateScore에 현재 회차 정보를 넘김
 - setSkip() : skip 값과 현재 회차 값을 비교하여 같다면 skip 값을 0으로 초기화
 - updateScore() : 종료된 회차 정보를 받아서 team.inning_score에 스코어 저장
 - skip : skip할 회차값 저장, default = 0(no skip)
 - inning() : skip값이 0이면 스킵하지 않고 다음 투구보기
  skip 할 값을 입력받았다면 skip 에 값을 저장
  사용자가 값을 잘 못 입력할 시 에러처리 기능 추가
 - printResult() : 경기 종료 후 최종 결과 화면에 표시하고 점수 초기화

main
 - 데이터 입력 중 팀이름을 입력하지않고 enter시 입력문구 재출력

setSample() : 팀의 player data 샘플 설정
