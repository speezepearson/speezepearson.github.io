---
layout: post
title:  "Automated Debugging"
date:   2016-03-20 12:00:00 -0800
categories: compsci research
---

I.
--

Debugging (taking the "almost" out of "software that almost works") is difficult and expensive. Software developers see this. And, as always when software developers see something difficult and expensive, they ask, "Can we make computers do this a million times faster and cheaper?"

So you say, "Computer! Make my program work!"

And your computer responds, "How do I know what you want? I mean, your program does *something*. I guess you want it to do something else? But I don't know what it means to 'fix' the program."

Your first instinct is to describe what's wrong, but you quickly realize that an exact description of what's wrong is equivalent to the bugfix itself: exactly what you're trying to make the *computer* do. You need a shortcut, an approximation.

So, instead: "Computer! Consider yonder test suite. Notice the numerous assertions about how the program should behave, run on certain inputs. Notice how there are some tests that *fail*: the program behaves differently than expected in those cases. You see?"

"I see."

"Computer! A *correct* version of my program will cause all the tests to pass, instead of fail."



II. Automated Software Repair.
------------------------------

"Computer! Fix my program, so that all those tests pass."

This gives birth to the field of automated program repair. I'm not well-educated on this topic. Many people have made repair tools, and last I heard, a famously grumpy fellow named Martin Rinard tried to show how useless they all were by writing his own, which did just as well as anybody else's, but worked by just deleting random lines of code.

Personally, I'm skeptical about this whole approach. It seems to me that "fixes the bug" is a much, much, **much** stronger requirement than "makes the tests pass." Automated repair tools, as far as I've seen, search for only simple patches, and I doubt correctness is correlated with simplicity.



III. Fault Localization.
------------------------

"Computer! I understand that there is no existent mechanism by which I can create in your mind a vision conjugate to my own of the fixed program. I accept this. Instead, let us co-operate. Gaze again upon yonder test suite. Notice again that some tests pass, while others fail. First, inspect the execution of each passing test. Second, inspect the execution of each failing.

"Computer! See you any difference?"

This gives birth to the field of fault localization (FL), which I've been working on for -- my goodness, 2% of my life.

There are a couple different flavors, but the simplest (and, I believe, nearly the best) is "spectrum-based FL." Intuitively, if there's a line of code that's run by *lots* of failing tests and *very few* passing tests, that line is very suspicious: it's probably the buggy line that's making your tests fail. Conversely, if a line is run almost exclusively by *passing* tests, it's not suspicious at all.

So, you just tally up how many passing tests cover each line, and how many failing tests cover each line, and plug those numbers into some formula that goes *up* with number of failing tests and *down* with number of passing tests, and then you have a "suspiciousness" for every line in your program. And then you start examining those lines, starting with the most suspicious. Ta-da!

My current research project has involved running spectrum-based FL on bugfixes drawn from several open-source projects. On average, the first statement associated with the fault appears 2% of the way through the ranking[^ranking-defn] -- pretty good, I think! Of course, this relies on you being able to recognize the bug as soon as you see any buggy line, which isn't a given... but this is a good first-order approximation.





<br/><br/>
<hr/><hr/><hr/><hr/>
<br/><br/>


[^ranking-defn]: i.e. you have to examine 2% of the lines of code in the modules of your program that any failing test loaded. We did this in Java, using [Defects4J][d4j]'s library of bugs.


[d4j]: https://github.com/rjust/defects4j
