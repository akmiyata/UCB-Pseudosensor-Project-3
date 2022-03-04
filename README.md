# UCB-Pseudosensor-Project 3

This is the first project in "M2M and IoT Interface Design and Protocols" (ECEA 5348), and picks up where Project 2 from ECEA 5347 left off. I have included four files:
  1.  UCB5348-Pseudosensor-Project1.pdf: Project overview, including requirements, assumptions, and other notes, as well as screenshots of the UI in several scenarios.
  2.  boto_retrieve.py:   
  4.  pseudosensor.py: Starter code used to generate pseudorandom weather information. I decided to use the class-supplied file this time rather than my own code, just to mix things up a bit. 
  5.  publish_final.py: Setup MQTT message queue, generate weather data, and add to queue.

# What I learned

Unlike prior projects, there was a lot of unfamiliar tech here for me. Just learning to use AWS certificates took much more time than I anticipated. Boto3 was also new to me, but like most other libraries, it didn't take too long to figure out how to use tools for my specific application. 

Initially I thought the biggest hurdle for me would be adjusting to the Cloud9 IDE, since I'm so used to VSCode, but Amazon did a great job making the IDE user friendly and a fairly seemless transition from VSCode. I just wish other AWS tools were like that (see UCB-Pseudosensor-Project 4).
