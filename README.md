Gharret Wilcut
4/29/2024
CS 2500 
Honors Project Report
Delivery Suggestion System Honors Project
	In the past several years there have been several companies offering services when it comes to food based delivery services. Companies like Doordash, UberEats, and Grubhub have all provided a similar service to what I have prototyped in my project. 
	
My simulation uses OSMNX to get an accurate graph of the city Chicago to be used for these tests. I also acquired the locations of restaurants in Chicago by using their food inspection data. I combined these to match a node on the graph to the approximate location of a restaurant using its latitude and longitude.
  
<img src="pictures\get_graph_function.JPG"
     alt="Get Graph Function"
     style="float: left; margin-right: 10px;" />

The main algorithm holding this whole project together is Dijkstra’s, I have been using it in conjunction with the heap data structure. The addition of heaps being used decreased the total time to process the algorithm by roughly 90% going from taking it around 70 seconds down to 7 seconds this was a major help seeing that otherwise this program would have taken days to run. Originally the Dijkstra's algorithm did have a target built in, making the algorithm stop when it found the target node. This allowed for a roughly 10% reduction even further but I stopped using it because I had concerns for whether or not it was interfering with the program causing key errors. It can easily be reinstated and allow for a reduction in overall time but due to how long the program takes to finish I worried it would be a fruitless endeavor.

<img src="pictures\dijkstra.JPG"
     alt="Dijkstra Algorithm"
     style="float: left; margin-right: 10px;" />

I ran into several issues throughout the entirety of the project most of which occurred at the end when trying to get data on the average rewards. The main two being that I didn’t actually set up unique identifiers for each driver and that there was a chance of the driver, restaurant or dropoff location to have the same node location. With the issue of there not being any unique identifiers for drivers I just set them to their memory location, while a simple and easy fix, this will probably need to be changed in the future. The reason that the drivers not having a unique identifier is such a big problem is that if a driver has the same age/experience it throws an error because I have the driver trying to be in a heap as a tuple with the age/experience set to the first value. So when the ages are the same it moves on to the driver and a driver cannot have < be used on it. The second big problem was that the nodes might be the same. I fixed this by checking if a node is already in use and if so it goes and gets a different one. I could only become aware of these issues after running my program for several hours. I had to fix these at midnight while my laptop screen was also broken for some reason. 

<img src="pictures\runtime_analysis_honorsProject.JPG"
     alt="Runtime Analysis"
     style="float: left; margin-right: 10px;" />
	
In testing I had it trying to get an average on the rewards drivers would earn based on the number of drivers and orders there are. I had them be one to one so one driver for every order. I had it go from 2 to 20 drivers and orders with only having 20 monte carlo runs. This was not ideal considering the small amount of runs would not give a completely accurate picture of what the program would do in most cases at those amounts of drivers but it was either that or have it run for an incredibly long time because even at this level it took nearly five hours to finish processing on my own hardware. In testing in the future I would like to use the Mill to test this program with bigger MC runs and with more orders.


<img src="pictures\finished graph.png"
     alt="Finished Graph"
     style="float: left; margin-right: 10px;" />


As the number of deliveries rise the best reward looks to be in an upward trend as well and with more monte carlo runs this would have been more evident. This at the same time the average reward tends to be stable with a slight rise as the orders increase in volume. 

This project taught me a lot about algorithms and how using certain data structures can enhance the efficiency of the algorithms. It was very frustrating at times and I didn’t achieve all I wanted. I really wanted to use a different way at which the program decides which driver goes where. I wanted to have it go through all the driver’s best choices in terms of reward. If no one else had that as their first choice that was going to be their delivery then base it off of their experience. I wasted a lot of time trying to get that function to work and I never could so I had to fall back on the original where it is based solely on the experience or in this case now the memory address of the driver since it kept giving me errors otherwise. I also learned that even if something works on a small scale, when used in larger and larger sample sizes errors can pop up that you otherwise haven’t dealt with or known about. 
