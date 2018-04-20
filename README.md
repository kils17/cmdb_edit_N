## CMDB edit tool for N

## logic
dic.csv (argv[1]) 파일을 읽어서 list 객체(dic)에 저장하고
svr.csv (argv[2]) 파일을 읽어서 list 객체(svr)에 저장하고
svr list에 있는 ip 주소를 dic 의 2번째 컬럼인 IP에서 첫번째 매칭되는 행을 output.csv에 기록한다.

UTF-8 을 기반으로 수행된다.

## how to use
Usage: python cmdb.py {dicfile} {srvfile}

dicfile은 고객에게 받아서 수동으로 맞추고
srvfile은 User App으로 생성한다.

dicfile과 srvfile의 컬럼 수가 정확히 일치해야 한다.
