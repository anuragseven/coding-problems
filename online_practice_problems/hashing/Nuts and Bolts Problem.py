#Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.

#Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
#The elements should follow the following order ! # $ % & * @ ^ ~ .
def matchPairs(self,nuts, bolts, n):
		symbols=[
		    '!',
		    '#',
		    '$',
		    '%',
		    '&',
		    '*',
		    '@',
		    '^',
		    '~'
		]
		symbolsToNums={s:i for i,s in enumerate(symbols)}
		numsToSymbols={i:s for i, s in enumerate(symbols)}
		
		for i in range(len(nuts)):
		    nuts[i]=symbolsToNums[nuts[i]]
		    bolts[i]=symbolsToNums[bolts[i]]
		nuts.sort()
		bolts.sort()
		
		for i in range(len(nuts)):
		    nuts[i]=numsToSymbols[nuts[i]]
		    bolts[i]=numsToSymbols[bolts[i]] 