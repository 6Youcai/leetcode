- [Tenth Line](https://leetcode.com/problems/tenth-line/)

```
# Read from the file file.txt and output the tenth line to stdout.
awk 'NR==10' file.txt
```

- [Valid Phone Numbers ](https://leetcode.com/problems/valid-phone-numbers/)

```
# Read from the file file.txt and output all valid phone numbers to stdout.
awk '$0 ~ /^[0-9]{3}-[0-9]{3}-[0-9]{4}$/ || $0 ~ /^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/' file.txt
```

- [Word Frequency](https://leetcode.com/problems/word-frequency/)

```
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt  | xargs -n 1 | sort  | uniq -c | awk '{print $2,$1}' | sort -k 2nr
```

- [Transpose File](https://leetcode.com/problems/transpose-file/)

```
# Read from the file file.txt and print its transposed content to stdout.
cn=`awk 'NR==1{print NF}' file.txt` && for i in $(seq 1 $cn); do sed 's/ /\t/g' file.txt | cut -f $i | xargs; done
```
