# pyremotepy
The most disgusting hack to call python remotely on a target I was working on recently. Don't laugh. It worked.

You'll need to pip install flask for the server. Run the server, update the command section and it will get executed once by the client.

The client will call back every 5->15 seconds, and 60->120 seconds when connection fails.

Just replace <YOUR_IP_HERE> and <YOUR_PORT_HERE> with your ip and port and you're good to go.
