Basic ROS terms and publisher ,subscriber architecture:

Nodes perform the processes and computation. A robot system has varius nodes which perform activities like control of wheel motors and are written with the help of client library and roscpp or rospy.

Master is responsible for name registration and look overall computation. Withut the master nodes will not be able to communicate with each other and exchane messages .For example before running any node we must run roscore in seperate terminal.

Nodes communicate with each other using messages. It supports standard primitive type like integer, float, boolean, array.

Messages are routed from subscriber to publisher using topic. A publisher publish the message on a given topic. A topic is a name which is used to identify the content of the name.A node intrested in a certain kind of topic will subscribe to it.In simple word the publisher and subscriber is not aware of each other existance and communicate through topic .A particular subscriber and publisher can subscibe and publish to more than one topic at a time.



![image](https://user-images.githubusercontent.com/75692297/118522380-9aae0400-b759-11eb-990d-512943b7a7ef.png)

A node offers service under name and a client uses this service to make request and wait for the reply .It is composed of a pair of message structure, one for the request and one for the reply.
