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
            <BR>�����̶� ���󿡴� ���������Ʈ���� �ִ�. 
            <BR>
            <BR><FONT class=red color="#9C1C18">��<b>���� ���� �������� �� ��ʻ�� ���α׷�</b>��</FONT>
            </center>
            <p style="margin-right:18px; margin-left:15px;">������ ���б� 3�г� �ݿ��� �������� �ѹ��� ����. 
            Ŭ���� ����Ʈ��<FONT class=red>��<b>������ �Ѹ�</b>��</FONT>�� �ɶ����� �ο��. ���Ŀ� ��Ƴ��� �л����� ������ ���ư��� �ִٴ�<FONT class=red>��<b>���ΰ���</b>��</FONT>�̾���.... <br>

            </TD>
            <TD valign="top" style="margin:0; padding:0;">
<TABLE width="100%" cellspacing="1">
               <TR>
                  <TD bgcolor="#9C1C18">��������</TD>
                </TR>
              </TBODY>
            </TABLE>
<BR><font color=yellow size="+1"><b>&nbsp;&nbsp;�ȳ��ϼ���.</b></font><BR> 
                        &nbsp;&nbsp;&nbsp;&nbsp;��� �Ǽ���!
<BR><BR>
            <TABLE width="100%" cellspacing="1">
                <TR>
                  <TD bgcolor="#9C1C18">Program</TD>
                </TR>
                <TR>
                  <TD>
<BR><iframe width=100% height=15 frameborder=0 scrolling=no src="notice.cgi"></iframe>
<BR>
<BR>��<A href="regist.htm"><FONT color="#ffffff" size="-1">����/���� ����<font size="-2">(�űԵ��)</font></FONT></A>
<BR>��<A href="rule.htm"><FONT color="#ffffff" size="-1">�Ŵ���</FONT></A>
<BR>��<A href="rank.cgi"><FONT color="#ffffff" size="-1">������ ����Ʈ</FONT></A>
<BR>��<A href="news.cgi"><FONT color="#ffffff" size="-1">���� ��Ȳ</FONT></A>
<BR>��<A href="map.cgi"><FONT color="#ffffff" size="-1">��ȸ�� ����</FONT></A>
<BR>��<A href="winner.cgi"><FONT color="#ffffff" size="-1">���� �����</FONT></A>
<BR>��<A href="admin.cgi"><FONT color="#ffffff" size="-1">������<font size="-2">(�����ڸ��)</FONT></FONT></A>
<BR>
<BR>
</TD>
                </TR>
                <TR>
                  <TD bgcolor="#9C1C18">�</TD>
                </TR>
                <TR>
                  <TD>
<table width="100%">
<tr><form method="post" action="battle.cgi" name="login">
<input type="hidden" name="mode" value="main">
<td align="left" valign="middle">
<BR> &nbsp;���̵� : <input size="10" type="text" name="Id" maxlength="10" value="$c_id">&nbsp;
��й�ȣ : <input size="10" type="password" name="Password" maxlength="10" value="$c_password">&nbsp;
<input type="submit" name="Enter" value="�"><BR>
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
<br><a href=mailto:ruria\@hanmir.com>�ѱ�ȭ �� ���� by �縮��</a>
<a href=mailto:hic2002\@nazzim.net>�Ϻ� ���� by Ȳ��ö</a>
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

