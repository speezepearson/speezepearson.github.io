---
layout: post
title:  "Practical Log-Odds"
date:   2015-12-29 12:00:00 -0800
categories: statistics
summary: "Introduces a neat way of thinking about probabilities ('log-odds'), suitable for mental ballparking."
---

I assert that for everyday purposes, you should start thinking about probabilities in this wacko weird way called "log-odds," which (I claim) makes it easier for you to:

- estimate probabilities;
- update those estimates in response to new information; and
- remember those estimates.

Let me explain myself.


Motivation
----------

By far, the most common everyday application of statistics is assigning confidence to statements. How likely is it that there'll be a pop quiz in class today? That you'll crash your car if you drive there? That you forgot to turn the oven off?

Unfortunately, the way your statistics class trained you to think about probabilities (i.e. numbers between zero and one) is not well-suited to this task. The ability to quickly and accurately update your beliefs in response to new information is an **incredibly important** skill, and when using probabilities, that kind of calculation requires impressive mental gymnastics.

The classic example:

> The probability of breast cancer is 1% for a woman at age forty who
> participates in routine screening. If a woman has breast cancer, the
> probability is 80% that she will get a positive mammography. If a
> woman does not have breast cancer, the probability is 9.6% that she
> will also get a positive mammography. A woman in this age group
> had a positive mammography in a routine screening. What is the
> probability that she actually has breast cancer? ____%

Your intuition will do a terrible job here, as evidenced by 95% of physicians getting it horribly wrong[^bayes-example-source]. Even if you're familiar with Bayes's Theorem, applying it involves calculating $\frac{0.8}{.01\*.8 + .99\*.096}$, which takes me several seconds to even ballpark in my head.

If only there were a better way.

There's a better way.


Log-Odds
--------

Without any motivation for the moment, let's define how to convert a probability to "log-odds": the log-odds of an event $x$ is $10\cdot\log_{10} \frac{P(x)}{P(\neg x)}$. (Because we're gonna be using $10\cdot\log_{10}$ all over the place, let's define a function $dB(x) := 10 \log_{10} x$.)

Some features of this definition:

- Log-odds are numbers, going from $-\infty$ to $\infty$.
- Intuitively:
  * $-\infty$ corresponds to "impossible";
  * $-10$ corresponds to (about) "one in ten";
  * $0$ corresponds to "no idea", i.e. probability $0.5$;
  * $10$ corresponds to (about) "nine out of ten"; and
  * $\infty$ corresponds to "certain."
- Intuitively, a log-odds difference of $10$ means something like "I'm ten times as certain": something with a log-odds of $5$ has odds of about three-to-one, while $-5$ corresponds to odds of one-to-three. $50$ corresponds to hundred-thousand-to-one, and $60$ corresponds to million-to-one.
- Because this behavior resembles the behavior of other things traditionally measured in decibels (dB), log-odds are usually measured in dB as well. $\newcommand{\dB}{\,\text{dB}}$


#### Advantages

For purposes of ballparking things in your head, log-odds are a much more intuitively meaningful representation of certainty than are probabilities. Reasons:

- **They're memorable.** You're probably not very good at remembering the difference between probabilities $.00001$ and $.000001$, or $.95$ and $.99$. They *feel* the same, at least to me. But you're *great* at remembering the difference between $-40\dB$ and $-50\dB$, or $13\dB$ and $20\dB$, the log-odds representations of those same probabilities.

- **They have great resolution.** Log-odds from $-100\dB$ to $100\dB$ describe all the levels of certainty you're likely to use in your life:

  * A log-odds of $0\dB$ corresponds to "one to one": "No clue."
  * A log-odds of $5\dB$ corresponds to "(about) three to one": "Pretty sure."
  * A log-odds of $10\dB$ corresponds to "ten to one": "Very confident."
  * A log-odds of $50\dB$ corresponds to "a hundred thousand to one": what you usually mean when you say "I'm 100% certain."
  * A log-odds of $100\dB$ corresponds to "ten billion to one": about as certain as it is possible for you to be of anything, given that you might be having a bizarre, complex, strangely specific hallucination.
  <br/><br/>

- **They help you update your beliefs in response to new information.** Often, you gain information about something (e.g. whether you have breast cancer) by seeing a *probable consequence* of it (e.g. a mammography result). In these situations, you can typically easily ballpark these questions:

  * "How likely did I used to think $x$ was?"
  * "How likely is $obs$ (my observation) in a world where $x$ is true?"
  * "How likely is $obs$ (my observation) in a world where $x$ is false?"
  <br/><br/>

  To estimate $P(x\|obs)$ from this, you need to multiply, add, and divide, which is tough to do in your head. But to compute $L(x\|obs)$ (the corresponding log-odds), you just need  addition, subtraction, and a feeling for logs:

  $$ L(x|obs) = L(x) + dB(P(obs|x)) - dB(P(obs|\neg x)) $$

  I'll put the mathy "why" in a footnote.[^bayes-math]


