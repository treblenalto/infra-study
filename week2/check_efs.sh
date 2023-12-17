# !/bin/bash

# calculate time to move 100 submission files to and from EFS
# move to EFS
start=$(date +%s%N)
for i in {1..100}
do
    sudo cp -r submission.csv ~/efs/submission_$i.csv
done
end=$(date +%s%N)

echo "Storing to EFS: $(($(($end-$start))/1000000)) milliseconds"
echo "Storing to EFS Average: $(($(($end-$start))/1000000/100)) milliseconds"

# move from EFS
start=$(date +%s%N)
for i in {1..100}
do
    sudo cp -r ~/efs/submission_$i.csv efs/submission_$i.csv
done
end=$(date +%s%N)
echo "Retrieving from EFS: $(($(($end-$start))/1000000)) milliseconds"
echo "Retrieving from EFS Average: $(($(($end-$start))/1000000/100)) milliseconds"