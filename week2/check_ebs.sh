# !/bin/bash

# calculate time to move 100 submission files to and from EBS
# move to EBS
start=$(date +%s%N)
for i in {1..100}
do
    sudo cp -r submission.csv ~/ebs/submission_$i.csv
done
end=$(date +%s%N)

echo "Storing to EBS: $(($(($end-$start))/1000000)) milliseconds"
echo "Storing to EBS Average: $(($(($end-$start))/1000000/100)) milliseconds"

# move from EBS
start=$(date +%s%N)
for i in {1..100}
do
    sudo cp -r ~/ebs/submission_$i.csv ebs/submission_$i.csv
done
end=$(date +%s%N)
echo "Retrieving from EBS: $(($(($end-$start))/1000000)) milliseconds"
echo "Retrieving from EBS Average: $(($(($end-$start))/1000000/100)) milliseconds"