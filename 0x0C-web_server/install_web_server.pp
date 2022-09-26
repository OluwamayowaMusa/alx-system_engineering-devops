# Install web server

package { 'nginx' :
  ensure   => 'installed',
  provider => 'apt'
}
