# Configure client config file using puppet

file_line { 'no passwd' :
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
  replace => true
}

file_line { 'identity file' :
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
  replace => true
} 
