---
layout: post
title:  "What Makes a Good Statistical Test"
date:   2015-12-26 12:00:00 -0800
categories: statistics
---

My statistics education (and yours too, probably) was largely of the form:

- In *this* situation, you should use the $\chi^2$ test: first, write your data in a table, then...
- In *that* situation, you should use the Student t-test: first, plug your numbers into this formula, then...
- In *this* situation, you should use the Wilcoxon signed-rank test: first, subtract the second number of each pair from the first number, then...
- In *that* situation...

This is good enough for most purposes, because usually you're in one of those situations. But, because it doesn't teach *what it means* for a statistical test to be good in a particular situation, if you find that you're *not* in any of those situations, you're in trouble.

The goal of this post is to tie together some facts that maybe came up in your statistics class, but whose fundamental importance was not sufficiently emphasized.


Important Facts
---------------

Here is how to tell whether a test is good or not:

- A "statistical test" is basically just a "weirdness function" (usually called, less descriptively, a "test statistic"), which takes an experimental result (e.g. a sequence of coin flips, or several piles of numbers) and returns a number.
- No result has a p-value. A result has a p-value with respect to (a) a test and (b) a null hypothesis. Saying that your experimental result "has a p-value of 0.03, according to [test], with null hypothesis $H_0$" means that you plugged the result into [test]'s weirdness function, got some weirdness, and calculated that if $H_0$ is true, you couldn't possibly see so large a weirdness more than 3% of the time.
- No test is "good"; no test is even "good at telling whether [some null hypothesis] is true." Tests are only "good at distinguishing between *this* hypothesis and *that* hypothesis." A test is good at distinguishing between $H_0$ and $H_1$ if it tends to produce small p-values (with respect to $H_0$) in worlds where $H_1$ is true.

And that's it!


### Toy Example

How does this fit into your existing knowledge base? Well, to illustrate, here are some statistical tests you might apply to a sequence of coin flips:

1. $ weirdness := \left\| nHeads - nFlips/2 \right\| $ is a good statistical test for distinguishing between the hypotheses "this coin is fair" and "this coin is biased," because it tends to produce larger numbers in worlds where the coin is biased.

   Because this test is so simple, so often useful, and so good at its job, people have made big tables where you can look up the p-value for any given $nHeads$ and $nFlips$. But you could trivially do that yourself!

2. $ weirdness := nToggles/nFlips $, where $nToggles$ is the number of flips that are different from their predecessors, is good for distinguishing between the hypotheses "this coin is fair" and "this coin has some weird hidden state that makes it 'anti-sticky,' i.e. each flip wants to be different than its predecessor, i.e. I kinda expect to see $HTHTHTHT$ a lot."

   Because anti-stickiness isn't a common alternative hypothesis, this test isn't used very often, and nobody has made a big p-value table for you. But that doesn't mean it's not good at its job.

Note that even though these two statistical tests operate on the same inputs, and have the same null hypothesis, they are **terrible** at doing each other's jobs. A biased coin will tend to have even *fewer* toggles than a fair coin, so test (2) will mark a biased coin as not-weird-at-all; and an anti-sticky coin will come up Heads even *closer* to half the time than a fair coin, so test (1) will mark an anti-sticky coin as not-weird-at-all.


Takeaways
---------

- Every statistical test is designed specifically to distinguish between two particular hypotheses.
- The only metric of a test's quality is how well it distinguishes those hypotheses.
- Every statistical test (that I'm aware of) boils down to a single "weirdness function" that generally produces small numbers when the null hypothesis is true, and big numbers when the alternative hypothesis is true.
