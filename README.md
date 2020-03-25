# rest_to_hyper
Provides a framework for automatically building and publishing Tableau Data Sources based on RESTful data.

## What does this code do?
There are four main functionalities of this code:
- Pulling data from a GET call and storing the results as nested lists
- Dynamically creating a hyper instance and defining columns
- Swapping a .hyper file in a Tableau Data Source (.tds)
- Publishing the .tds to Tableau Server (or Online)

The different functionalities are divided into separate python files and methods with the goal of creating modular pieces that can be leveraged in other workflows.

## Why did I make this?
Well, good question. It started out as a pet project to get more information about who was in a Slack channel I am an admin of. I ended up deciding that I thought the code was useful and would be worth sharing out to the world! The general idea is to try and lower the barrier to entry for anyone trying to access data in the web and keep it fresh in Tableau. I think that this methodology (although not perfect, please don't run this at your enterprise without a CR!) is more flexible than a WDC and is certainly cheaper than paying a partner to pipe the data around.


## How do I get started?
First, give it a clone and try running main.py! It should work right out of the box. When you are ready to start implementing your own version of the code, there will several key places where you will need to modify the code to fit your use case:
- callREST.py: the URL of the GET request
- mapfields.py: tablename, fields (and potentially any nested fields--see example in comments of code for more context)
- swapandpublish.py: names of files, path, and login information for Tableau (username and password or token)


## Transforming the GET results
In my experience, the hardest part of this process is normalizing the results of a GET request. There are just too many APIs that format their JSON (or XML...) in completely different ways. I recommend using a tool like Postman to get a sample response of the JSON you will be 'flattening' for hyper. I've included an example of how to combine the results of multiple, paginated requests, and how to handle a single, larger response that includes information nested within the JSON.

## Scheduling
The end goal of this is to be able to schedule main.py to run at a cadence that you choose--programmatically refreshing data from the web and delivering it to your Tableau users. I would recommend using a Windows box and a batch file (or something) to run your resulting code as often as you need.

Shoutouts to the SWAPI! Learn more about it here:
https://swapi.co/
