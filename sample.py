i=0
j=0
while i<10:
	while j<100:
		if j>50:
			break
		j+=1
	if i>=5:
		break
	i+=1
print(i,j)




"""
/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
SELECT * FROM BLIZZARD_ORDERS WHERE (STATUS LIKE 'PLACED' OR STATUS LIKE 'IN TRANSIT') ORDER BY ORDER_DATE, ORDER_ID LIMIT 5;
"""

^[a-z]{1,6}@hackerrank.com|^[a-z]{1,6}[_][0-9]{0,4}@hackerrank.com


^[a-z]{1,6}[_]*[0-9]{0,4}@hackerrank.com