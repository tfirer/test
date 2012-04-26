#!/usr/bin/perl
##
## auto bu dingcang
##
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Cookies;
use Encode;
use HTTP::Headers;

my $ua=LWP::UserAgent->new(keep_alive=>1);
   $ua->cookie_jar(HTTP::Cookies->new(file=>'get_page_login.cookies', autosave=>1));

main();

sub main{
    log_in();
    bu_din_cang();
}

sub log_in{
    print "login...\n";
    my $loginaccount=[
            user=>"huoyan.lai\@mixiu.cn",
            pwd=>198811120,
            x=>35,
            y=>21,
            url=>"http://10.132.64.207:9000/",
          ];
    my $res = $ua->post('http://10.132.64.207:9000/portal/auth/login_check',$loginaccount);
    if ($res->code == 302){
        printf ("login success...  code->%s : message->%s\n",$res->code,$res->message);    
    }else{
        my $string = sprintf ("login error...  code->%s : message->%s\n",$res->code,$res->message);    
        die $string;
    }
}

sub bu_din_cang{
    my $time = get_time();
    print "-----------------$time------------------\n";
    my $content = [
            number=>1,
            member_id=>86,
            order_member_id=>86,
            recipe_id=>2171,
            rest_id=>92,
            order_time=>$time,
    ];
    my $res =  $ua->post('http://10.132.64.207:9000/dingcan/recipe/save',$content);
    if ($res->code == 200 ){
        printf ("不订餐成功...  code->%s : message->%s\n",$res->code,$res->message); 
    }else{
        my $string = sprintf ("不订餐失败...  code->%s : message->%s\n",$res->code,$res->message);    
        die $string;
    }
}

sub get_time{
    my @times = localtime;
    my ($day,$mon,$year) = @times[3,4,5];
    return sprintf("%d-%02d-%02d",$year+1900,$mon+1,$day);
}
