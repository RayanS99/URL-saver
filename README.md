# Individual assignment - Save for later

In this exercise you'll create a simple web application in which you
can store links for reading later.

The app is expected to run locally on the user's computer, so we **won't
need to deal with signup or authentication.**.

For inspiration, we'll build something similar to
[del.icio.us][delicious], [Pocket][pocket], or Read it Later.

[delicious]: http://del.icio.us
[pocket]: http://getpocket.com

## Exercises

### Exercise 1

Create the index of the application.  It should be served on the `/`
route.

This screen should show all links stored by the user.  Each link must
contain a title and a URL, and it should also display the image in
`images/link.png`.

### Exercise 2

Make it possible to add new links.  The fields we must gather from the
link are:
- URL
- title

Whenever a link is added, it must appear in the index screen.

### Exercise 3

Make it possible to mark items as read.  Whenever we do so, they
must not appear in the index anymore.


## Grading

| Area                               | Description                                                 | Possible points |
|:-----------------------------------|:------------------------------------------------------------|:----------------|
| **Exercise 1**                     |                                                             | 2               |
| **Exercise 2**                     |                                                             | 2               |
| **Exercise 3**                     |                                                             | 2               |
| **DB**                             | A proper database is used instead of storing data in memory | 1               |
| **Deployment**                     | The app is deployed (App Engine, Heroku, ...)               | 1               |
| **General coding & app behaviour** |                                                             | 2               |
