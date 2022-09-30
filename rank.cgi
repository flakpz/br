#!/usr/bin/perl

#require "jcode.pl";
require "br.pl";
require "$lib_file";
&LOCK;
require "$pref_file";

    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    push(@log,"<TABLE border=\"1\"  cellspacing=\"0\" bordercolor=\"gray\" bordercolordark=\"gray\" bordercolorlight=\"black\">\n");
    push(@log,"<tr align=\"center\"><td>학 적</td><td width=\"70\">얼 굴</td><td>소속부</td><td>코멘트</td></tr>\n");
    $killnum = 0;
    foreach (0 .. $#userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$_]);

        if (($w_hit > 0) && ($w_sts ne "NPC0")) {
			unless ( $w_com ) {
				$w_com = "　";
			}
	    if ($w_kill > $killnum) { $killnum = $w_kill; }
            push(@log,"<tr><td align=\"center\">&nbsp;$w_f_name $w_l_name&nbsp;<br>&nbsp;$w_cl $w_sex $w_no번&nbsp;</td><td align=\"center\"><IMG src=\"$imgurl$icon_file[$w_icon]\" width=\"70\" height=\"70\" border=\"0\" align=\"absmiddle\"></td><td align=\"center\">&nbsp;$w_club&nbsp;</td><td>&nbsp;$w_com&nbsp;</td></tr>\n");
            $rnk2++;$ok++;
        } else { $ng++; }

    }
    
    push(@log,"</table><BR>\n");
    $inwon = $ng + $ok - $npc_num;
    push(@log,"총 참가 인원 $inwon명　　　 <font color=red> 생존자 $ok명 </font><br>\n");
       if ( $inwon >= 42 ) { 
         push(@logd,"최대 참가 인원에 도달했습니다. 더 이상 등록이 불가능합니다. 다음 프로그램을 기다려 주세요.</table><br>\n"); 
         push(@log,"<BR>\n"); 
    } else  { push(@log,"<BR>\n"); }

    foreach (0 .. $#userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$_]);

        if (($w_hit > 0) && ($w_sts ne "NPC0")) {
			unless ( $w_com ) {
				$w_com = "　";
			}
           if (( $w_kill == $killnum) && ( $killnum == 0 )) {
            push(@logd,"\n");
           } elsif (( $w_kill == $killnum ) && ( $killnum != 0 )) {
            push(@logd,"<table width=\"312\"><tr><td bgcolor=\"#9C1C18\" align=center>■ BATTLE ROYALE THE BEST KILLER ■</td></tr><table><table border=1 cellspacing=\"0\" bordercolor=\"gray\" bordercolordark=\"gray\" bordercolorlight=\"black\">\n");
            push(@logd,"<tr><td align=\"center\" width=\"70\"><IMG src=\"$imgurl$icon_file[$w_icon]\" border=\"0\"></td><td align=\"center\" width=\"230\">&nbsp;<font color=\"yellow\">&nbsp;$w_f_name $w_l_name</font>&nbsp;<br>&nbsp;&nbsp;$w_cl $w_sex $w_no번&nbsp;&nbsp;<br><br><font color=\"red\"><b>TOTAL $killnum KILLS</b></font></td></tr><tr><td colspan=\"2\" align=\"center\">&nbsp;$w_com&nbsp;</td></tr></table><br>\n");
           }                
        } 

    }
    
    &HEADER ;
    print "</b></center>\n" ;
    print "■ BATTLE ROYALE 생존자 일람 ■</TD></TR><TR><TD valign=top><BR><center>\n";
    print @logd;
    print @log;
    &FOOTER;
&UNLOCK;

exit;
