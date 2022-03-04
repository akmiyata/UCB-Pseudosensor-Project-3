# UCB-Pseudosensor-Project 3

This is the first project in "M2M and IoT Interface Design and Protocols" (ECEA 5348), and picks up where Project 2 from ECEA 5347 left off. I have included three files:
  1.  UCB-Pseudosensor-Project2.pdf: Project overview, including requirements, assumptions, and other notes, as well as screenshots of the UI in several scenarios.
  2.  index.html: Landing page for the user interface. I chose function over form due to timing constraints; normally this would bother me, but I'm focusing on my current  
      classload and job hunt at the moment.  
  4.  getOne.html: This page displays one set of pseudorandom weather values, generated on the fly. 
  5.  getTen.html: This page displays ten sets of weather values, with timestamps incrementing one second between each reading. Maximum, minimum, and average values are also displayed. 

# What I learned

Despite the recent upload, it's been awhile since I worked on this project... I was already quite familiar with HTML/CSS, so it was quite easy to setup a VERY basic UI (normally I'd make the UI "prettier", but time constraints did not allow me to do so... maybe one day...). Tornado Web Server was a new technology for me, but I was already somewhat familiar with client-server communication (via HTTP), so syntax was the only real hurdle there.  I think the biggest takeaway from this project was that it could've been a much quicker and less painful process if I had started with Tornado documentation; tutorials are great, but often times going to the source will give you a much clearer picture that fits your specific needs.
