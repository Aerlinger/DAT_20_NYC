#Introducing the Apriori Algorithm
*From Ed's DAT course: (https://github.com/podopie/DAT18NYC/edit/master/examples/assignment1.md)*

**Solves for:**

1. How often do items occur together in a dataset?
2. How likely are these items to occur together?

**How it works:**

The algorithm addresses the problem in two steps:

1. Identify frequent itemsets in the data.
  * *For example, in a pharmacy transaction dataset, what groups of purchases appear together frequently for customers?*
  * Note: there is a frequency minimum set by the user to improve the power of the analysis.  The lower the frequency threshold, the higher chance of a large number of rules with less strength.
2.  Mathematically describe the relationship between the different items in the itemset.
  * *For example, if a common itemset includes a toothbrush, toothpaste and mouthwash, given two of those items are were purchased, what is the probability the third will also be purchased?*

**Application Overview:**

No.| Application          | Business Question
---|----------------------|----------------------------------------------------------------
1. | CRM messenging       | How can a company optimize their customer communications?
2. | Savings offer bundle | Which products should be bundled in coupons to increase sales?
3. | Product placement    | What products should be placed together on a store shelf?

*Details:*

 1. A travel service wants to understand what other cities customers are likely to travel to based on past bookings. The company will use this analysis to tailor emails to included relevant suggestions and encourage use of the travel service.  The analysis may reveal that customers who book in San Francisco, CA and Austin, TX have a 70% probability of later booking in Portland, OR.  As a result, the service can message people who recently booked in SF and Austin about offerings in Portland, OR.
 2. A CPG company wants to boost sales of it's all-surface cleaner.  The association analysis may show that only 40% of customers who purchase paper towels and sponges also purchase the cleaner.  The CPG company can use this to include a bundle coupon where a discount is offered for the cleaner with the purchase of paper towels and sponges.
 3. A grocer wants to optimize store design and shelving for a new location.  They can use this analysis type to itentify bundles of items that should be placed near one another or in sequence throughout the store. Purchasers of frozen pizzas and hot pockets may also often buy Ben and Jerry's ice cream in 80% of cases. Based on these results, the store would want to put hot pockets, frozen pizza and Ben and Jerry's near one another within the frozens section of the store.
 