### How to make it work
-----

1. [Open this link](https://discord.com/oauth2/authorize?client_id=1436776940370395267&permissions=8&integration_type=0&scope=bot)

# OR!!!

1. Create a ``token.txt``.
2. Go to [Discord Developers](https://discord.com/developers/)
3. Sign in / Log in
4. Open 'My Applications'
5. Click 'New Application'
6. Name it something like '*Cleaner*'
7. And click the checkbox
8. Confirm you are not a robot
9. Set up the App Icon, Description, Tags and if you want - links at the bottom.
10. Then click 'Bot' - And set up the Bot Icon, Bot Banner, Username, and reset the token.
11. Copy the token and put it into ``token.txt``
12. Scroll down to **Privileged Gateway Intents**, and tick all of the boxes.
13. Then for Bot Permissions, Click *Administrator*. This is because the bot needs permissions to delete certain messages.
14. Click OAuth2.
15. Scroll down to ***OAuth2 URL Generator*** - and click '*bot*'.
16. Scroll down ***again*** to "Bot Permissions" - and click *Administrator*. Again, this is because the bot needs permissions to delete certain messages.
17. Make sure Interaction Type is "***Guild Install***".
18. Copy the generated URL.
19. Open it, or send it to your friends
20. Grant it permissions
21. Run ``main.py``
22. Enjoy!
