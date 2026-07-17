#!/bin/bash
classname="Banker"
testhome="./tests"
javac $classname.java

count=0
pass=0
declare -a errorList
for i in $(ls ${testhome} | egrep -i '.in' ); do
    count=$((count+1))
    testcase=${i%%.in*}
    java $classname < ${testhome}/${testcase}.in > ${testhome}/${testcase}.output
    diff "${testhome}/${testcase}.out" ${testhome}/${testcase}.output > ${testhome}/${testcase}.diff
    diffResult=$(cat ${testhome}/${testcase}.diff)
    if [ -n "$diffResult" ]
      then
        printf "x"
        errorList=( "${errorList[@]}" "${testcase}" )
      else
        printf "."
        pass=$((pass+1))
        rm ${testhome}/${testcase}.output
        rm ${testhome}/${testcase}.diff
    fi
done

printf "\ntotal $((count)), passed $((pass)).\n"

# error output
for val in "${errorList[@]}"; do
    printf  "$val "
done

if [[ "$count" -ne "$pass" ]];
  then
  echo "is not correct."
fi

# clean up
rm *.class

