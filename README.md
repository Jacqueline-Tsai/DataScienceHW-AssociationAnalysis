## Association Analysis

### Preprocessing
I clean the data by dropping data with no **InvoiceNo** or **InvoiceNo begin with C** or **not located in United Kingdom** or **the item is POSTAGE**

### Implementation
pseudocode
> 	for each case X ⇒ Y:
> 		support = P(X & Y)
> 		confidence = P(X & Y) / P(X)
> 		if support > 0.01 and confidence > 0.5:
>			they are associated
		
If confidence > 0.5, that means for all people who buy X, the number of people who buy Y is more than the number of people who do not buy Y. But if confidence > 0.5 and support.
