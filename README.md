Install using `pip3 install prisoners_problem`.

Run a couple samples with a given strategy:

```
>>> from prisoners_problem import simulate
>>> simulate.nsamples(1000, strategy=simulate.try_find_self)
0.3
>>>
```

`help(simulate.nsamples)` should give information for how to put in your own
strategy.

You can run `python3 -m prisoners_problem.viz` to show the results of the
visualization.
