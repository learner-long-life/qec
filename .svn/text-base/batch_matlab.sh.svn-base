#! /bin/sh

for file in E$1*.m
  do echo $file
  nice -n 20 /projects/matlab/bin/matlab -nosplash -nojvm -r "${file%.m}"
done

echo "Done!" | mail -s $(hostname) ppham
exit

