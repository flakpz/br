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
            if ($getmonth !=0) { push (@log,"\n"); }
            $getmonth=$month;$getday = $mday;
        }

		if ( $host && ($getkind ne "SPEAKER") ) { $host = "\($host\)"; }
        if ($getkind eq "SPEAKER") {
			push (@log,"\n") ;
		} elsif ($getkind =~ /WINEND/) { #우승자 결정
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@logd,"<font color=\"lime\"><B>$month월 $mday일 ($week요일) $hour시$min분 : <font color=\"lime\"><b>우승자</B><font color=\"yellow\"> $w_f_name $w_l_name</font> \($w_cl $w_sex $w_no번\)</font><br>\n") ;
            }
        } elsif ($getkind =~ /NOWINNER/) { #우승자 결정
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@logd,"<font color=\"lime\"><B>$month월 $mday일 ($week요일) $hour시$min분 : <font color=\"lime\"><b>게임 종료 (타임아웃)</B></font><br>\n") ;
	            $allareacheck = "1"; $allareacheck2 = "1";
            }
        } elsif ($getkind eq "EX_END") { #프로그램 정지
            $log_num = pop @log;
            if ($log_num =~ /게임종료/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@logd,"<B>$month월 $mday일 ($week요일) $hour시$min분 : <font color=\"lime\"><b>프로그램 긴급정지</B></font><br>\n") ;
            }
        } elsif ($getkind eq "NEWGAME") { #관리자에 의한 데이터 초기화
            push (@log,"<B>$month월 $mday일 ($week요일) $hour시$min분 : 새로운 프로그램 개시</b></font><BR>\n") ;
        }

        $cnt++;
    }
   
   print "Cache-Control: no-cache\n";
   print "Pragma: no-cache\n";
   print "Content-type: text/html\n\n";
   print "<HTML><HEAD><meta http-equiv=\"content-type\" content=\"text/html\; charset=euc-kr\"><title>$game</title><link rel=\"stylesheet\" type=\"text/css\" href=\"br.css\">\n";
   print "</HEAD><BODY topmargin=\"0\" marginheight=\"0\"><CENTER>";
   print @logd;
   print @log;
   print "</CENTER></BODY></HTML>\n";

&UNLOCK;

exit;
