echo "**********************"
ls -al | grep '\.py$' | grep -r "print"
echo "**********************"
grep -H 'print' *.py
echo "**********************"
uptime | awk '{print $3$4}'