#### Disadvantages

There are reasons log-odds haven't taken over the world. It would be dishonest not to list them.

- **Memorization is annoying.** If you hop on this bandwagon, you'll need to quickly compute $10 \log_{10}$ in your head. It's slightly easier than it sounds ($\pm 10\dB$ for each order of magnitude, then use a lookup table for whatever's left), but, at least the way I do it, it requires you memorize this table:

  * $10 \log_{10} 2 \approx 3$
  * $10 \log_{10} 3 \approx 5$
  * $10 \log_{10} 4 \approx 6$
  * $10 \log_{10} 5 \approx 7$
  * $10 \log_{10} 6 \approx 8$
  * $10 \log_{10} 8 \approx 9$
  <br/><br/>

- **Addition is harder.** What's $5\dB + 3\dB$? I think it's probably like $7\dB$, but I'm not sure. Addition in log-space is hard.

- **Reduced interoperability.** Not many people use log-odds, so you'll have to translate whenever you talk statistics with a heathen.

That said, I think it's worth it.


Log-Odds: a Parable
-------------------

You're sitting in a coffee shop, people-watching through the steam wafting off your cappuccino. Your boyfriend, Alex, called earlier to let you know he'd have to work late, and, feeling in a pleasantly quiet mood today, you decided to lounge around downtown until he gets out.

On the sidewalk opposite, you glimpse Alex, strolling alongside an attractive woman.

You're not immediately sure how to parse this information, but your muscles feel like they might not respond anyway, and rush-hour traffic soon obscures the duo. You stare absently across the street for a few more moments.

Then, not one to be run away with by your emotions, you put down your coffee, pick up your pencil, and begin to figure.


#### Estimates
Okay... things with Alex are going very well. You haven't picked up any signs of discontentment, and he seems like a moral, upstanding fellow -- five minutes ago, you'd have placed the probability of his cheating at... your first instinct is $1/1000$ ($-30\dB$), but correcting for overconfidence bias, let's call it $1/100$ ($-20\dB$).

If there's Another Woman, you'd expect him to be walking with her essentially every time he claimed a late night -- probability $1$ ($0\dB$). If there's not, how often would he be walking with a pretty lady while you thought he was at work? Well, he might be taking a short break, or getting some air while talking over some issue with a colleague -- call that probability about $1/40$ ($-16\dB$), because while he certainly does it once in a while, it's <i>a priori</i> unlikely he'd be doing it at *this very moment*.

#### Ending 1: Probabilities

So, plugging those numbers into Bayes's Theorem, you get

$$\begin{align}
P(cheat|walk) &= P(cheat) \frac{P(walk|cheat)}{P(walk)} \\
              &= P(cheat) \frac{P(walk|cheat)}{P(cheat) P(walk|cheat) + P(\neg cheat) P(walk|\neg cheat)} \\
              &= (.01) \frac{1}{(.01)(1) + (.99)(.025)} \\
              &\approx 2/7
\end{align}$$


#### Ending 2: Log-Odds

$$\begin{align}
L(cheat|walk) &= L(cheat) + dB(P(walk|cheat)) - dB(P(walk|\neg cheat)) \\
              &= -20 + 0 - (-16) \\
              &= -4
\end{align}$$

#### Conclusion

Well. He's *probably* not cheating, but that's still a worryingly high probability.

<i>Hm,</i> some detached part of you notices, <i>The log-odds approach <strong>was</strong> much easier -- just like that blog post promised.</i>




<br/><br/>
<hr/><hr/><hr/><hr/>
<br/><br/>




[^bayes-example-source]: Result of Eddy 1982, according to [Gigerenzer and Hoffrage 1995][gigerenzer]. I couldn't find Eddy except behind paywalls.

[^bayes-math]: Okay, we can all get behind Bayes's Theorem, right? And recall that the function $dB$ is pretty much just a log, so it distributes the same way over multiplication. Then <br/> $$\begin{align}
    L(x|obs) &:= dB\left(\frac{P(x|obs)}{P(\neg x|obs)}\right) \\
             &= dB\left(\frac{P(x) P(obs|x)/P(obs)}{P(\neg x) P(obs|\neg x)/P(obs)}\right) \\
             &= dB\left(\frac{P(x)}{P(\neg x)} \cdot \frac{P(obs|x)}{P(obs|\neg x)}\right) \\
             &= dB\left(\frac{P(x)}{P(\neg x)}\right) + dB\left(\frac{P(obs|x)}{P(obs|\neg x)}\right) \\
             &= L(x) + dB(P(obs|x)) - dB(P(obs|\neg x))
  \end{align}$$<br/>

[gigerenzer]: http://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf
[bayess-theorem]: https://en.wikipedia.org/wiki/Bayes%27_theorem#Statement_of_theorem
[bayes-example]: http://www.math.cornell.edu/~mec/2008-2009/TianyiZheng/Bayes.html
