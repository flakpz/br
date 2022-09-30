#■ 파일 락 형식
# → 0=no 1=symlink 관수 2=mkdir 관수
# 로컬테스트 때에는 mkdir 관수를, 서버에 업했을 때에는 사용가능하다면
# symlink 관수를 사용하도록 합니다.
#$lkey = 1;
$lkey = 0;

## ----------------------------------------------------------------------------+
## BATTLE ROYALE CGI
##   (C) 2000 by Happy Ice.
##   E-MAIL: webmaster@happy-ice.com
##   HomePage: http://www.happy-ice.com/battle/
##
## ----------------------------------------------------------------------------+
## BATTLE ROYALE CGI 한글화 및 개조
##   by Ruria
##   E-MAIL: ruria@hanmir.com
##
## ----------------------------------------------------------------------------+
## BATTLE ROYALE CGI modify and customize
##   by Jason
##   E-MAIL: bluster@dizitown.net
##   HomePage: http://br.dizitown.net


## ---[주의사항]---------------------------------------------------------------+
## 1. 이 스크립트를 사용해 생기는 손해에 대해서 제작자는 일체 책임이 없습니다.
##
## 2. 설치에 관한 질문은 서포트 게시판에 부탁드립니다. 메일로 오는 질문은
##    답할 수 없습니다.
##
## 3. 개조에 관한 질문에는 일체 답할 수 없습니다.
##
## 4. 초보적인 질문에는, 일체 답하지 않습니다. 모르면 포기해 주세요.
## ----------------------------------------------------------------------------+

#■ 게임 버젼
$ver = "V01.15";

#■ 개인 버젼
$custver ="Korean + Item Plus Pack Added / Customized";

#■ 게임 타이틀
$game = "Battle Royale";

#------- 기본설정 ---------

#■ 관리자
$a_id = "protonate" ;	# NPC 사용시의 ID가 됩니다.
$a_pass = "protonate" ;

#■ 디렉토리 (마지막에 /로 끝내지 마세요)
$LOG_DIR = "./log" ; #게임 데이터
$DAT_DIR = "./dat" ; #아이템/무기/NPC 초기설정
$LIB_DIR = "./lib" ; #라이브러리

#실행(cgi) 파일
$pref_file = "pref.cgi";
$battle_file = "battle.cgi";
$attack_file = "attack.cgi";
$regist_file = "regist.cgi";
$admin_file = "admin.cgi";

#라이브러리 파일
$lib_file = "$LIB_DIR/lib.cgi";
$lib_file2 = "$LIB_DIR/lib2.cgi";
$ending_file = "$LIB_DIR/ending.cgi";
$reader_file = "$LIB_DIR/reader.cgi";
$item_lib_file = "$LIB_DIR/item.cgi";
$itemsei_lib_file = "$LIB_DIR/itemsei.cgi";
$itemgou_lib_file = "$LIB_DIR/itemgou.cgi";
$poison_file = "$LIB_DIR/poison.cgi";
$speaker_file = "$LIB_DIR/speaker.cgi";
$hack_file = "$LIB_DIR/hack.cgi";
$event_file = "$LIB_DIR/event.cgi";
$gousei_file = "$DAT_DIR/gousei_tbl.cgi";

#■ 개별 백업
$u_save_dir = "$LOG_DIR/users/"; #유저 개별 백업 디렉토리
$u_save_file = "_back.cgi"; #ID에 추가할 문자열

#■ 유저 데이터 파일
$user_file = "$LOG_DIR/userdatfile.cgi" ;
$back_file = "$LOG_DIR/userbackfile.cgi" ; #관리자가 백업

#■ 뉴스 로그 파일
$log_file = "$LOG_DIR/newsfile.cgi" ;

#■ 락 파일명
$lockf = "./lock/lock";

#■ 유저 파일
$member_file = "$LOG_DIR/memberfile.cgi" ;

#■ 금지지역 파일
$area_file = "$LOG_DIR/areafile.cgi" ;

#■ 지급무기 파일
$wep_file = "$DAT_DIR/wepfile.cgi" ;

#■ 개인 소지품 아이템 파일
$stitem_file = "$DAT_DIR/stitemfile.cgi" ;

#■ 취득 아이템 파일
$item_file = "itemfile.cgi" ;

#■ 시간 관리 파일
$time_file = "$LOG_DIR/timefile.cgi" ;

