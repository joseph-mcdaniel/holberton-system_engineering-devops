# modify ULIMIT
exec { 'ULIMIT':
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  command => "sed -i -e 's/4/4096/g' -e 's/5/8000/g' /etc/security/limits.conf"
}
