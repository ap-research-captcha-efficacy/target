# target
modular Flask webapp capable of serving CAPTCHA challenges

## use
the project uses flask installed within a venv.

```
$ ./setup.sh
```
should create the venv and install all dependencies once you're in it, then you can use 
```
(venv) $ ./run.sh
```
once in the venv to run it.
```
$ . venv/bin/activate
```
should drop you into a venv shell any time after the setup.

## design spec

designed so that it *emulates* a real environment without *replication* (e.g. the use of tokens handled
userside is better for us when we're writing solver suites than the usual session values)

### outward behavior:
* non-standard header `X-Research` should be set for all responses
* `/captchas` returns a list of the avaliable CAPTCHA types
* served CAPTCHA decided by `/captcha/name`
    * `?modifiers=a,b,c` used for the obvious
    * e.g. `/an5char?modifiers=distort,obstruct` serves a 5-character alphanumeric CAPTCHA that has distorting and obstructive effects applied to it
    * all valid CAPTCHA responses should be JSON with two attributes
        * `challenge`, which is the challenge stored as a data URI
        * `token`, which stores a randomly generated token
            * this is used as a naive session tracker
* solutions should be POSTed to `/solutions` with the given token value and the answer, `200` means correct and `401` means incorrect
    * good responses come with the `passport_token` in a JSON object

### internal behavior:
* challenge information, including the generated token, is kept in an internal queue
    * ~~after a certain size (20 perhaps) old values can be knocked off~~
    * invalid after 60 seconds
    * CAPTCHA types are treated as separate modules and loaded during initialization
* a similar system is used for storing and authentication of 'passports'
