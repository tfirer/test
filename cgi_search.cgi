#!/usr/bin/perl

use CGI;
use File::Find;

$base_url = 'http://10.132.64.207:10901';
@paths = qw(/home/huoyan.lai/apache2/cgi-bin  /home/huoyan.lai/apache2/cgi);
$co = new CGI;    

if (!$co->param())
{
    print $co->header,
    $co->start_html('CGI Site Search Example'),
    $co->center(
        $co->br,
        $co->h1('CGI Search'),
        $co->start_form,
        "String to search for: ",$co->textfield('key'),
        $co->p,
        $co->submit(-value=>'Search'), 
        $co->reset,
        $co->end_form
    ),
    $co->hr;

} else {
    print $co->header,
    $co->start_html('CGI Search'),
    $key = $co->param('key');
    $number_found = 0;
    @results = ();

    finddepth \&finder, @paths;

    print $co->center($co->h1("Found $number_found matches"));
    
    foreach $file (@results) {
        $file =~ s/\/home\/huoyan.lai\/apache2\///;
        print $co->a({-href => "$base_url/$file"},$file),$co->br;
    }

    print $co->end_html;
}

sub finder
{
    if ($File::Find::name =~ /$key/){
        $number_found++;
        push @results,$File::Find::name;    
    }
}

