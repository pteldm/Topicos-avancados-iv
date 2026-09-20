entrada=$(tr -cd '0-9' <<< $2)
for i in {1..10}
	do
		sudo perf stat -a -x ';' -e power/energy-cores/,power/energy-pkg/,system_time,user_time,duration_time python "$1" < "$2" 2>>"resultados-melhorado-algoritmo-insertion/resultado-entrada-$entrada.csv"
	done
