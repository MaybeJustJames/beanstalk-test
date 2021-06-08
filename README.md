# Job queuing

Scientific software services often require long run-times. This is at odds with the synchronous request/response paradigm of the web. Therefore it is necessary to run long-running compute workloads "in the background". This is very often achieved in an ad-hoc manner.

## [Beanstalkd](https://beanstalkd.github.io/)
> Beanstalk is a simple, fast work queue.

Beanstalk provides a generic interface for (priority) job queuing. There can be multiple independent or collaborating job producers and job consumers written in a variety of [programming languages](https://github.com/beanstalkd/beanstalkd/wiki/Client-Libraries). If a client library for a language does not exist (e.g. R) then implementing the text-based protocol is fairly simple.
