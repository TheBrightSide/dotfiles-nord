get_first_of_split() {
  read -ra ADDR <<< "$1"
  echo "${ADDR[0]}"
}

check_if_installed () {
  "command -v $($1)" &> /dev/null
  if [ $? -eq 0 ]; then
    echo "$(get_first_of_split $1) installed"
  else
    echo "$(get_first_of_split $1) not installed"
  fi
}

echo "$(check_if_installed 'bash')"
echo "$(check_if_installed 'i3')"
echo "$(check_if_installed 'dmenu')"
echo "$(check_if_installed 'alacritty')"
