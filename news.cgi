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
        $week = ('??','??','ȭ','??','??','??','??') [$wday];
        if (($getmonth != $month) || ($getday != $mday)) {
            if ($getmonth !=0) { push (@log,"</LI></UL>\n"); }
            $getmonth=$month;$getday = $mday;
            push (@log,"<P><font size=\"+1\" color=\"lime\">&nbsp;<B>$month?? $mday?? ($week????)</B></font><BR>\n");
            push (@log,"<UL>\n");
        }

		if ( $w_name && $w_kind ) {
	        if ($w_kind =~ /N/) {           #???? ?迭
	            $d3 = "?????? ????" ;
	        } elsif (($w_kind =~ /A/) && ($wtai > 0)) { #ȭ?? ?迭
	            $d3 = "ȭ?쿡 ????" ;
	        } elsif (($w_kind =~ /G/) && ($wtai > 0)) { #?? ?迭
	            $d3 = "?ѿ? ????" ;
	        } elsif ($w_kind =~ /C/) {  #?????? ?迭
	            $d3 = "?????Ϳ? ????" ;
	        } elsif ($w_kind =~ /D/) {  #??ź ?迭
	            $d3 = "????" ;
	        } elsif ($w_kind =~ /S/) {  #??? ?迭
	            $d3 = "???⿡ ????" ;
	        } elsif (($w_kind =~ /B/) || (($w_kind =~ /G|A/) && ($wtai == 0))) { #???? or ź ???? ?? or ȭ?? ???? Ȱ
	            $d3 = "?б??? ????" ;
	        } else {
	            $d3 = "???ش???" ;
	        }
	    }
	    else {
	    	$d3 = "???ش???";
	    }

		if ( $host && ($getkind ne "SPEAKER") ) { $host = "\($host\)"; }
        if ($getkind eq "DEATH") {  #???? (?ڽ??? ????)
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ ???????? ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH1") { #?????????죩
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ ?ߵ??? ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH2") { #??????Ÿ?죩
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ $d3 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH3") { #??????Ÿ?죩
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ $d3 ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATH4") { #?????????Σ?
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ ?????? ??ħ?? ???? ?????̰? ???? ]</font> $host<BR>\n") ;
        } elsif ($getkind eq "DEATHAREA") { #????????????????
            push (@log,"<LI>$hour??$min?? : <font class=\"red\">???? : $w_f_name $w_l_name [ ???? ???????? ?????̰? ???? ]</font> $host<BR>\n") ;
		} elsif ($getkind eq "SPEAKER") {
			push (@log,"<LI>$hour??$min?? : <font class=\"speak\">$w_f_name $w_l_name??\(??\)??$host?????? Ȯ?????? ???ƴ?.</font><BR>\n") ;
		} elsif ($getkind =~ /WINEND/) { #?????? ????
            $log_num = pop @log;
            if ($log_num =~ /????????/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour??$min?? : <font class=12 color=\"lime\"><b>???????? : </B><BR>?????????????? : $w_f_name $w_l_name \($w_cl $w_sex $w_no??\)<br></font>\n") ;
            }
        } elsif ($getkind =~ /NOWINNER/) { #?????? ????
            $log_num = pop @log;
            if ($log_num =~ /????????/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour??$min?? : <font class=12 color=\"lime\"><b>???????? : Ÿ?Ӿƿ?</B><BR></font>\n") ;
	            $allareacheck = "1"; $allareacheck2 = "1";
            }
        } elsif ($getkind eq "EX_END") { #???α׷? ????
            $log_num = pop @log;
            if ($log_num =~ /????????/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour??$min?? : <font class=12 color=\"lime\"><b>???????? : ???α׷? ????????</B></font><BR>\n") ;
            }
        } elsif ($getkind eq "AREA") { #???? ???? ?߰?
            $log_num = pop @log;
            if (($log_num !~ /????????/)||($log_num !~ /<UL>/)){
                push (@log,$log_num);
                push (@log,"<LI>$hour??$min?? : <font color=\"lime\">???????? ?߰? : <b>$place[$ar[$w_l_name]], $place[$ar[$w_l_name+1]], $place[$ar[$w_l_name+2]]</b></font>\n");
                if ( !$allareacheck ) { push (@log,"???? ?????????? <font color=\"lime\"><b>$place[$ar[$w_f_name]], $place[$ar[$w_f_name+1]], $place[$ar[$w_f_name+2]]</b></font>.<BR>\n"); }
                $allareacheck="";
            }else{
                push (@log,$log_num);
            }
        } elsif ($getkind eq "ENTRY") { #?űԵ???
            push (@log,"<LI>$hour??$min?? : <font color=\"A0C0FF\">???? [ $w_cl $w_sex $w_no??</font><font color=yellow> $w_f_name $w_l_name</font> <font color=\"A0C0FF\">]</font><BR>\n") ;
        } elsif ($getkind eq "NEWGAME") { #?????ڿ? ???? ?????? ?ʱ?ȭ
            push (@log,"<LI><font size=\"+1\" color=\"lime\"><b>$hour??$min?? : ???ο? ???α׷? ????</b></font><BR>\n") ;
        }

        $cnt++;
    }

    for ($i=0; $i<$arealist[1]  ; $i++) {
        $ars = ($ars . " $place[$ar[$i]]") ;
    }
    $ars = "<BR><font color=\"lime\"><B>&nbsp;&nbsp;???? ????????</B></FONT><font class=red>&nbsp;$ars</font><BR>\n";
    if ( !$allareacheck2 ) { $ars = $ars . "<font color=\"lime\"><B>&nbsp;&nbsp;???? ????????</B></FONT><font color=FFFF00>&nbsp; $place[$ar[$i]], $place[$ar[$i+1]], $place[$ar[$i+2]]</font>\n"; }


    &HEADER ;
    print "</b></center>\n" ;
    print "?? BATTLE ROYALE ???? ??Ȳ ??</TD></TR><TR><TD valign=top><BR><table width=\"100%\" border=0><tr><td width=70><img src=\"http://br.dizitown.net/img/10.jpg\"></td>\n";
    print "<td valign=middle>&nbsp;$BOSS<br>???? ?????? ???õ? ?????? ?޿????? ???̱? ?ٶ???. ????????~??<br><br>&nbsp;<b>?????????? ?߰? ?ð??? $dtime?ð??̴?. (?д??? ????)</b></td></tr></table>";
    print "$ars";
    print @log;
    print "</center>\n" ;
    print "<BR>\n";

    &FOOTER;
&UNLOCK;

exit;
