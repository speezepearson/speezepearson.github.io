---
layout: post
title:  "Odds are Unnormalized PDFs"
date:   2016-06-30 12:00:00 -0800
categories: statistics
---

We're all familiar with odds like $m:n$. There are two possibilities ($x$ and $\neg x$), and the odds tell us the ratio of the probabilities.

But there's no reason we can't extend the concept to more than two things! We could have odds over any set of possibilities!

- **Many options.** The best strategy in rock-paper-scissors is to pick the three options with odds $1:1:1$.
- **Non-mutually-exclusive options.** The odds of "planet is habitable" to "planet is inside the asteroid belt" are $1:4$.
- **Infinite options.** The odds for how many times you have to flip a coin before getting heads are $1 : \frac{1}{2} : \frac{1}{4} : \frac{1}{8} : \frac{1}{16} : \cdots$.
- **Uncountably infinite options.** The odds for how long you need to wait for an atom in your sample of radium to decay is $t \mapsto e^{-n \lambda_{Ra} t}$.

> Hey, that just looks like a probability distrib--

YUP. Odds are just PDFs that you don't bother normalizing!


As you recall, a [PDF][def-pdf] (or [PMF][def-pmf]) $p$ is just a function from some set of outcomes to $\mathbb{R}^+$, obeying two rules:

1. **Physical meaning.** If $p(x) = 2 p(y)$, then $x$ is twice as likely to occur as $y$.
2. **Normalization.** $\int p(x) \,dx = 1$ (for PDFs; for PMFs, $\sum_x p(x) = 1$).

The first requirement is useful because it *relates the PDF to the real world.* That's a good feature to have. But odds have it too.

The second requirement is useful because it lets you take a p-value in isolation and interpret it physically. Odds don't have that feature, but you don't always need it.


This makes a few things clear about odds:

- Every PDF (or PMF) is an ODF, since there are strictly fewer restrictions on ODFs than on PDFs.
- In fact, every PDF corresponds to infinitely many different ODFs: if you take a PDF and multiply it by any positive real number, it retains the exact same physical meaning.
- Does every ODF correspond to a PDF? No: some ODFs can't be normalized (e.g. the ODF $o(x) := 1$, over the real numbers). (Are these ODFs useful? Dunno yet.)


[def-pdf]: https://en.wikipedia.org/wiki/Probability_density_function
[def-pmf]: https://en.wikipedia.org/wiki/Probability_mass_function
