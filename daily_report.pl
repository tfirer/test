#!/usr/bin/perl
use strict;
use warnings;
use Authen::SASL;
use MIME::Base64;
use Encode;
sub send_mail{
    my($to,$cc,$from,$subject,@body) = @_;
    use Net::SMTP_auth;
    my $relay = "mail.mixiu.cn";
    my $smtp = Net::SMTP_auth->new($relay,Hello=>'mixiu.cn',Debug=>1);
    die "Could not open connection:$_!" if (! defined $smtp);
    $smtp->auth('LOGIN','bin.liu@mixiu.cn','8KUjW9Lx');
    $smtp->mail($from);
    $smtp->to($to);
    $smtp->cc($cc);
    $smtp->data();
    $smtp->datasend("To: $to\n");
    $smtp->datasend("Cc: $cc\n");
    $smtp->datasend("Subject:$subject\n");
    $smtp->datasend("From:=?UTF-8?B?".encode_base64($from, '')."?=\n\n");
    $smtp->datasend("From: $from\n");
    $smtp->datasend("\n");
    for(@body){
        $smtp->datasend("$_\n");
    }
    $smtp->dataend();
    $smtp->quit;
}
my @body ;
my ($today,$tomorrow,$problem,$subject,$date);
$date = time;
my (undef ,undef ,undef ,$day,$month,$year) = localtime $date;
$month += 1;
$year += 1900;
$month = sprintf("%02d",$month);
$day = sprintf("%02d",$day);
$subject = "Liu Bin Daily Report $year/$month/$day";
print"今天工作内容：\n";
chomp($today = <STDIN>);
print"明天工作计划：\n";
chomp($tomorrow = <STDIN>);
print"今天工作所遇问题：\n";
chomp($problem = <STDIN>);
push @body, "疲れ様です。刘斌です。\n 今日の作業内容を報告致します。\n【本日行った作業】";
push @body, $today;
push @body, "【明日の予定】";
push @body, $tomorrow;
push @body, "【問題点、依頼事項】";
push @body, $problem;
send_mail('dev003@mixiu.cn','intern@mixiu.cn','刘斌 <bin.liu@mixiu.cn>',$subject,@body);
