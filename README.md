![Cover](images/pollution.png)

### What is this?

This is a Simple Twitter Bot that gathers pollution data from MojVozduh’s API made by @jovanovski and checks if it’s above the normal values which by AQI standards is 50 and tweets to The Munipicalities, Minister of Environment and Spatial Planning and 2 eco activists organization.

### How do I run it?

You’ll need to Create a Twitter Account and a Twitter App for it to connect to twitter and tweet. Once you’ve done that fill the config.py with your credentials and install tweepy using pip.

This Project runs on Python3 and only Python3 will be supported due to issues with Unicode.

To run the bot every 2 hours or more please use Cron. 
`0 */2 * * * python3 /root/Bots/AirPollutionNotifier
/botv1.py`
This cron job runs every 2 hour

Photo: [A storm is coming photo by Witch Kiki (@littlewitch) on Unsplash](https://unsplash.com/photos/E9hVNb7wOY8)
