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

my $res = $ua->get('http://10.132.64.227/html5/binLiu.htm');
print $res->content;
aaaaa
