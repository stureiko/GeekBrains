#!/bin/bash
echo
echo "Task 1 - вывести 3-и раза имя пользователя"
n=3
while [ $n -gt 0 ]
do
    echo $USER
    (( n -= 1 ))
done

echo "*********************************************"
echo
echo "Task 2 - вывести все четные числа от 0 до 100"
count=0
while [ $count -lt 101 ]
do
    if (( $count%2 == 0 )); then
        echo $count
    fi
    (( count+=1 ))
done

