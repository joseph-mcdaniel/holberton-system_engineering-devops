# modify ULIMIT
exec { 'ULIMIT':
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  command => "sed -i 's/15/4096/g' /etc/default/nginx; service nginx restart"

}
