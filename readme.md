no7ify
=======

no7ify is a simple python email and sms notification script.
Project Link: [projects.carlyleoliver.com/no7ify](projects.carlyleoliver.com/no7ify)

Running it
============

   * Edit config.sample.py
   * After adding in your conifguration values, rename it to config.py
   * Uses Gmail by default

   For environments running Python 2.4.5 and older, use sendmail245, else use the newer sendmail275.
   The difference being slicker email configuration. Had to rework for an older version since my web host was being difficult.

To Do
======
   * Throw in Twilio support, which will mean, figuring out a way to incorporate the Twilio python library onto my web host. Or else resort to the Rest API.
   * Variable subject lines
   * Add CC,BCC support
   * Twitter, Facebook, Google+ integration.


Author
======

no7ify was created by psuedokool (https://github.com/pseudokool)
