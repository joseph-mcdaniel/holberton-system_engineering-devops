# manifest that kills a process"
exec { 'killmennow':
  command => "pkill -f 'killmenow'",
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
