#!/usr/bin/perl -w
# Check peer certificate validity for Zabbix
# Require perl module : IO::Socket, Net::SSLeay, Date::Parse
# Require unix programs : openssl, echo, sendmail
#
# Based on sslexpire from Emmanuel Lacour <elacour@home-dn.net>
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any
# later version.
#
# This file is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file; see the file COPYING.  If not, write to the Free
# Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301, USA.
#


use strict;
use IO::Socket;
use Net::SSLeay;
use Getopt::Long;
use Date::Parse;

Net::SSLeay::SSLeay_add_ssl_algorithms();
Net::SSLeay::randomize();

# Default values
my $opensslpath = "/usr/bin/openssl";
my $host = '127.0.0.1';
my $port = '443';

my %opts;
GetOptions (\%opts,
    'host|h=s',
    'port|p=s',
    'help',
);

if ($opts{'host'}) {
    $host = $opts{'host'};
}
if ($opts{'port'}){
    $port = $opts{'port'};
}

if ($opts{'help'}) {
    &usage;
}

# Print program usage
sub usage {
    print "Usage: sslexpire [OPTION]...
-h, --host=HOST        check this host
-p, --port=TCPPORT     check this port on the previous host
    --help             print this help, then exit
";
    exit;
}

# This will return the expiration date
sub getExpire {

    my ($l_host,$l_port) = @_;
    my ($l_expdate,$l_comment);

    # Connect to $l_host:$l_port
    my $socket = IO::Socket::INET->new(
        Proto => "tcp",
        PeerAddr => $l_host,
        PeerPort => $l_port
        );
    # If we connected successfully
    if ($socket) {
        # Intiate ssl
        my $l_ctx = Net::SSLeay::CTX_new();
        my $l_ssl = Net::SSLeay::new($l_ctx);

        Net::SSLeay::set_fd($l_ssl, fileno($socket));
        my $res = Net::SSLeay::connect($l_ssl);

        # Get peer certificate
        my $l_x509 = Net::SSLeay::get_peer_certificate($l_ssl);
        if ($l_x509) {
            my $l_string = Net::SSLeay::PEM_get_string_X509($l_x509);
            # Get the expiration date, using openssl
            $l_expdate = `echo "$l_string" | $opensslpath x509 -enddate -noout 2>&1`;
            $l_expdate =~ s/.*=//;
            chomp($l_expdate);
        }
        else {
            $l_expdate = 1;
        }

        # Close and cleanup
        Net::SSLeay::free($l_ssl);
        Net::SSLeay::CTX_free($l_ctx);
        close $socket;
    }
    else {
            $l_expdate = 1;
    }
    return $l_expdate;
}


# Print remaining days before expiration
sub report {
    # Convert date into epoch using date command
    my ($l_expdate) = @_;

    if ($l_expdate ne "1") {
        # The current date
        my $l_today =  time;
        my $l_epochdate = str2time($l_expdate);

        # Calculate diff between expiration date and today
        my $l_diff = ($l_epochdate - $l_today)/(3600*24);

        # Report if needed
        printf "%.0f\n", $l_diff;
    }
    else {
        print "Unable to read certificate!\n";
        exit (1);
    }
}

# Get expiration date
my $expdate = getExpire($host,$port);

# Report
report("$expdate");
