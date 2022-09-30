#!/usr/bin/perl

#require "jcode.pl";
require "br.pl";
require "$lib_file";
&LOCK;
require "$pref_file";



    open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

    ($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21],$ar[22]) = split(/,/, $arealist[4]);

    $getmonth=$getday=0;
    foreach $loglist(@loglist) {
        ($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$host,$w_name,$w_kind,$wtai)= split(/,/, $loglist);
        ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($gettime);
        $hour = "0$hour" if ($hour < 10);
        $min = "0$min" if ($min < 10);  $month++;
        $year += 1900;
        $week = ('일','월','화','수','목','금','토') [$wday];
        if (($getmonth != $month) || ($getday != $mday)) {
            if ($getmonth !=0) { push (@log,"</LI></UL>\n"); }
            $getmonth=$month;$getday = $mday;
            push (@log,"<P><font size=\"+1\" color=\"lime\">&nbsp;<B>$month월 $mday일 ($week요일)</B></font><BR>\n");
            push (@log,"<UL>\n");
        }

		if ( $w_name && $w_kind ) {
	        if ($w_kind =~ /N/) {           #베기 계열
	            $d3 = "흉기로 베임" ;
	        } elsif (($w_kind =~ /A/) && ($wtai > 0)) { #화살 계열
	            $d3 = "화살에 맞음" ;
	        } elsif (($w_kind =~ /G/) && ($wtai > 0)) { #총 계열
	            $d3 = "총에 맞음" ;
	        } elsif ($w_kind =~ /C/) {  #던지기 계열
	            $d3 = "던진것에 맞음" ;
	        } elsif ($w_kind =~ /D/) {  #폭탄 계열
	            $d3 = "폭발" ;
	        } elsif ($w_kind =~ /S/) {  #찌르기 계열
	            $d3 = "흉기에 찔림" ;
	        } elsif (($w_kind =~ /B/) || (($w_kind =~ /G|A/) && ($wtai == 0))) { #곤봉 or 탄 없는 총 or 화살 없는 활
	            $d3 = "둔기로 맞음" ;
	        } else {
	            $d3 = "살해당함" ;
	        }
	    }
	    else {
	    	$d3 = "살해당함";
	    }

		if ( $host && ($getkind ne "SPEAKER") ) { $host = "\($host\)"; }
        if ($getkind eq "DEATH") {  #사망 (자신이 원인)
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ 사고당함 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH1") { #사망（독살）
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ 중독됨 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH2") { #사망（타살）
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ $d3 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH3") { #사망（타살）
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ $d3 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH4") { #사망（정부）
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ 정부의 지침을 어겨 목걸이가 폭발 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATHAREA") { #사망（금지지역）
            push (@log,"<LI>$hour시$min분 : <font class=\"red\">사망 : $w_f_name $w_l_name [ 금지 지역에서 목걸이가 폭발 ]</font> $host<BR>\n") ;
		} elsif ($getkind eq "SPEAKER") {
			push (@log,"<LI>$hour시$min분 : <font class=\"speak\">$w_f_name $w_l_name이\(가\)『$host』라고 확성기로 외쳤다.</font><BR>\n") ;
		} elsif ($getkind =~ /WINEND/) { #우승자 결정
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour시$min분 : <font class=12 color=\"lime\"><b>게임종료 : </B><BR>　　　　우승자 : $w_f_name $w_l_name \($w_cl $w_sex $w_no번\)<br></font>\n") ;
            }
        } elsif ($getkind =~ /NOWINNER/) { #우승자 결정
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour시$min분 : <font class=12 color=\"lime\"><b>게임종료 : 타임아웃</B><BR></font>\n") ;
	            $allareacheck = "1"; $allareacheck2 = "1";
            }
        } elsif ($getkind eq "EX_END") { #프로그램 정지
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour시$min분 : <font class=12 color=\"lime\"><b>게임종료 : 프로그램 긴급정지</B></font><BR>\n") ;
            }
        } elsif ($getkind eq "AREA") { #금지 구역 추가
            $log_num = pop @log;
            if (($log_num !~ /게임종료/)||($log_num !~ /<UL>/)){
                push (@log,$log_num);
                push (@log,"<LI>$hour시$min분 : <font color=\"lime\">금지지역 추가 : <b>$place[$ar[$w_l_name]], $place[$ar[$w_l_name+1]], $place[$ar[$w_l_name+2]]</b></font>\n");
                if ( !$allareacheck ) { push (@log,"다음 금지지역은 <font color=\"lime\"><b>$place[$ar[$w_f_name]], $place[$ar[$w_f_name+1]], $place[$ar[$w_f_name+2]]</b></font>.<BR>\n"); }
                $allareacheck="";
            }else{
                push (@log,$log_num);
            }
        } elsif ($getkind eq "ENTRY") { #신규등록
            push (@log,"<LI>$hour시$min분 : <font color=\"A0C0FF\">전입 [ $w_cl $w_sex $w_no번</font><font color=yellow> $w_f_name $w_l_name</font> <font color=\"A0C0FF\">]</font><BR>\n") ;
        } elsif ($getkind eq "NEWGAME") { #관리자에 의한 데이터 초기화
            push (@log,"<LI><font size=\"+1\" color=\"lime\"><b>$hour시$min분 : 새로운 프로그램 개시</b></font><BR>\n") ;
        }

        $cnt++;
    }

    for ($i=0; $i<$arealist[1]  ; $i++) {
        $ars = ($ars . " $place[$ar[$i]]") ;
    }
    $ars = "<BR><font color=\"lime\"><B>&nbsp;&nbsp;현재 금지지역</B></FONT><font class=red>&nbsp;$ars</font><BR>\n";
    if ( !$allareacheck2 ) { $ars = $ars . "<font color=\"lime\"><B>&nbsp;&nbsp;다음 금지지역</B></FONT><font color=FFFF00>&nbsp; $place[$ar[$i]], $place[$ar[$i+1]], $place[$ar[$i+2]]</font>\n"; }


    &HEADER ;
    print "</b></center>\n" ;
    print "■ BATTLE ROYALE 진행 상황 ■</TD></TR><TR><TD valign=top><BR><table width=\"100%\" border=0><tr><td width=70><img src=\"http://br.dizitown.net/img/10.jpg\"></td>\n";
    print "<td valign=middle>&nbsp;$BOSS<br>『자 여러분 오늘도 힘내서 급우들을 죽이기 바란다. 힘내라구~』<br><br>&nbsp;<b>금지구역의 추가 시간은 $dtime시간이다. (분단위 버림)</b></td></tr></table>";
    print "$ars";
    print @log;
    print "</center>\n" ;
    print "<BR>\n";

    &FOOTER;
&UNLOCK;

exit;