#■ 총성 로그 파일
$gun_log_file = "$LOG_DIR/gunlog.cgi" ;

#■ 종료 프래그
$end_flag_file = "e_flag.txt" ;

#우승자(생존자) 기록 파일
$survivordatfile = "$LOG_DIR/survivor.cgi";

#■ 장소
$place[0] = "분교";
$place[1] = "북쪽갑";
$place[2] = "북쪽 주택가";
$place[3] = "면사무소";
$place[4] = "우체국";
$place[5] = "소방서";
$place[6] = "관음당";
$place[7] = "시미즈 연못";
$place[8] = "서쪽 신사";
$place[9] = "호텔 자리";
$place[10] = "터널";
$place[11] = "서쪽 주택가";
$place[12] = "산악지대";
$place[13] = "절";
$place[14] = "학교";
$place[15] = "남쪽 신사";
$place[16] = "삼림지대";
$place[17] = "겐지로 연못";
$place[18] = "남쪽 주택가";
$place[19] = "요양소";
$place[20] = "등대";
$place[21] = "남쪽갑";

# SU=발견증가 SD:발견감소 DU:방어증가 DD:방어감소 AU:공격증가 AD:공격감소
@arsts = ("SU","DD","DU","SU","SD","SU","AU","SU","SD","AD",
	"DD","DU","SU","SD","AD","SD","SD","SD","AU","SU",
	"DU","SU");

@area = ("D-6","A-2","B-4","C-3","C-4","C-5","C-6","D-4","E-2","E-4",
	"E-7","F-2","F-5","F-8","G-3","G-6","H-4","H-6","I-6","I-7",
	"I-10","J-6");

@arno = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21");

@arinfo = (
	"분교다. 곧 여기는 금지지역이 되겠구나.<BR>빨리 이동하지 않으면, 목걸이가 폭발하고 만다...",
	"바다에는 배가 보인다. 탈출하려는 학생들을 감시하고 있는 정부의 배인가...",
	"전에는 여기에서도 사람이 살고 있었겠지. 지금은 폐허로 변했구나.",
	"여기가 마을의 중심인가. 지금으로서는 아무도 없는가...",
	"여기서는, 눈에 띄는 것이 없는데...",
	"소방서라곤 해도, 소방차조차 없구나.",
	"크고 작은 여러가지 불상이 모셔져 있구나. 밤에는 으시시하겠네.",
	"맑은 물이 가득 차 있구나.",
	"학문의 신들이 모셔져 있는거구나, 틀림없어.",
	"이런 장소는 유령이 자주 나올까? 유령같은건 믿지 않지만.",
	"깜깜하구나. 이런 곳에서 협공당하면 국물도 없겠군.",
	"여기도, 다른 주택가와 같이, 모두 폐허로 변했구나...",
	"이 섬을 한눈에 볼 수 있는 고지대다. 당연히 이곳에 서 있으면, 다른 곳에서도 날 발견할 가능성이 높을 것이다.",
	"모두 아주 황폐해져 있구나.",
	"낮동안의 학교라는 건 좋은 것이지만, 밤의 학교라는 것은 좋은 것이 아니군.",
	"새집도 썩어서 형편없는 모습을 드러내고 있구나.",
	"나무들이 울창하게 자라 있구나. 풀숲에서 갑자기 습격하더라도 알아채지 못할거야...",
	"여기는 연못이라기보다도, 웅덩이구나. 정말 기분 나쁜 곳이야...",
	"여기는, 다른 주택가보다, 가게가 많구나. 상점가인가 뭔가였겠지.",
	"황폐해져 있지만, 찾아보면 아직 사용할 수 있는 약 같은 것이 있을 것 같다...",
	"요새로서 점거하면, 견고한 오새가 될듯한데. 바닥에는 말라붙은 혈흔이 많이 있구나. 무슨 일이 있었던거지?",
	"병사의 배와... 우승자가 탈 배인가? 몇척의 배가 떠 있다.",
) ;

#■ 반 번호
@clas = ("3학년A반","3학년B반","3학년C반","3학년D반","3학년E반","F학년6반","G학년7반","H학년반","3학년I반","3학년J반");
$clmax = 1;	#반 숫자

$manmax=30;		#성별당 최대수

$maxmem=$clmax*$manmax*2; #최대등록인원수

$dtime=24; #금지구역추가 시간

#■플레이어의 세이브 데이터 유효기한. 날짜로 기입합니다. 디폴트로 1주일.
$save_limit = 7;

