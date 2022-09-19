# Configure server using puppet

file { 'ssh/config' :
  ensure  => file,
  path    => '~/.ssh/config',
  content => 'Host 18627-web-01\n\tHostName 18627-web-01\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school'
}
