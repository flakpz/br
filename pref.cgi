#!/usr/bin/perl

require "br.pl";

    #접속 금지
#	local($host) = $ENV{'REMOTE_ADDR'};
#	local($host2) = &GetHostName($ENV{'REMOTE_ADDR'});
# $host는 숫자 IP 주소. IP 블럭할때 사용. (아래 주석처리 부분)
# $host2는 도메인네임이 나오는 IP 주소. 뉴스파일에 사용.

    $host = $ENV{'REMOTE_ADDR'};

    #숫자 IP인 $host만 사용.
    local($oklist) = 0 ;
    foreach $oklist (@oklist) {
        if ($host eq $oklist) {
            $okflg = 1 ;
        }
    }

    #접속 금지 체크
    if ($okflg == 0) {
        foreach $kick (@kick) {
            if (($host =~ /$kick/)||($host eq $kick)||($host eq "")) {
                &ERROR("당신의 IP는 억세스 금지 되어 있거나\, IP를 알 수 없습니다.<BR>관리인에게 문의하세요.") ;
            }
        }
    }

    #관리 파일
    open(DB,"$area_file");seek(DB,0,0); @arealist=<DB>;close(DB);
    open(FLAG,$end_flag_file) || exit; $fl=<FLAG>; close(FLAG);

    ($y,$m,$d,$hh,$mm) = split(/,/, $arealist[0]);
    ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);
    $year+=1900;$month++;

    if (($year eq $y) && ($month eq $m) && ($mday eq $d) && ($hour >= $hh) && ($fl !~ /종료/)) { #금지 구역 추가
        ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now+(1*60*60*24));
        $year+=1900; $month++;
        $dhour = $hour + $dtime;
        $dmday = $mday - 1;
        if ( $dhour >= 24 ) {
              $dhour = $dhour - 24; $dmday = $dmday + 1;
          }    
        $newareadata[0] = ($year . "," . $month . "," . $dmday . "," . $dhour . ",0\n") ; #지역 추가 시간
        ($ar,$hackflg,$a) = split(/,/,$arealist[1]) ;
        $ar2 = $ar + 3;
        $newareadata[1] = "$ar2,0,\n" ; #금지 구역
        $newareadata[2] = $arealist[2] ;
        $newareadata[3] = $arealist[3] ;
        $newareadata[4] = $arealist[4] ;

        ($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],
            $ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],
            $ara[20],$ara[21]) = split(/,/, $arealist[4]);
        open(DB,">$area_file"); seek(DB,0,0); print DB @newareadata; close(DB);

        #금지 구역 추가 로그
        &LOGSAVE("AREAADD") ;

        open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

        for ($cnt=0; $cnt<$ar2; $cnt++) {
            for ($i=0; $i<$#userlist+1; $i++) {
                ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);
                if (($place[$w_pls] eq $place[$ara[$cnt]]) && ($w_hit > 0)&& ($w_sts ne "NPC0") && ($fl !~ /종료/)) {#금지 구역?
                    &LOGSAVE("DEATHAREA") ;
                    $w_hit=0; $w_death=$deth; $w_sts="사망";
                    $userlist[$i] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,\n" ;
                }
            }
        }
        open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

        if ($ar2 == $#ara+1) {
            open ( NEWS, "<$log_file");
            @NEWS = <NEWS>;
            ($endtime)= split(/,/, $NEWS[0]);
            ($starttime)= split(/,/, $NEWS[$#NEWS]);
            close (NEWS);

            $survivordat = "우승자없음\,전원사망";

            if (-e $survivordatfile) {
                open ( SURVIVOR, "<$survivordatfile");
                @SURVIVOR = <SURVIVOR>;
                close (SURVIVOR);
                unshift(@SURVIVOR, ("$starttime\,$endtime\,$survivordat,\n"));
                open (SURVIVOR, ">$survivordatfile");
                print SURVIVOR @SURVIVOR;
                close (SURVIVOR);
            
            &LOGSAVE("NOWINNER");
            }
        }

    } else {
        ($ar,$hackflg,$a) = split(/,/,$arealist[1]) ;
    }

($secc,$minc,$hourc,$mdaycook,$monthc,$yearc,$wdayc,$ydayc,$isdstc) = localtime($now + $save_limit*86400);
$weekcook = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') [$wdayc];
$mdaycook = "0$mdaycook" if ($mdaycook < 10);
$monthcook = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec') [$monthc];
$yearcook = $yearc+1900;
$expires = "$weekcook, $mdaycook-$monthcook-$yearcook 00:00:00 GMT";

1
