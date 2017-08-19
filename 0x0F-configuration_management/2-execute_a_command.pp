# manifest that kills a process"
$filename = /home/vagrant/holberton-system_engineering-devops/0x05-processes_and_signals/4-to_infinity_and_beyond
exec { '$(filename)':
  command => 'pkill -9 $(filename)'
}
