#!/usr/bin/perl

require "br.pl";
require "$lib_file2";

&CREAD;

print "Cache-Control: no-cache\n";
print "Pragma: no-cache\n";
print "Content-type: text/html\n\n";

print <<"_HERE_";
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=euc-kr">
<title>Battle Royale</title>
<link rel="stylesheet" type="text/css" href="br.css">
</head>
<body onLoad="document.login.Id.focus()" topmargin="0" marginheight="0">
<CENTER>
<TABLE cellspacing="1" width="806">
    <TR>
      <TD valign="top" align="left">
      <TABLE width="100%" cellspacing="1">
        <TBODY>
          <TR>
            <TD align="left" valign="top" width="1%" style="margin:0; padding:0;"><IMG src="./img/index.jpg" width="300" height="200" border="0"><BR>
            <center>
            <BR>조선이란 나라에는 어떤『프로젝트』가 있다. 
            <BR>
            <BR><FONT class=red color="#9C1C18">『<b>조선 정부 전투실험 제 사십사번 프로그램</b>』</FONT>
            </center>
            <p style="margin-right:18px; margin-left:15px;">전국의 중학교 3학년 반에서 무작위로 한반을 선별. 
            클래스 메이트가<FONT class=red>『<b>최후의 한명</b>』</FONT>이 될때까지 싸운다. 최후에 살아남는 학생만이 집으로 돌아갈수 있다는<FONT class=red>『<b>살인게임</b>』</FONT>이었다.... <br>

            </TD>
            <TD valign="top" style="margin:0; padding:0;">
<TABLE width="100%" cellspacing="1">
               <TR>
                  <TD bgcolor="#9C1C18">공지사항</TD>
                </TR>
              </TBODY>
            </TABLE>
<BR><font color=yellow size="+1"><b>&nbsp;&nbsp;안녕하세요.</b></font><BR> 
                        &nbsp;&nbsp;&nbsp;&nbsp;즐겜 되세요!
<BR><BR>
            <TABLE width="100%" cellspacing="1">
                <TR>
                  <TD bgcolor="#9C1C18">Program</TD>
                </TR>
                <TR>
                  <TD>
<BR><iframe width=100% height=15 frameborder=0 scrolling=no src="notice.cgi"></iframe>
<BR>
<BR>ㆍ<A href="regist.htm"><FONT color="#ffffff" size="-1">전학/입학 수속<font size="-2">(신규등록)</font></FONT></A>
<BR>ㆍ<A href="rule.htm"><FONT color="#ffffff" size="-1">매뉴얼</FONT></A>
<BR>ㆍ<A href="rank.cgi"><FONT color="#ffffff" size="-1">생존자 리스트</FONT></A>
<BR>ㆍ<A href="news.cgi"><FONT color="#ffffff" size="-1">진행 상황</FONT></A>
<BR>ㆍ<A href="map.cgi"><FONT color="#ffffff" size="-1">대회장 지도</FONT></A>
<BR>ㆍ<A href="winner.cgi"><FONT color="#ffffff" size="-1">역대 우승자</FONT></A>
<BR>ㆍ<A href="admin.cgi"><FONT color="#ffffff" size="-1">통제실<font size="-2">(관리자모드)</FONT></FONT></A>
<BR>
<BR>
</TD>
                </TR>
                <TR>
                  <TD bgcolor="#9C1C18">등교</TD>
                </TR>
                <TR>
                  <TD>
<table width="100%">
<tr><form method="post" action="battle.cgi" name="login">
<input type="hidden" name="mode" value="main">
<td align="left" valign="middle">
<BR> &nbsp;아이디 : <input size="10" type="text" name="Id" maxlength="10" value="$c_id">&nbsp;
비밀번호 : <input size="10" type="password" name="Password" maxlength="10" value="$c_password">&nbsp;
<input type="submit" name="Enter" value="등교"><BR>
<BR>
</td>
</form>
</tr>
</table>         
<TABLE width="100%" cellspacing="1">
               <TR>
                  <TD bgcolor="#9C1C18">Communication</TD>
                </TR>
              </TBODY>
            </TABLE>
<BR>&nbsp;<BR>
                  </TD>
                </TR>
              </TBODY>
            </TABLE>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<table width=800>
<tr>
<td colspan=2 align=center bgcolor="#9C1C18">
&nbsp;
</td>
</tr>
<tr>
<td align=left>
<B><A href="http://www.happy-ice.com/battle/" target="_blank">Battle Royale $ver</A></b> <a href="#">$custver</a>
<br><a href=mailto:ruria\@hanmir.com>한글화 및 개조 by 루리아</a>
<a href=mailto:hic2002\@nazzim.net>일부 수정 by 황인철</a>
</td>
<td align=right>
<a href="http://cgi.chollian.net/~kk0117/aro/" target="_blank">Item Plus pack by Sohon</a>
<br><a href=mailto:bluster\@dizitown.net>Customized by Jason</a>
</td>
</tr>
</table>
</CENTER>
<br>
</body>
</html>
_HERE_

