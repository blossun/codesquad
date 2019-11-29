############################
1단계
############################

Game객체
 - 스트라이크 / 볼 / 안타 / 아웃 결과를 저장하는 strike, ball, outs, hits 속성
 - result : 투수가 공을 던진 후 결과를 저장
 - throw() 함수 : 랜덤하게 스트라이크 / 볼 / 안타 / 아웃 네 가지 중 한 결과가 출력되고 result에 결과를 저장한다.
 - display() : 누적된 스트라이크(S), 볼(B), 아웃(O) 상황을 출력
 - updateResult() : throw()함수의 결과로 셋팅된 result 의 값에 따라 현재 진행 중인 게임의 결과를 update 및 print 한다.
  if문을 이용해 규칙1, 규칙2를 적용하여 result 를 반영한다.
  규칙1 ) 스트라이크가 3회 누적되면 1 아웃이다.
  규칙2 ) 볼이 4회 누적되면 1 안타가 된다.

main()
 - while 문을 통해 3 아웃이 나오기 전까지 경기를 계속 진행한다.
  throw() 와 updateResult() 를 진행
 - updateResult() 를 한 뒤, 게임의 결과 outs 이 3번이면 안타수를 출력하고 경기가 종료된다.
 - if문을 통해 게임 결과 안타(hits)거나 아웃(outs)면 다음 타자로 넘어가고, strike와 ball 카운트가 초기화 된다.

 
