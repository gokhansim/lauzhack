# Lauzhack 2017
# Inspiration
As a team, we love challenging ourselves with the applications of big data. Therefore, we thought that Credit Suisse's challenge that aims to detect fraudsters on a synthetic dataset was a great fit for us. So we implemented the first challenge to come up with algorithms to find suspicious actions efficiently.

# What it does
Going through the ids in the transactions dataset, we implemented three main patterns:
- Flow pattern: Money goes from 1 person, propagate through a network of nodes and end up at another person’s account missing a small amount (payments to the intermediate nodes). All this happens in a short time range (days, hours).
- Circular pattern: Money goes from one person to another one, etc., and finally comes to the person who initiated the first payment missing a small amount (payments to the intermediate nodes). All this happens in a short time range (days, hours).
- Time pattern: Money goes from client A to client B in multiple transactions of the same amount which are equally spread in time.

These clients are detected and are visualised with the help of Neo4j.

# How we built it
We used **Python 3.x** (Jupyter Notebook to have the code organised), a powerful DigitalOcean server (the data was big!) and **Neo4j** to see our implementation results in a human-friendly way.

# Challenges we ran into 
- It was our first time with Neo4j, we spent a fair amount of time on learning it in a very detailed way. Then we figured out that we should use it only to validate the results that we find rather than finding results.
- The datasets; operating with them was quite challenging. There were invalid data rows so we had to spent some time to eliminate them or to use them for our good. Also the data was very random, for example for a fraud type, the small dataset did not contain any pattern that has more than 1000 amount of the currency involved. 

# Accomplishments we're proud of
We have implemented 3 patterns that can potentially detect fraudsters on the provided synthetic datasets.

# What's next for Find the Fraud
There can be a web application built to query possible fraudsters for a specified time period, specified people or countries. We believe that this would increase the user experience immensely.
