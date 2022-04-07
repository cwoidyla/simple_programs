PARAM1=${1:-a}  # Default = 'a'
PARAM2=${2:-b}  # Default = 'b'
PARAM3=${3:-c}  # Default = 'c'

echo "${PARAM1} ${PARAM2} ${PARAM3}"

if [[ $PARAM1 == "a" && $PARAM2 == "b" ]]; then
    echo "param1 = a and param2 = b"
elif [[ $PARAM1 == "a" || $PARAM3 == "c" ]]; then
    echo "either param1 = a or param3 = c"
else
    echo "default condition"
fi

CSVS="a,b,c,d"
CSV_VAL_ARR=$(echo $CSVS | tr "," "\n")
for CSV in $CSV_VAL_ARR
do
    echo "$CSV"
done

