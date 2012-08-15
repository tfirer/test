#!/usr/bin/perl
use strict;
use warnings;

use Mail::POP3Client;

my $mail = new Mail::POP3Client('huoyan.lai@mixiu.cn','6yxzr7sk','mail.mixiu.cn');

print $mail->Count;