#■ 레벨업 베이스 경험치 & 증가량
$baseexp = 16;
$lvinc = 4;

#■숙련도 베이스
$BASE = 20 ;

#■프로그램 최저 개최일수
# 이벤트·덫등으로 최후의 한명이 결정되더라도, 이 날짜 이하라면 게임이 속행됩니다.
# 0으로 하면 1일.
$battle_limit = 0;

#■ 프로그램 접수마감일수
$limit = 2;

#■ 스테미너 최대치
$maxsta = 500;

#■ 응급처치 커맨드의 소비 스테미너
$okyu_sta = 50;

#■ 독 조사 커맨드의 소비 스테미너
$dokumi_sta = 20;

#■ 회복량의 설정
$kaifuku_time = 1; # 스테미너 회복시간(초) : 30초로 1포인트 회복
$kaifuku_rate = 3;  # 체력회복비율 : 스테미너의 1/x (0으로 하지 말것)

#■ 시각 (해외서버일 때는, $now=time+(9*60*60); 등으로 해 주세요. 예 : 9시간차)
$now=time;

#-------- 보안관련설정 ---------

#■ 억세스 금지 IP
@kick = (
"111.222.111.*",
"255.255.255.255",
"EndofIP");
#■ 억세스 허가 IP
@oklist = (
"TANATOS");

# 억세스금지에 대해
# IP를 얻을 수 없는 경우는 배제하고 있습니다.
# 배제하고 싶지 않은 경우, 억세스 허가 IP 주소를 넣어 주세요.
# 예 : @oklist = ("127.0.0","TANATOS","TANATOS","TANATOS");
# 이렇게하면, 127.0.0.*** 의 IP 주소는 거부되지 않습니다.
# 이용할 때는, pref.cgi의 7-21행째의 주석을 벗겨 주세요.

#■ method=POST 한정 (0=no 1=yes) → 보안대책
$Met_Post = 1;

#■ 다른 사이트에서 투고배제시의 지정 (http://부터 쓴다)
$base_url = "http://hic2004.nfori.net/br/";

#------- 선택기능 ---------

# NPC설정 유무 (0=no 1=yes)
# 설치할 경우는 base.cgi에 NPC 데이터를 작성해 주세요.
$npc_mode = 1;
$npc_num = 2;     # NPC의 수. 생존자 수 계산에서 제외。
$npc_file = "$DAT_DIR/base.cgi"; #NPC DATA FILE
$BOSS = "담임";   # 보스캐릭터 명칭(웃음)
$ZAKO = "괴물";   # 자코 캐릭터 명칭(^_^;)


# 아이콘 이미지가 있는「디렉토리」
# → URL이라면 http:// 부터 쓴다
# → 마지막에 반드시 / 로 닫는다
$imgurl = "https://github.com/flakpz/br/img/";

#맵 이미지 URL
$mapimgurl = "https://github.com/flakpz/br/img/map.jpg";

#아이콘 미리보기
$iprefile = "icon.cgi";

# 아이콘을 정의 (상하는 반드시 짝으로. 남자 아이콘을 앞, 여자 아이콘을 뒤로 해 주세요.)
@icon_file = ('0.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg','31.jpg','32.jpg','33.jpg','34.jpg','35.jpg','36.jpg','37.jpg','38.jpg','39.jpg','40.jpg','41.jpg');
@icon_name = ('남자 1번','남자 2번','남자 3번','남자 4번','남자 5번','남자 6번','남자 7번','남자 8번','남자 9번','남자 10번','남자 11번','남자 12번','남자 13번','남자 14번','남자 15번','남자 16번','남자 17번','남자 18번','남자 19번','남자 20번','남자 21번','여자 1번','여자 2번','여자 3번','여자 4번','여자 5번','여자 6번','여자 7번','여자 8번','여자 9번','여자 10번','여자 11번','여자 12번','여자 13번','여자 14번','여자 15번','여자 16번','여자 17번','여자 18번','여자 19번','여자 20번','여자 21번');
# 여자 아이콘의 처음은 몇번째? (0을 넣으면 아이콘 체크를 하지 않습니다)
# 0부터 세어 주세요.
$icon_check = 21;
# NPC 아이콘의 처음은 몇번째? (0을 넣으면 아이콘 체크를 하지 않습니다)
# 0부터 세어 주세요.
$icon_check2 = 0;

#==========　설정 여기까지 ===============
1;
